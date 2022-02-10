from django.urls import path

from . import views


app_name = "base"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("planlist/", views.PlanListView.as_view(), name="plan-list"),
]
