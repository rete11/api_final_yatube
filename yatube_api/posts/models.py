from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель группы"""
    title = models.CharField(verbose_name="Название", max_length=200)
    slug = models.SlugField(verbose_name="Слаг группы", unique=True)
    description = models.TextField(verbose_name="Описание группы")


class Post(models.Model):
    """Модель поста"""
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор поста",
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="posts/",
        null=True,
        blank=True,
    )
    group = models.ForeignKey(
        Group,
        verbose_name="Группа",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="posts"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("id",)

    def __str__(self):
        return self.text


class Follow(models.Model):
    """Модель подписок"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор записей'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_follow'),)

    def __str__(self):
        return f'{self.user}'


class Comment(models.Model):
    """Модель комментария"""
    author = models.ForeignKey(
        User,
        verbose_name="Автор комментария",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post, verbose_name='Пост', on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('id',)

    def __str__(self):
        return self.text
