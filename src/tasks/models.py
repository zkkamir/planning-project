from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from groups.models import Group


class Task(models.Model):
    """
    A class to represent a task. tasks can be placed in different groups and
    convey different meanings.
    """

    class Tags(models.IntegerChoices):
        """Choices available for task's tag field."""

        NI = 1, "Not Important"

    subject = models.CharField(_("task subject"), max_length=255)
    notes = models.TextField(_("task notes"), blank=True, null=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name="tasks",
        on_delete=models.CASCADE,
        verbose_name=_("task owner"),
    )
    slug = models.SlugField(_("task slug"))
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.CASCADE,
        verbose_name=_("task parrent"),
        blank=True,
        null=True,
    )
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    tag = models.PositiveSmallIntegerField(
        _("tag"), choices=Tags.choices, blank=True, null=True
    )
    reason = models.CharField(_("why this has to be done"), max_length=255)
    groups = models.ManyToManyField(
        Group,
        related_name="items",
        blank=True,
        verbose_name=_("groups"),
    )

    @property
    def has_children(self):
        return bool(self.children.all().count())

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject
