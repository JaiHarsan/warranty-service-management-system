
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.accounts.models import User
from django.contrib.auth.hashers import make_password, check_password
import uuid
import json

def get_user_from_request(request):
    token = request.headers.get('Authorization')
    if not token:
        return None
    token = token.replace('Bearer ', '')
    return User.objects(token=token).first()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if User.objects(email=data.get('email')).first():
            return Response({'error': 'Email already exists'}, status=400)
        password_hash = make_password(data.get('password', ''))
        user = User(name=data.get('name'), email=data.get('email'), phone=data.get('phone'), password_hash=password_hash)
        user.save()
        return Response({'message': 'User registered'}, status=201)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        user = User.objects(email=data.get('email')).first()
        if not user or not check_password(data.get('password', ''), user.password_hash):
            return Response({'error': 'Invalid credentials'}, status=401)
        user.token = str(uuid.uuid4())
        user.save()
        return Response({'token': user.token, 'name': user.name, 'email': user.email})

class MeView(APIView):
    def get(self, request):
        user = get_user_from_request(request)
        if not user:
            return Response({'error': 'Unauthorized'}, status=401)
        return Response(json.loads(user.to_json()))

class LogoutView(APIView):
    def post(self, request):
        user = get_user_from_request(request)
        if user:
            user.token = None
            user.save()
        return Response({'message': 'Logged out'})
