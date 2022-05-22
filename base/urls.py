from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from .feeds import LatestEntriesFeed
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.aboutPage, name="about"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("settings/", views.globalSettings, name="global-settings"),
    # path('rss/index.rss', LatestEntriesFeed()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
