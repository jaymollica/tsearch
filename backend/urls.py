from django.conf.urls import include, url
from backend.views import GalleryView, HomeView

urlpatterns = [
    url(r'^gallery$', GalleryView.as_view()),
    url(r'^home$', HomeView.as_view())
]