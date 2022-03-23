from rest_framework import permissions

from .permissions import isStaffEditorPermission

class StaffEditorPermissionMixin():
    permissions_classes = [permissions.IsAdminUser, isStaffEditorPermission]