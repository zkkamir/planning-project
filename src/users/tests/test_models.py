import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    """
    Test user creation.
    """
    user = User.objects.create_user(
        email="test@test.test", password="testtest"
    )
    assert User.objects.count() == 1
    assert user.email == "test@test.test"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False
    with pytest.raises(AttributeError):
        user.username
    with pytest.raises(TypeError):
        User.objects.create_user()
    with pytest.raises(TypeError):
        User.objects.create_user(email="")
    with pytest.raises(ValueError):
        User.objects.create_user(email="", password="foo")


@pytest.mark.django_db
def test_create_superuser():
    """
    Test superuser creation.
    """
    user = User.objects.create_superuser(
        email="supertest@test.test", password="testtest"
    )
    assert User.objects.count() == 1
    assert user.email == "supertest@test.test"
    assert user.is_active is True
    assert user.is_staff is True
    assert user.is_superuser is True
    with pytest.raises(AttributeError):
        user.username
    with pytest.raises(ValueError):
        User.objects.create_superuser(
            email="supertest@test.test", password="foo", is_superuser=False
        )
