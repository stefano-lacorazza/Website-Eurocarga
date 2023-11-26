from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("team/", views.team, name="team"),
    path("services/", views.services, name="services"),
    path("pqrs/", views.pqrs, name="pqrs"),
    path("tracking/", views.tracking, name="tracking"),
    path("offices/", views.offices, name="offices"),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()