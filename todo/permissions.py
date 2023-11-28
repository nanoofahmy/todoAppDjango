from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print(f'id_todo: {view.action}')
        # Allow anyone to view todos and comments
        if view.action in ['list', 'retrieve']:
            return True
        # Allow any user to add comments to any ttodoo
        elif view.action == 'create':
            return True
        # Only allow the owner to edit or delete their own todos and comments
        elif view.action in ['update', 'partial_update', 'destroy']:
            print(f'update: {self.is_owner(request, view)}')
            return self.is_owner(request, view)

        return False

    def is_owner(self, request, view):
        # Check if the user is the owner of the tttodoo , commmment
        print(f'id_tnnnodo: {view.action}')
        if view.action == 'update' or view.action == 'partial_update':
            print(f'update2: {view.action}')
            obj = view.get_object()
        elif view.action == 'destroy':
            obj = view.get_object()
        else:
            return False

        return obj.user == request.user