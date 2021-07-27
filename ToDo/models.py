from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


import string
import random


class Category(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('todo:category_detail', args=[str(self.id)])

    @classmethod
    def get_first_category(cls):
        try:
            obj = cls.objects.get(name='Tasks')
            return obj

        except cls.DoesNotExist:
            values = {'name': 'Tasks'}
            obj = cls(**values)
            obj.save()
            return obj

    def __str__(self):
        return str(self.name)


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class TaskList(models.Model):
    PRIORITY_STATUS = (
        (0, 'None',),(1, 'Low',), (2, 'Medium',), (3, 'High',),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400,null= True, blank= True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=Category.get_first_category(),
        related_name='task_category')
    priority = models.IntegerField(choices=PRIORITY_STATUS, default=0)
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"), null=True, blank=True)
    due_time = models.TimeField(default=timezone.now().strftime("%H:%M"), null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('todo:task_detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super(TaskList, self).save(*args, **kwargs)