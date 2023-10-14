from rest_framework.permissions import BasePermission


class AccessPermission(BasePermission):
    message = 'У вас недостаточно прав для выполнения данного действия.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
