from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# TEMP
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # TEMP
    path("", TemplateView.as_view(template_name="_base.html"), name="home"),
    path(
        "about/",
        TemplateView.as_view(template_name="_base.html"),
        name="about",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
