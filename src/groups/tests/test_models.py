import pytest
from django.contrib.auth import get_user_model

from groups.models import Group


@pytest.mark.django_db
def test_create_group():
    """
    Test group instance creation.
    """
    user = get_user_model.objects.create_user(
        email="test@test.test", password="testtest"
    )
    group = Group.objects.create(
        name="test name", description="test description", owner=user
    )

    assert group.name == "test name"
    assert group.description == "test description"
    assert group.user == user
    assert group.slug == "test-name"
