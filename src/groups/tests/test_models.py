import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError
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
def test_create_group_is_successful(name, description):
    """
    Test the happy path Group instance creation.
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


@pytest.mark.django_db
def test_creating_duplicate_group_fails():
    """
    Test Groups cannot be created with the same name.
    """
    user = get_user_model().objects.create_user(
        email="test@test.test", password="testtest"
    )
    group1 = Group.objects.create(  # noqa
        name="test", description="test1", owner=user
    )
    with pytest.raises(IntegrityError):
        group2 = Group.objects.create(  # noqa
            name="test", description="test2", owner=user
        )
