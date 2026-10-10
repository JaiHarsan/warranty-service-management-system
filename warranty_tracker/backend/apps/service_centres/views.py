
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.service_centres.models import ServiceCentre
import json

class ServiceCentreList(APIView):
    def get(self, request):
        city = request.query_params.get('city')
        brand = request.query_params.get('brand')
        query = {}
        if city: query['city__icontains'] = city
        if brand: query['brand__icontains'] = brand
        scs = ServiceCentre.objects(**query)
        return Response([json.loads(s.to_json()) for s in scs])
