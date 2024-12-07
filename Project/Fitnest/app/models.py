from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


#this class is where the user can create a post for their blogs
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    body = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

#this part where user can upload their video on their journey 
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/%y')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def str(self):
        return self.name

# Represents gym membership plans
class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


# Represents member profile, linked to a user
class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member_profile")
    phone_number = models.CharField(max_length=15)
    membership_plan = models.ForeignKey(MembershipPlan, on_delete=models.SET_NULL, null=True, blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Represents gym trainers
class TrainerProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    specialties = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Represents gym class categories
class ClassCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Represents gym classes with schedule
class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    trainer = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.schedule.strftime('%Y-%m-%d %H:%M')}" "
