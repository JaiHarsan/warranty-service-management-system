
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.service_history.models import ServiceHistory
from apps.products.models import Product
from apps.accounts.views import get_user_from_request
import json

class ServiceHistoryView(APIView):
    def get(self, request, product_id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        p = Product.objects(id=product_id, user_id=user).first()
        if not p: return Response({'error': 'Not found'}, status=404)
        histories = ServiceHistory.objects(product_id=p)
        return Response([json.loads(h.to_json()) for h in histories])
