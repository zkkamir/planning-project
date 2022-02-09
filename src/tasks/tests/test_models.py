from datetime import date
import pytest
from django.utils.text import slugify


from groups.models import Group
from tasks.models import Task


@pytest.mark.parametrize(
    "kwargs",
    [
        ({"subject": "test"},),
        ({"subject": "test", "notes": "test note"},),
        (
            {
                "subject": "test",
                "notes": "test note",
                "start_date": date.today(),
            },
        ),
        (
            {
                "subject": "test",
                "notes": "test note",
                "start_date": date.today(),
                "finish_date": date.today(),
                "group": "test",
            },
        ),
    ],
)
@pytest.mark.django_db
def test_creating_task_successful(db, user, django_user_model, **kwargs):
    """
    Test the happy path of Task instance creation.
    """
    kwargs["owner"] = user
    # Not clean, try to clean up
    if "group" in kwargs:
        kwargs["group"] = Group(name=kwargs["group"], owner=user)
    task = Task.objects.create(**kwargs)

    assert task.slug == slugify(kwargs["name"])
    assert task.has_children is False
    assert task == user.tasks.get(id=task.id)
    assert task == kwargs["group"].items.get(id=task.id)
