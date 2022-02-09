import pytest


@pytest.mark.django_db
def test_create_user(django_user_model):
    """
    Test user creation.
    """
    user = django_user_model.objects.create_user(
        email="test@test.test", password="testtest"
    )
    assert django_user_model.objects.count() == 1
    assert user.email == "test@test.test"
    assert user.is_active is True
    assert user.is_staff is False
    assert user.is_superuser is False
    with pytest.raises(AttributeError):
        user.username
    with pytest.raises(TypeError):
        django_user_model.objects.create_user()
    with pytest.raises(TypeError):
        django_user_model.objects.create_user(email="")
    with pytest.raises(ValueError):
        django_user_model.objects.create_user(email="", password="foo")


@pytest.mark.django_db
def test_create_superuser(django_user_model):
    """
    Test superuser creation.
    """
    user = django_user_model.objects.create_superuser(
        email="supertest@test.test", password="testtest"
    )
    assert django_user_model.objects.count() == 1
    assert user.email == "supertest@test.test"
    assert user.is_active is True
    assert user.is_staff is True
    assert user.is_superuser is True
    with pytest.raises(AttributeError):
        user.username
    with pytest.raises(ValueError):
        django_user_model.objects.create_superuser(
            email="supertest@test.test", password="foo", is_superuser=False
        )
