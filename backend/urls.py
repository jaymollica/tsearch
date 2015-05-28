from django.conf.urls import include, url
from backend.views import GalleryView, HomeView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^gallery$', GalleryView.as_view()),
    url(r'^home$', HomeView.as_view())
]