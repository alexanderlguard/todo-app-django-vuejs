from django.db import models

# Groups
class Group(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

# Tasks
class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True)
    state = models.BooleanField(default=False)
    tag = models.CharField(max_length=30)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="tasks")