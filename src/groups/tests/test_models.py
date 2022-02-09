import pytest
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
def test_create_group_is_successful(name, description, user):
    """
    Test the happy path Group instance creation.
    """
    group = Group.objects.create(
        name=name, description=description, owner=user
    )

    assert group.name == name
    assert group.description == description
    assert group.owner == user
    assert group.slug == slugify(name)


@pytest.mark.django_db
def test_creating_duplicate_group_fails(user):
    """
    Test same user cannot create Groups with the same name.
    """
    group1 = Group.objects.create(  # noqa
        name="test", description="test1", owner=user
    )
    with pytest.raises(IntegrityError):
        group2 = Group.objects.create(  # noqa
            name="test", description="test2", owner=user
        )


@pytest.mark.django_db
def test_different_users_can_create_same_group(create_user):
    """
    Test two different users can have groups with the same name.
    """
    user1 = create_user(email="user1@test.test")
    user2 = create_user(email="user2@test.test")
    user1_group = Group.objects.create(
        name="test", description="test", owner=user1
    )
    user2_group = Group.objects.create(
        name="test", description="test", owner=user2
    )
    assert user1_group.name == user2_group.name
