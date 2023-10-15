from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet)
router.register("follow", FollowViewSet)
router.register("groups", GroupViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
