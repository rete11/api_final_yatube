from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


from posts.models import User, Comment, Post, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.

    Поля:
        - author: автор поста, только для чтения

    Мета-класс:
        - fields: все поля модели
        - model: модель Post
    """

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.

    Поля:
        - author: автор комментария, только для чтения
        - post: пост, только для чтения

    Мета-класс:
        - fields: все поля модели
        - model: модель Comment
    """

    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Group.

    Мета-класс:
        - fields: все поля модели
        - model: модель Group
    """

    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Follow.

    Поля:
        - user: пользователь, слаг поле 'username', доступные значения
        из queryset User.objects.all()
        - following: пользователь, слаг поле 'username', доступные значения
        из queryset User.objects.all()

    Мета-класс:
        - fields: все поля модели
        - model: модель Follow
        - validators: валидаторы для модели Follow

    Методы:
        - validate(data): выполняет валидацию полей user и following
    """

    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        fields = "__all__"
        model = Follow
        validators = (
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
                message=("Подписка на данного автора уже оформлена"),
            ),
        )

    def validate(self, data):
        if data["user"] == data["following"]:
            raise serializers.ValidationError(
                "Вы не можете на себя подписаться"
            )
        return data
