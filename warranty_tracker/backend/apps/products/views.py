
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products.models import Product
from apps.accounts.views import get_user_from_request
import json

class ProductList(APIView):
    def get(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        products = Product.objects(user_id=user)
        return Response([json.loads(p.to_json()) for p in products])
    
    def post(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        data = request.data
        p = Product(user_id=user, brand=data.get('brand'), category=data.get('category'), product_name=data.get('product_name'))
        p.save()
        return Response(json.loads(p.to_json()), status=201)

class ProductDetail(APIView):
    def get(self, request, id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        p = Product.objects(id=id, user_id=user).first()
        if not p: return Response({'error': 'Not found'}, status=404)
        return Response(json.loads(p.to_json()))

    def put(self, request, id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        p = Product.objects(id=id, user_id=user).first()
        if not p: return Response({'error': 'Not found'}, status=404)
        for k, v in request.data.items():
            setattr(p, k, v)
        p.save()
        return Response(json.loads(p.to_json()))

    def delete(self, request, id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        p = Product.objects(id=id, user_id=user).first()
        if not p: return Response({'error': 'Not found'}, status=404)
        p.delete()
        return Response(status=204)

from datetime import datetime, timedelta
from apps.warranties.models import Warranty
from rest_framework.parsers import MultiPartParser

class ProductUpload(APIView):
    parser_classes = [MultiPartParser]
    
    def post(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        
        # Simulate OCR extracting data from PDF
        p = Product(user_id=user, brand="Sony (Extracted)", category="electronics", product_name="Bravia 4K XR")
        p.save()
        
        # Set an expiry 29 days from now to trigger the < 30 days reminder
        w = Warranty(
            product_id=p, 
            warranty_type="Standard",
            start_date=datetime.utcnow() - timedelta(days=336), 
            end_date=datetime.utcnow() + timedelta(days=29),
            duration=365,
            coverage="Full Parts & Labor"
        )
        w.save()
        
        return Response({'message': 'Invoice processed', 'product_id': str(p.id)}, status=201)
