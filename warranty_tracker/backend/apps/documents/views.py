
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.documents.models import DocumentItem
from apps.accounts.views import get_user_from_request
import json

class DocumentView(APIView):
    def get(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        docs = DocumentItem.objects(user_id=user)
        return Response([json.loads(d.to_json()) for d in docs])
