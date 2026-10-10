
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.health_checks.models import HealthCheck
from apps.products.models import Product
from apps.accounts.views import get_user_from_request
from .rules import evaluate
import json

class HealthCheckView(APIView):
    def post(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        
        data = request.data
        product = Product.objects(id=data.get('product_id'), user_id=user).first()
        if not product: return Response({'error': 'Product not found'}, status=404)
        
        responses = data.get('responses', {})
        risk, issue, rec = evaluate(product.category, responses)
        
        hc = HealthCheck(
            product_id=product,
            responses=responses,
            symptoms=data.get('symptoms', ''),
            risk_level=risk,
            potential_issue=issue,
            recommendation=rec
        )
        hc.save()
        return Response(json.loads(hc.to_json()), status=201)

class HealthReportView(APIView):
    def get(self, request, id):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        hc = HealthCheck.objects(id=id).first()
        if not hc or hc.product_id.user_id.id != user.id:
            return Response({'error': 'Not found'}, status=404)
        return Response(json.loads(hc.to_json()))
