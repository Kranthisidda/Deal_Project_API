from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    fmv = models.DecimalField(max_digits=10, decimal_places=2)
    tax_credit_transfer_rate = models.DecimalField(max_digits=5, decimal_places=4)
    tax_credit_transfer_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Deal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    projects = models.ManyToManyField(Project)
    tax_credit_transfer_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
