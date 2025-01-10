from django.db import models


# Create your models here.
class Todo(models.Model):
    add_todo = models.CharField(max_length=100, null=False)

    def get_absolute_url(self):
        return f"/delete/{self.id}"

