from django.db import models
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]
class Task(models.Model):
    description = models.CharField(max_length=1500, null=False, blank=False, verbose_name='Task Description')
    details = models.CharField(max_length=3000, null=False, verbose_name='Task Details')
    status = models.CharField(max_length=11, choices=status_choices, verbose_name='Choice')
    completion_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):

        return "{}. {}".format(self.pk, self.description)