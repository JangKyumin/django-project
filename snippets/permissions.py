from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS 이 세가지 메소드만 넘겨준다.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
