from django.db import models

class Task(models.Model):
    title = models.CharField("Поле1", max_length=50)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title
