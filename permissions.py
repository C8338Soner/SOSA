from rest_framework import permissions

#template
class PermissionName(permissions.BasePermission):
    message = 'Add a custom message for if the permission is not granted'

    def has_permission(self, request, view):
      return request.user.is_authenticated