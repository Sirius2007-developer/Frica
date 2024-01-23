from django.db import models
from django.urls import reverse
# Create your models here.
class B_cake(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("birthdaydetail", args=[self.slug])

    def __str__(self):
        return self.name


class Custom(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("customdetail", args=[self.slug])

    def __str__(self):
        return self.name

class Wedding(models.Model):
    name = models.CharField(max_length=250)
    cost = models.IntegerField()
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("weddingdetail", args=[self.slug])

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    full_info = models.TextField()
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("categorydetail", args=[self.slug])

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    img = models.ImageField(upload_to='team/img')
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("teamdetail", args=[self.slug])

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='testimonial/img')
    job = models.CharField(max_length=50)
    comment = models.TextField()
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse("testimonialdetail", args=[self.slug])

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name