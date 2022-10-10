from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Publication(models.Model):
    STATUS_CHOICES = (
        ('open', 'Октрытая'),
        ('close', 'Закрытая'),
        ('draft', 'Черновик')
    )
    """
    классы которые наследуются от models.Model являются моделями - представление таблицы в БД
    """

    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='pubs', null = True) # в бд хранится NULL
    text = models.TextField(blank=True) # blank  поле становиться необязательным к заполнению, но в БД хранит пустую
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='publications')
    #User.publocations.all()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self) -> str:
        return f'{self.title}'




class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,
    related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    create_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-create_at'] # сортеровка по убыванию, по указанным полям 










