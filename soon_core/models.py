from django.db import models
from solo.models import SingletonModel


class SiteSettings(SingletonModel):
    """
    A singleton model to store site-wide settings that can be
    edited in the Django admin.
    """
    # General Site Information
    project_name = models.CharField(max_length=100, default="Project Nova")

    site_domain = models.CharField(
        max_length=100,
        blank=True,
        help_text="The full domain of the site (e.g., https://www.projectnova.com)"
    )

    og_image = models.ImageField(
        upload_to='site_graphics/',
        blank=True,
        null=True,
        help_text="Social sharing image (1200x630px recommended)."
    )


    # New field for the main headline
    hero_headline = models.CharField(
        max_length=200,
        default="A New Digital Frontier Awaits."
    )

    # New field for SEO
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="SEO description for search results (max 160 characters)."
    )

    project_description = models.TextField(
        blank=True,
        help_text="The main tagline or description shown on the homepage."
    )
    main_graphic = models.ImageField(
        upload_to='site_graphics/',
        blank=True,
        null=True,
        help_text="The main hero image for the coming soon page."
    )

    # Social Media Links
    twitter_url = models.URLField(blank=True, help_text="Your full Twitter URL (e.g., https://twitter.com/yourprofile)")
    linkedin_url = models.URLField(blank=True, help_text="Your full LinkedIn URL")
    github_url = models.URLField(blank=True, help_text="Your full GitHub URL")

    # YouTube Embed
    youtube_embed_url = models.URLField(
        blank=True,
        help_text="Optional. Paste the 'embed' URL from YouTube. e.g., https://www.youtube.com/embed/your_video_id"
    )

    google_analytics_id = models.CharField(
        max_length=20,  # e.g., 'UA-XXXXX-Y' or 'G-XXXXXXXXXX'
        blank=True,
        help_text="Optional. Your Google Analytics Tracking ID (e.g., UA-XXXXX-Y or G-XXXXXXXXXX)."
    )

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Settings"


class Subscriber(models.Model):
    """
    Represents a user who has subscribed to the mailing list
    on the 'coming soon' page.
    """
    email = models.EmailField(
        unique=True,
        help_text="The subscriber's email address."
    )
    referral_source = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="The source from which the subscriber was referred (e.g., twitter, product_hunt)."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date the subscriber signed up."
    )

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"