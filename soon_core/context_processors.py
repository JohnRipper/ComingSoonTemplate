from .models import SiteSettings

def site_settings(request):
    """
    Makes the SiteSettings object available in the context of all templates.
    """
    # .get_solo() is a helper from django-solo that retrieves the
    # single settings instance, creating it if it doesn't exist yet.
    return {'site_settings': SiteSettings.get_solo()}