import datetime
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer


def update_last_login(user):
    user.last_login = datetime.datetime.now()
    user.save()


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = {
        TokenAuthentication,
    }
    permission_classes = {IsAuthenticated}

    def get_object(self):
        return self.request.user
