from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView
from .models import Review, Like
from menu.models import MenuItem
from .forms import ReviewForm
from django.http import HttpResponseForbidden


class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

    def get_queryset(self):
        queryset = Review.objects.filter(approved=True).order_by('-created_at')
        menu_item_id = self.request.GET.get('menu_item')
        search_query = self.request.GET.get('search')

        if menu_item_id:
            queryset = queryset.filter(menu_item__id=menu_item_id)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(body__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        reviews = context['reviews']

        # Attach total_likes and has_liked for each review instance
        for review in reviews:
            review.total_likes = review.total_likes()
            review.has_liked = review.has_liked(user)

        context['menu_items'] = MenuItem.objects.all()
        context['request'] = self.request
        context['hide_toast_cart'] = self.request.session.pop(
            'hide_toast_cart',
            False
        )

        return context


@login_required
def create_review(request, menu_item_id=None):
    menu_item = None
    if menu_item_id:
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.menu_item = (
                menu_item if menu_item else form.cleaned_data['menu_item']
            )
            review.user = request.user
            review.approved = False  # Ensure new review is pending approval
            review.save()
            messages.success(
                request,
                "Your review has been submitted for approval."
            )
            request.session['hide_toast_cart'] = True
            return redirect('review_list')
        else:
            messages.success(
                request,
                (
                    "There was an error processing your review. "
                    "Please try again or "
                    "contact us if you continue to have trouble!"
                )
            )
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'menu_item': menu_item,
        'hide_toast_cart': True,
    }

    return render(request, 'reviews/review_form.html', context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to edit this review."
        )

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            edited_review = form.save(commit=False)
            edited_review.approved = False  # Need re-approval after edit
            edited_review.save()
            messages.success(
                request,
                "Your review has been updated and submitted for re-approval."
            )
            request.session['hide_toast_cart'] = True
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'menu_item': review.menu_item,
        'hide_toast_cart': True,
    })


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden(
            "You are not allowed to delete this review."
        )

    if request.method == 'POST':
        review.delete()
        messages.success(request, "Review deleted.")
        return redirect('review_list')

    # Store the previous page (fallback to home if not available)
    referer = request.META.get('HTTP_REFERER', reverse('review_list'))

    return render(request, 'confirm_delete.html', {
        'item_name': f"your review from {review.created_at.strftime('%B %d, %Y')}",
        'delete_url': reverse('delete_review', args=[review_id]),
        'cancel_url': referer,
    })


def toggle_like(request, review_id):
    ''' A view to toggle the like feature for a review'''

    if request.user.is_authenticated:
        review = get_object_or_404(Review, id=review_id)
        like, created = Like.objects.get_or_create(
            user=request.user,
            review=review
        )

        if not created:
            like.delete()
    else:
        messages.error(
            request,
            "You must be logged in to like a review."
        )
    return redirect('review_list')
