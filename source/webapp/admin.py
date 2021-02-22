from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):

    list_display = ['id', 'status', 'created_at']

    list_filter = ['status']

    search_fields = ['status', 'completion_date']

    fields = ['description', 'status', 'completion_date', 'created_at', 'updated_at']

    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Task, TaskAdmin)