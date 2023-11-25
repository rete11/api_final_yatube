from rest_framework import permissions


class IsAuthOrReadOnly(permissions.BasePermission):
    """
    Проверяет разрешение доступа пользователя на чтение или запись объектов.
    Методы:
    - has_permission(request, view): Проверяет, имеет ли пользователь
    разрешениена доступ к представлению.
    - has_object_permission(request, view, obj): Проверяет, имеет ли
    пользователь разрешение на доступ к конкретному объекту.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
