from django.urls import path

from .views import AboutPageView, HomePageView, LinkPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('link/', LinkPageView.as_view(), name='link')
]
