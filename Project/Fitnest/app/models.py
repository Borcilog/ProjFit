from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


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

#It represents a gym class, likely used for managing class information and enrollment
class GymClass(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField()
    max_capacity = models.PositiveIntegerField()
    available_spots = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def spots_available(self):
        return self.available_spots

#For represents a trainer, likely used for managing trainer profiles and information.
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    specialty = models.CharField(max_length=200)  # E.g., Weight training, Yoga, etc.
    image = models.ImageField(upload_to='trainers/', null=True, blank=True)

    def __str__(self):
        return self.user.username

#A schedule for a gym class, used for managing class times and durations  
class ClassSchedule(models.Model):
    gym_class = models.ForeignKey(GymClass, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date_time = models.DateTimeField()  # Class date and time
    duration = models.DurationField()  # Duration of the class (e.g., 1 hour)

    def __str__(self):
        return f"{self.gym_class.name} - {self.date_time}"
    
#User's enrollment in a gym class, It is used for managing class registrations.
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_schedule = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.class_schedule.gym_class.name} on {self.class_schedule.date_time}"
