from django.db import models

class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/about/', blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/category/', blank=True, null=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    country = models.CharField(max_length=200)
    day = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    content = models.TextField()
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='packages')
