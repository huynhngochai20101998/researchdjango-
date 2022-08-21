from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import User, Category, Course, Lesson


class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "created_at", "activate", "courses"]
    search_fields = ["subject", "created_at", "courses__subject"]
    readonly_fields = ["avatar"]

    def avatar(self, lesson):
        if lesson:
            return mark_safe(
                '<img src="/static/{url}" alt ={alt} />'.format(url=lesson.image.name, alt=lesson.subject)
            )


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
