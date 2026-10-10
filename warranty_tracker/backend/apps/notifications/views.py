
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.notifications.models import Notification
from apps.accounts.views import get_user_from_request
import json

class NotificationView(APIView):
    def get(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        notifs = Notification.objects(user_id=user).order_by('-created_at')
        return Response([json.loads(n.to_json()) for n in notifs])
        
    def put(self, request, id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        notif = Notification.objects(id=id, user_id=user).first()
        if not notif: return Response({'error': 'Not found'}, status=404)
        notif.read = True
        notif.save()
        return Response(json.loads(notif.to_json()))
        
    def delete(self, request, id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        notif = Notification.objects(id=id, user_id=user).first()
        if not notif: return Response({'error': 'Not found'}, status=404)
        notif.delete()
        return Response(status=204)
