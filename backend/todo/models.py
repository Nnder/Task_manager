from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name='Выполнена?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, related_name='todo', on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Планировщик задач'
        verbose_name_plural = 'Планировщик задач'
