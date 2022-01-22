from django.urls import path
from . import views
from django.shortcuts import redirect, render
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('dashboard')),

    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('miniplayer', views.dashboard, name="dashboard"),

    path('miniplayer/getVideos', views.getVideos, name="videos"),
    path('miniplayer/video/<int:id>', views.videoPage, name="videoPage"),
    path('miniplayer/video/<int:id>/rating', views.rating, name="rating"),
    path('miniplayer/video/<int:id>/comments', views.comments, name="comments"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)