from django.urls import path
from . import views

# This is a common practice to namespace your app's URLs.
# It helps prevent URL name collisions with other apps.
app_name = 'soon_core'

urlpatterns = [
    # This pattern matches the root URL of the app (e.g., '/').
    # It maps to the `home_view` you created.
    # The `name='home'` allows you to refer to this URL easily in templates and views.
    path('', views.index, name='home'),

    # You could add a 'success' page for after the user subscribes.
    # path('success/', views.success_view, name='success_page'),
]
