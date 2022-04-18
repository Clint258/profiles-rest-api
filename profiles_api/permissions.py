from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit thier own profile"""

    def has_object_perssion(self, request, view, obj):
        """"Check if user is trying to edit their own profile"""
        if request.method in permission.SAFE_METHODS:
            return True

        return obj.id == request.user.id
