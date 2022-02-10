from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_homepageview_successful(client):
    """
    Test that homepageview resolves successfully.
    """
    url = reverse("base:home")
    respone = client.get(url)

    assert respone.status_code == 200
    assertTemplateUsed(respone, "base/home.html")
