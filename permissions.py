from rest_framework import permissions

#template
class PermissionName(permissions.BasePermission):
    message = 'Add a custom message for if the permission is not granted'

    def has_permission(self, request, view):
      return request.user.is_authenticated

class IsAddedByUser(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    return bool(obj.user == request.user or request.user.is_staff)