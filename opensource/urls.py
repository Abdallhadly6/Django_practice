from django.urls import path
from . import views

app_name = 'opensource'

urlpatterns = [
    path('student/<st_id>', views.getStudent),
    path('all', views.getAllStudents),
    path('new', views.newStudent),
    path('edit/<st_id>', views.editStudent , name='edit'),
    path('delete/<st_id>', views.deleteStudent),
]
