from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm, NewsletterSignupForm


def index(request):
    ''' A view to return the home page'''

    hide_toast_cart = request.session.pop('hide_toast_cart', False)
    form = NewsletterSignupForm()
    context = {
        'hide_toast_cart': hide_toast_cart,
        'form': form
    }

    return render(request, 'home/index.html', context)


def contact_view(request):
    ''' A view to handle the contact page '''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                "Thanks for contacting us!",
                (
                    "Hi {},\n\nThanks for reaching out. We’ll get back to you "
                    "shortly.\n\n- The Wangers Team".format(contact.name)
                ),
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
            )
            messages.success(
                request,
                "Your message has been submitted. We'll be in touch soon!"
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def newsletter_signup(request):
    '''A view to handle newletter signup submission'''
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "You’ve been signed up for the newsletter!"
            )
            request.session['hide_toast_cart'] = True
        else:
            messages.error(request, "Please enter a valid email.")
            request.session['hide_toast_cart'] = True
    return redirect(request.META.get('HTTP_REFERER', '/'))
