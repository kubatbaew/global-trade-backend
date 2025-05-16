from rest_framework.views import APIView
from rest_framework import response
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.users.serializers import UserGetMeSerializer


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
