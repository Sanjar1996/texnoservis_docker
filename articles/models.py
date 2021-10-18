from django.db import models


class AboutModel2(models.Model):
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=250)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class HodimModel(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=250)
    images = models.ImageField(upload_to='images/', blank=True)
    twitter = models.CharField(max_length=70, blank=True)
    facebook = models.CharField(max_length=70, blank=True)
    instagram = models.CharField(max_length=70, blank=True)
    telegram = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    types = models.CharField(max_length=50)

    def __str__(self):
        return self.types


class ImagePortfolio(models.Model):
    portfolio = models.ManyToManyField("Portfolio")
    image = models.ImageField(upload_to='images')


class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    email_address = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class FAQModel(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question
