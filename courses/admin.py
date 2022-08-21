from django.contrib import admin

from courses.models import User, Category, Course, Lesson

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
