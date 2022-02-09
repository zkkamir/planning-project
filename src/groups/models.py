from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    """
    A class to represent a group of tasks.
    """

    name = models.CharField(_("group name"), max_length=127)
    description = models.TextField(_("group description"))
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name=_("owner")
    )
    slug = models.SlugField(_("group slug"))

    class Meta:
        unique_together = (
            "name",
            "owner",
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
