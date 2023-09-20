from django.db import models

# Create your models here.
class Tasks(models.Model):
    taskTittle = models.CharField(max_length=30)
    taskDescription = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTittle

