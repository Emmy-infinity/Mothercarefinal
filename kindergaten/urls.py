from django.urls import path
from. import views
from .urls import path

app_name='kindergaten'

urlpatterns = [

    path('', views.home, name='home'),
    path('about/',views.about ,name='about' ),
    path('teacher/',views.teacher, name='teacher'),
    path('course/',views.course, name='course'),
    path('pricing/', views.price,name='pricing'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact, name='contact')
    


]