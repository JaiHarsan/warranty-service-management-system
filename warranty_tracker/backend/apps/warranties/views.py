
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.warranties.models import Warranty
from apps.products.models import Product
from apps.accounts.views import get_user_from_request
from datetime import datetime
import json

def calculate_status(end_date):
    if not end_date: return "UNKNOWN", 0
    days_remaining = (end_date.replace(tzinfo=None) - datetime.utcnow()).days
    if days_remaining > 30: return "ACTIVE", days_remaining
    elif days_remaining >= 0: return "EXPIRING_SOON", days_remaining
    return "EXPIRED", days_remaining

class WarrantyList(APIView):
    def get(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        products = Product.objects(user_id=user)
        warranties = Warranty.objects(product_id__in=[p.id for p in products])
        res = []
        for w in warranties:
            data = json.loads(w.to_json())
            status, days = calculate_status(w.end_date)
            data['status'] = status
            data['days_remaining'] = days
            res.append(data)
        return Response(res)

    def post(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        data = request.data
        product = Product.objects(id=data.get('product_id'), user_id=user).first()
        if not product: return Response({'error': 'Product not found'}, status=404)
        w = Warranty(product_id=product, warranty_type=data.get('warranty_type'))
        if 'start_date' in data: w.start_date = datetime.fromisoformat(data['start_date'].replace('Z', ''))
        if 'end_date' in data: w.end_date = datetime.fromisoformat(data['end_date'].replace('Z', ''))
        w.save()
        return Response(json.loads(w.to_json()), status=201)
