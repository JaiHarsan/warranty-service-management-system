
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.appointments.models import Appointment
from apps.accounts.views import get_user_from_request
import json
import random

class AppointmentView(APIView):
    def get(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        appts = Appointment.objects(user_id=user)
        return Response([json.loads(a.to_json()) for a in appts])
        
    def post(self, request):
        user = get_user_from_request(request)
        if not user: return Response({'error': 'Unauthorized'}, status=401)
        data = request.data
        appt = Appointment(
            user_id=user,
            product_id=data.get('product_id'),
            service_centre_id=data.get('service_centre_id'),
            issue=data.get('issue'),
            date=data.get('date'),
            time=data.get('time'),
            request_id=f"WS-2026-{random.randint(1000, 9999)}"
        )
        appt.save()
        return Response(json.loads(appt.to_json()), status=201)
