from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    Render and return home template.
    """

    template_name = "base/home.html"
