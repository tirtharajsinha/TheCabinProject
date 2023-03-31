from django.db import models

# Create your models here.


VISIBILITY = (
    ("PRIVATE", "PRIVATE"),
    ("PUBLIC", "PRIVATE")
)


class Apps(models.Model):
    id = models.BigAutoField(primary_key=True)
    appname = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    username = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="appicon")
    url = models.CharField(max_length=255)
    pinned = models.BooleanField(default=True)

    def __str__(self):
        return str(self.appname)


class Services(models.Model):
    id = models.BigAutoField(primary_key=True)
    servicename = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return str(self.servicename)


class AppOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    apporder = models.CharField(max_length=255)

    def __str__(self):
        return str(self.username)


class SystemVar(models.Model):
    id = models.BigAutoField(primary_key=True)
    var = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return str(self.var)
