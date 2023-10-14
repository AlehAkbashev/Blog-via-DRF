from rest_framework import viewsets, permissions, generics, mixins
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializers
from posts.models import Post, Comment, Follow, Group, User
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from django.db import models



def get_post(self, model: models.Model = Post, key: str = "post_id"):
    id = self.kwargs.get(key)
    return get_object_or_404(model, pk=id)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_post(self)
        serializer.save(post=post, author=self.request.user)

    def perform_update(self, serializer):
        post = get_post(self)
        serializer.save(post=post, author=self.request.user)

    

class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        following_name = self.request.data.get('following')
        following_user = get_object_or_404(User, username=following_name)
        serializer.save(user=self.request.user, following=following_user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers

