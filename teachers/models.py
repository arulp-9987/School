from django.db import models


class Teacher(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    subject = models.CharField(max_length=100)

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    joining_date = models.DateField()

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name
