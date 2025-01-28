from django.urls import path
from .views import (
    NewsView,
    AboutView,
    PrivacyView,
    ContactView,
)


urlpatterns = [
    path('news/', NewsView.as_view(), name='news'),
    path('about/', AboutView.as_view(), name='about'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('contact/', ContactView.as_view(), name='contact'),

]