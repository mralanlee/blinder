from rest_framework import generics
from rest_framework.response import Response
from users.serializers import RegisterSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class WelcomeView(generics.GenericAPIView):

    def get(self,request,*args,**kwargs):
        return Response({'hello':'world'})

register = RegisterAPIView.as_view()
hello = WelcomeView.as_view()