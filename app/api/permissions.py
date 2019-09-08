from rest_framework import permissions

class IsAPIAuthorized(permissions.BasePermission):
    """
    Custom rest_framework permission to check Django custom permision.
    This will allow user management via Django Admin
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='is_api_authorized').exists()