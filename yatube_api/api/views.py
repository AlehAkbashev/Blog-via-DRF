from rest_framework import viewsets, permissions, generics, mixins, serializers, filters
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializers
from posts.models import Post, Comment, Follow, Group, User
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from django.db import models
from .permissions import AccessPermission




def get_post(self, model: models.Model = Post, key: str = "post_id"):
    id = self.kwargs.get(key)
    return get_object_or_404(model, pk=id)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AccessPermission, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AccessPermission, permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        post = get_post(self)
        serializer.save(post=post, author=self.request.user)

    def perform_update(self, serializer):
        post = get_post(self)
        serializer.save(post=post, author=self.request.user)

    def get_queryset(self):
        post = get_post(self)
        return post.comments.all()


class FollowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def perform_create(self, serializer):
        following_name = self.request.data.get('following')
        following_user = get_object_or_404(User, username=following_name)
        if following_user == self.request.user:
            raise serializers.ValidationError({'error': 'Нельзя подписаться на самого себя'})
        serializer.save(user=self.request.user, following=following_user)

    def get_queryset(self):
        user = self.request.user
        return user.following.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

