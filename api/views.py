import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post, Like
from .serializers import PostListSerializer, PostDetailSerializer

def update_last_request(user):
    user.last_request = datetime.datetime.now()
    user.save()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        update_last_request(self.request.user)
        return super().get_queryset()

    def get_permissions(self):
        if self.action == "destroy":
            return [IsAdminUser()]
        return super().get_permissions()

    def get_serializer_class(self):
        return PostListSerializer if self.action == "list" else PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["PUT", "GET", "POST"], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, *args, **kwargs):
        user = request.user
        publication = self.get_object()
        if publication.likes.filter(user=user):
            publication.likes.filter(user=user).first().delete()
            publication.save()
            response = {
                "number_of_likes": publication.likes.count(),
                "likes": list(publication.likes.values()),
            }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        like = Like.objects.create(user=user)
        like.save()
        publication.likes.add(like)
        publication.save()
        update_last_request(self.request.user)
        response = {
            "number_of_likes": publication.likes.count(),
            "likes": list(publication.likes.values()),
        }
        return Response(response, status=status.HTTP_200_OK)
