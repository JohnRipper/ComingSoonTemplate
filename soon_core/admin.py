from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteSettings, Subscriber

# Register the singleton model
admin.site.register(SiteSettings, SingletonModelAdmin)

# You can keep your existing Subscriber admin if you have one
@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'referral_source', 'created_at')
    list_filter = ('referral_source', 'created_at')
    search_fields = ('email',)