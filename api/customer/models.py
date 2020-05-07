from django.db import models

# Create your models here.
class Hobbies(models.Model):
    hobiesId = models.IntegerField()
    hobiesName = models.CharField(max_length=255)

class Skill(models.Model):
    skillId = models.IntegerField()
    skillName = models.CharField(max_length=255)
    level = models.IntegerField()
     
class Profile(models.Model):
    # userId = models.IntegerField()
    name = models.CharField(max_length=255)
    img = models.ImageField()
    dob = models.DateTimeField()
    gender = models.IntegerField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    github = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    hobbies = models.ForeignKey(Hobbies,blank=True,related_name='hobbies',on_delete=models.CASCADE)

    class Meta:
        unique_together = ['email','hobbies']
        # ordering = ['userId']

