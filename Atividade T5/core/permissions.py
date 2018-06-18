from rest_framework import permissions

class OnlySafeMethods(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

class OnlyOwnerCanDoIt(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user==obj.owner:
            return True
        elif request.method=='GET':
            return True
        return False

class OnlyOwnerCanDestroyComments(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.post_id.owner==request.user:
            return True
        return False

