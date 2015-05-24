from django.conf.urls import include, url
from frontend.views import GalleryView

urlpatterns = [
    url(r'^gallery$', GalleryView.as_view()),
]