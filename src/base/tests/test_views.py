import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed, assertQuerysetEqual


def test_homepageview_successful(client):
    """
    Test that homepageview resolves successfully.
    """
    url = reverse("base:home")
    response = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed(response, "base/home.html")


def test_planslistview_successful(client, user):
    """
    Test that planlistview resolves successfully.
    """
    url = reverse("base:plan-list")
    client.force_login(user)
    response = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed(response, "base/plan_list.html")


@pytest.mark.django_db
def test_planslistview_secure(client, user):
    """
    Test that users can only see tasks that they have created.
    """
    user.tasks.create(subject="test", owner=user)
    user.task_groups.create(name="test", owner=user)
    url = reverse("base:plan-list")
    client.force_login(user)
    response = client.get(url)

    assertQuerysetEqual(response.context[-1]["tasks"], user.tasks.all())
    assertQuerysetEqual(response.context[-1]["groups"], user.task_groups.all())
