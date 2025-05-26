from rest_framework.views import APIView
from rest_framework import response, generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.users.serializers import UserGetMeSerializer


User = get_user_model()


class GetMeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: UserGetMeSerializer,
        },
        security=[{'Bearer': []}]
    )
    def get(self, request):
        serializer = UserGetMeSerializer(request.user)
        return response.Response(serializer.data)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetMeSerializer

    @swagger_auto_schema(
        operation_description="Create user",
        responses={
            201: UserGetMeSerializer,
            400: "User with client_code already exists."
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
