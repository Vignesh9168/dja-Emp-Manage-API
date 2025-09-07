from django.shortcuts import render
from .models import Employee
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.views import APIView


from rest_framework import viewsets
from .serializers import emp_serializer
# Create your views here.
import jwt , datetime

class GetData(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = emp_serializer 

class listData(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = emp_serializer    

class loginPage(APIView):
    def post(self,request):
        uemail = request.data['email']
        upassword = request.data['password']
        a = Employee.objects.filter(email = uemail).first()

        if not a :
            raise AuthenticationFailed("The given email not in database")
        
        if upassword != a.password :
            raise AuthenticationFailed("password not matching")

        payload = {
            'user' :a.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.utcnow()

        }
        encode_jwt = jwt.encode(payload, "secret",algorithm="HS256") 
        #Send the token back in the response 

        response = Response()
        #  Set JWT in HttpOnly cookie
        response.set_cookie (
            key = 'jwt',
            value = encode_jwt,
            httponly= True   # prevents JS access
        )
        
        response.data ={
            "message":"login successfully"
        }
        return response


class list_view(APIView):
    def get(self,request):
        from_cookies = request.COOKIES.get('jwt')

        if not from_cookies:
            raise AuthenticationFailed({"msg":"go and login bcoz we used logout endpoint"}) #check login status
        try :
            payload = jwt.decode(from_cookies, "secret",algorithms="HS256")
        except jwt.ExpiredSignatureError :
            raise AuthenticationFailed("unauthorized !!!! - expired")

        user = Employee.objects.filter(id = payload['user']).first()    

        s = emp_serializer(user)

        return Response(s.data)
    

class dele(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie("jwt")

        response.data =  {
            "message": "deleted cookies"
        }    
        return response