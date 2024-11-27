from django.urls import path
from .views import (HomePageView, AboutPageView, BlogListView, 
                    BlogDetailView, BlogCreateView, BlogUpdateView,
                    BlogDeleteView,ContactPageView, register, login_view, logout_view)
from . import views

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('register/', register, name='register'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('Video/Upload', views.upload_video, name='Video'),
    path('Videos/',views.video_list, name='Video_list'),
    path('Contact/', ContactPageView.as_view(), name='Contact'),
    path('class_schedule/', views.class_schedule, name='class_schedule'),
    path('class_enroll/<int:schedule_id>/', views.class_enroll, name='class_enroll'),
   
]
