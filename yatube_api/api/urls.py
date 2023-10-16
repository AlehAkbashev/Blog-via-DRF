from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comment"
)
router.register("follow", FollowViewSet, basename="follow")
router.register("groups", GroupViewSet)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
