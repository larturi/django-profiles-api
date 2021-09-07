from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Permite a un usuario editar su perfil """

    def has_object_permission(self, request, view, obj):
        """ Chequea si un usuario esta intentando editar su propio perfil"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ Permite actualizar el propio StatusFeed """

    def has_object_permission(self, request, view, obj):
        """ Chequea si un usuario esta intentando editar su propio feed"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile_id == request.user.id
