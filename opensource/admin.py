from django.contrib import admin
from .models import Track,Student
# Register your models here.

class CustomStudent (admin.ModelAdmin):
    fieldsets = (
			["Student Information" , {"fields" : ["fname","lname","age"]}],
			["Scholarship Information" , {"fields" : ["student_track"]}] )
    list_display = ('fname' , 'lname' , 'age' , 'student_track' , 'is_graduated')
class InlineStudent (admin.StackedInline):
    model = Student
    extra = 2

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

admin.site.register(Track , CustomTrack)
admin.site.register(Student , CustomStudent)