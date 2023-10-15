from rest_framework import permissions


class AccessPermission(permissions.BasePermission):
    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return request.user == obj.author
        return True
