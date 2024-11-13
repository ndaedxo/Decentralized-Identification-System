# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserSession
from .serializers import UserSessionSerializer
from .services import revoke_session, revoke_all_sessions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.urls import reverse

@api_view(['GET'])
def home(request):
    urls = {
        'home': request.build_absolute_uri(reverse('sessionManager:home')),
        'session-list': request.build_absolute_uri(reverse('sessionManager:session-list')),
        'revoke-session': request.build_absolute_uri(reverse('sessionManager:revoke-session', kwargs={'session_id': 1})),  # Example ID
        'revoke-all-sessions': request.build_absolute_uri(reverse('sessionManager:revoke-all-sessions')),
    }
    return Response({
        "message": "Welcome to Session Manager!",
        "available_urls": urls,
    })


class UserSessionListView(APIView):
    """
    API to list all active sessions for a user.
    """
    def get(self, request):
        sessions = UserSession.objects.filter(user=request.user)
        serializer = UserSessionSerializer(sessions, many=True)
        return Response(serializer.data)

class RevokeSessionView(APIView):
    """
    API to revoke a specific session.
    """
    def post(self, request, session_id):
        success = revoke_session(session_id)
        if success:
            return Response({"message": "Session revoked successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Session not found."}, status=status.HTTP_404_NOT_FOUND)

class RevokeAllSessionsView(APIView):
    """
    API to revoke all sessions for the user.
    """
    def post(self, request):
        revoke_all_sessions(request.user)
        return Response({"message": "All sessions revoked successfully."}, status=status.HTTP_200_OK)
