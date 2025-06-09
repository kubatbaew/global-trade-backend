from rest_framework.views import APIView
from rest_framework import response, generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.users.serializers import UserGetMeSerializer, UserCreateSerializer


User = get_user_model()


class GetMeAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: UserGetMeSerializer,
        },
        security=[{'Bearer': []}]
    )
    def get(self, request, telegram_id):
        try:
            user = User.objects.get(telegram_id=telegram_id)
        except User.DoesNotExist:
            return response.Response("Error not user with telegram id")
        
        serializer = UserGetMeSerializer(user)
        return response.Response(serializer.data)



class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @swagger_auto_schema(
        operation_description="Create a new user by telegram_id and client_code.",
        responses={
            201: openapi.Response(
                description="User created successfully.",
                schema=UserCreateSerializer()
            ),
            400: openapi.Response(
                description="Validation error",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "telegram_id": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_STRING),
                            example=["User with telegramId already exists."]
                        ),
                        "client_code": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_STRING),
                            example=["User with this client already exists."]
                        ),
                    }
                )
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetMeSerializer


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return response.Response({"detail": "User deleted"}, status=200)
    

