from django.core.exceptions import PermissionDenied


class CheckDevelopPermission:
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.profile.is_developer:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CheckPlayerPermission:
    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if user.profile.is_developer:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CheckGameOwnerPermission:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.developer != self.request.user:
            raise PermissionDenied('You can delete only your games')
        return obj
