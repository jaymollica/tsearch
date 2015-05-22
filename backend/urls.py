from django.conf.urls import include, url
from backend.views import GalleryView

urlpatterns = [
    url(r'^gallery$', GalleryView.as_view()),
]