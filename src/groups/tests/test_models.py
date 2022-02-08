import pytest
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from groups.models import Group


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, description",
    [
        ("Test Name", "Test Description"),
        ("teST_name", "teST_description"),
        ("TEST NAME", "TEST DESCRIPTION"),
    ],
)
def test_create_group(name, description):
    """
    Test group instance creation.
    """
    user = get_user_model().objects.create_user(
        email="test@test.test", password="testtest"
    )
    group = Group.objects.create(
        name=name, description=description, owner=user
    )

    assert group.name == name
    assert group.description == description
    assert group.owner == user
    assert group.slug == slugify(name)
