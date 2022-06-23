from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254)


    def __str__(self):
        return self.name

    def create_company(self):
        self.save()

    def delete_company(self):
        self.delete()

    @classmethod
    def find_company(cls, search_term):
        companies = cls.objects.filter(business_name__icontains=search_term)
        return companies

    def update_company(self):
        name = self.name
        self.name = name
        self.save()
     # get all images

    @classmethod
    def get_all_images(cls):
        images = Company.objects.all()
        return images


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', blank=True)
    # created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.created.strftime('%d-%m-%Y')}"
    def __str__(self):
        return f"{self.user.username} profile"


class Nanny(models.Model):
    profile_pic = models.ImageField(
        upload_to='profilepic/', default='default.jpeg')
    name = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=50, blank=True)
    rates = models.IntegerField(blank=True)
    availability = models.BooleanField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    about = models.TextField(default="Some String")
    skills = models.TextField(default="Some String")
    company=models.ForeignKey(Company, on_delete=models.CASCADE ,default=1)


    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name

    def get_image_by_id(cls):
        images = cls.objects.get(pk=id)
        return images


class Bio(models.Model):
    about = models.TextField()
    skills = models.TextField()
