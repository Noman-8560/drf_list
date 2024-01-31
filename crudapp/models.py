from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    fname = models.CharField(max_length=100, null=True)
    cnic = models.IntegerField(max_length=100, null=True)
    serial = models.IntegerField(max_length=100, null=True)
    fno = models.IntegerField(max_length=100,  null=True)

    def __str__(self):
        return str(self.id)
