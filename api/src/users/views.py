from rest_framework import generics

from users.serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


register = RegisterAPIView.as_view()
