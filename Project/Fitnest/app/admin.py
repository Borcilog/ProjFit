from django.contrib import admin
from .models import Post, Video, Contact, GymClass, Trainer, ClassSchedule, Enrollment

admin.site.register(Post)

admin.site.register(Video)

admin.site.register(Contact)

class GymClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_capacity', 'available_spots')
    search_fields = ('name',)

admin.site.register(GymClass, GymClassAdmin)

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'bio')
    search_fields = ('user__username', 'specialty')

admin.site.register(Trainer, TrainerAdmin)

class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('gym_class', 'trainer', 'date_time', 'duration')
    search_fields = ('gym_class__name', 'trainer__user__username')
    list_filter = ('trainer',)

admin.site.register(ClassSchedule, ClassScheduleAdmin)

class ClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_schedule', 'enrollment_date')
    search_fields = ('user__username', 'class_schedule__gym_class__name')

admin.site.register(Enrollment, ClassEnrollmentAdmin)