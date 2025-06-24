# /home/base/ProjectsV2/ComingSoonTemplate/soon_core/views.py

from django.shortcuts import render, redirect
from .forms import SubscriberForm


def index(request):
    """
    Renders the index page and handles form submission.
    If the request is from HTMX, it returns an HTML partial.
    Otherwise, it performs a full redirect.
    """
    # Get the 'ref' parameter from the URL. If it's not there, default to 'direct'.
    referral_source = request.GET.get('ref', 'direct')

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()  # No need for commit=False, the form handles the referral_source now

            # Check if the request is from HTMX
            if request.htmx:
                # If it is, return the success message partial
                return render(request, 'partials/success_message.html')

            # For non-HTMX requests, redirect as before
            return redirect('success_page')  # Fallback for non-JS users
        else:
            # If the form is invalid, we want to re-render the form with errors.
            # For HTMX, we can just send back the form partial.
            if request.htmx:
                return render(request, 'partials/subscriber_form.html', {'form': form})

    # For initial GET requests, create a form instance with the referral source
    form = SubscriberForm(initial={'referral_source': referral_source})
    context = {
        'form': form
    }
    return render(request, "index.html", context)