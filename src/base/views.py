from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from groups.models import Group
from tasks.models import Task


class HomePageView(TemplateView):
    """
    Render and return home template.
    """

    template_name = "base/home.html"


class PlanListView(LoginRequiredMixin, ListView):
    """
    The main user dashboard.
    """

    template_name = "base/plan_list.html"
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_groups = Group.objects.filter(owner=self.request.user)
        context.update({"groups": user_groups})
        return context

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
