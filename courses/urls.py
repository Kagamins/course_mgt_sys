from django.conf.urls import patterns, url
from courses import views

urlpatterns = [
    url(r'^course/create$', views.CourseCreate.as_view(), name='course_create'),

]
