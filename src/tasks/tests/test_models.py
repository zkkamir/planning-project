from datetime import date
import pytest
from django.utils.text import slugify


from tasks.models import Task


@pytest.mark.parametrize(
    "kwargs",
    [
        {"subject": "test"},
        {"subject": "test", "notes": "test note"},
        {
            "subject": "test",
            "notes": "test note",
            "start_date": date.today(),
        },
        {
            "subject": "test",
            "notes": "test note",
            "start_date": date.today(),
            "finish_date": date.today(),
            "group": "test",
        },
    ],
)
@pytest.mark.django_db
def test_creating_task_successful(user, kwargs):
    """
    Test the happy path of Task instance creation.
    """
    kwargs["owner"] = user
    group_name = None
    # Does not seem clean, try to clean up
    if "group" in kwargs:
        group_name = kwargs.pop("group")

    task = Task.objects.create(**kwargs)
    task.save()
    # Does not seem clean, try to clean up
    if group_name:
        task.groups.create(name=group_name, owner=user)

    assert task.slug == slugify(kwargs["subject"])
    assert task.has_children is False
    assert task == user.tasks.get(id=task.id)
    # Does not seem clean, try to clean up
    if task.groups.all().count():
        if task.groups.all().count() > 1:
            for group in task.groups.all():
                assert task == group.items.get(id=task.id)
        else:
            assert task == task.groups.all()[0].items.get(id=task.id)
