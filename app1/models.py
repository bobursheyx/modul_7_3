from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=30)

    class Meta:
        db_table = 'data'

    def __str__(self):
        return f"{self.name} {self.id}"