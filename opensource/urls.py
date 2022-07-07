from django.urls import path
from . import views

urlpatterns = [
    path('student/<st_id>', views.getStudent),
    path('all', views.getAllStudents),
    path('new', views.newStudent),
]
