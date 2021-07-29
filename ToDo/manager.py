from django.db import models
from django.db.models.functions import Now


class TaskOfCategoryManager(models.Manager):
    def empty_category(self):
        return self.filter(task_category=None)

    def not_empty_category(self):
        return self.exclude(task_category=None)


class DueDateManager(models.Manager):
    def get_queryset(self):
        return super(DueDateManager, self).get_queryset().filter(due_date__lt=Now())

