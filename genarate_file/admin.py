from django.contrib import admin
from .models import FileCSVModel
from django_celery_results.admin import TaskResult


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    """Admin-interface for results of tasks."""

    model = TaskResult
    list_display = ['task_id', 'task_name', 'date_done',
                    'status', 'worker', 'task_args']
    list_filter = ('status', 'date_done', 'periodic_task_name', 'task_name',
                   'worker')


admin.site.unregister(TaskResult)
admin.site.register(TaskResult, TaskAdmin)
admin.site.register(FileCSVModel)
