from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """
    A form for capturing new subscribers, based on the Subscriber model.
    """

    class Meta:
        # Link this form to the Subscriber model.
        model = Subscriber

        # Specify which model fields should be included in the form.
        fields = ['email', 'referral_source']

        # Customize the HTML widgets for each field.
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email address...',
                'class': 'form-control',  # Example class for Bootstrap styling
                'aria-label': 'Email Address',
            }),
            # This makes the referral_source field a hidden input in the HTML.
            # The user won't see it, but its value will be submitted with the form.
            'referral_source': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        """
        Override the default __init__ to remove the labels, as placeholders
        are often sufficient for a simple form like this.
        """
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['referral_source'].label = ""
