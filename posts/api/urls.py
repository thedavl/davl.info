from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.api import views as qv

router = DefaultRouter()
router.register(r"posts", qv.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("posts/<slug:slug>/comments/", qv.CommentListAPIView.as_view(), name="comment-list"),

    path("posts/<slug:slug>/comment/", qv.CommentCreateAPIView.as_view(), name="comment-create"),

    path("comments/<int:pk>/", qv.CommentRUDAPIView.as_view(), name="comment-detail"),

    path("comments/<int:pk>/like/", qv.CommentLikeAPIView.as_view(), name="comment-like"),
]
