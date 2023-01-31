from django.urls import path
# from .views import GoogleCalendarInitView, GoogleCalendarRedirectView
from .views import TestView,GoogleCalendarRedirectView,GoogleCalendarInitView

urlpatterns = [
    path('init/', GoogleCalendarInitView, name='google_calendar_init'),
    path('redirect/', GoogleCalendarRedirectView, name='google_calendar_redirect'),
    path('test/', TestView, name='calendar_test'),

]