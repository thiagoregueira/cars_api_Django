from rest_framework import permissions


class CarOwnerPermission(permissions.BasePermission):
    """
    Permissão personalizada para permitir apenas que os proprietários de carros
    acessem suas próprias informações.

    Métodos:
    - has_permission: Verifica se o usuário tem permissão para acessar a lista de carros.
    - has_object_permission: Verifica se o usuário tem permissão para acessar um objeto específico.
    """

    def has_permission(self, request, view):
        if view.action == 'list':
            view.queryset = view.queryset.filter(owner=request.user)
            return True
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
