from django.db import models

class company(models.Model):
	name = models.CharField(max_length=30)
	city = models.TextField()


class myuser(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    companyname = models.ForeignKey(company, on_delete=models.CASCADE)
