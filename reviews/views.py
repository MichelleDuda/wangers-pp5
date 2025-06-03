from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
        return Review.objects.filter(approved=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        reviews = context['reviews']

        # Attach total_likes and has_liked for each review instance
        for review in reviews:
            review.total_likes = review.total_likes()
            review.has_liked = review.has_liked(user)
        return context


@login_required
def create_review(request, menu_item_id=None):
    menu_item = None
    if menu_item_id:
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print("Valid Form")
            review = form.save(commit=False)
            review.menu_item = menu_item
            review.user = request.user
            review.approved = False  # Ensure new review is pending approval
            review.save()
            messages.success(request, "Your review has been submitted for approval.")
            return redirect('review_list')
        else:
            messages.success(request, "There was an error processing your review. Please try again or contact us if you continue to have trouble!")
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'menu_item': menu_item,
    }

    return render(request, 'reviews/review_form.html', context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            edited_review = form.save(commit=False)
            edited_review.approved = False  # Need re-approval after edit
            edited_review.save()
            messages.success(request, "Your review has been updated and submitted for re-approval.")
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {
        'form': form,
        'menu_item': review.menu_item
    })

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")
    
    menu_item_id = review.menu_item.id
    review.delete()
    return redirect('review_list')


def toggle_like(request, review_id):
    ''' A view to toggle the like feature for a review'''
    review = get_object_or_404(Review, id=review_id)
    like, created = Like.objects.get_or_create(user=request.user, review=review)

    if not created:
        like.delete()

    return redirect('review_list')