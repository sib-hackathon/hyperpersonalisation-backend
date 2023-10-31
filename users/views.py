from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users.models import User, GeneralSettings
from users.serializer import UserSerializer, GeneralSettingsSerializer, UserAndGeneralSettingsSerializer

class UserAndGeneralSettingsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserAndGeneralSettingsSerializer

    def get(self, request):
        user = request.user
        general_settings = GeneralSettings.objects.get(user=user)

        serializer = UserAndGeneralSettingsSerializer({
            'user': user,
            'general_settings': general_settings
        })

        return Response(serializer.data)

    def post(self, request):
        serializer = UserAndGeneralSettingsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
