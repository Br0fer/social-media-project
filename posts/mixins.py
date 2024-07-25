from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from posts.models import Post


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_by != request.user.profile:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ObjectExistMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user.profile
        liked_post = get_object_or_404(Post, pk=kwargs.get("pk"))

        try:
            checked_like = user.likes.get(post=liked_post)

            if checked_like:
                raise PermissionDenied

        except ObjectDoesNotExist:
            pass

        return super().dispatch(request, *args, **kwargs)
