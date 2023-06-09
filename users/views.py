from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .models import User,Student, School
from .serializers import SignupUserSerializer,UserSerializer,SchoolSerializer, StudentSignUpSerializer, UserSignUpSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.db import transaction
from common.response_template import get_response_template


class SignupUser(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            user_serializer_obj  = UserSignUpSerializer(data=request.data)
            user_serializer_obj.is_valid(raise_exception=True)
            user_obj = user_serializer_obj.save()
            request.data["user"] = user_obj.pk
            student_serializer_obj = StudentSignUpSerializer(data=request.data)
            student_serializer_obj.is_valid(raise_exception=True)
            student_serializer_obj.save()
            response_template = get_response_template()
            response_template['data'] = student_serializer_obj.data
            return Response(data=response_template)


class UserView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        try:
            queryset=Student.objects.get(id=self.request.user.student.id)
            return queryset
        except Exception as e:
            raise ValidationError(e)


class SchoolView(CreateAPIView):
    permission_classes=[]
    serializer_class = SchoolSerializer

    def get(self, request):
        """Fetch All Tests By User"""
        try:
            schools=School.objects.all()
            serializer = SchoolSerializer(schools, many=True)
            return Response({'data':serializer.data, 'success':True})
    
        except Exception as e:
           return Response({'message': str(e)},success=False, status=status.HTTP_400_BAD_REQUEST)
        

from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError, NotFound
import random


class SendPasswordResetOTPView(APIView):
    permission_classes = []

    def send_otp_email(self,otp,email):
        try:
            send_mail(
                'Your Password Reset OTP',
                f'Your password reset otp is {otp}',
                'hassan.shahzad@zweidevs.com',
                [email])
        except:
            pass

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email is None:
            raise ValidationError("No email is there")
        student_obj = Student.objects.filter(user__email=email).first()
        if not (student_obj is None):
            student_obj.otp = str(random.randint(1000,9999))
            student_obj.otp_verified = False
            student_obj.save()
            self.send_otp_email(student_obj.otp,email)
        respone_template = get_response_template()
        respone_template['data'] = "An Email has been sent to your account."
        return Response(respone_template)


class OTPConfirmationAPIView(APIView):
    permission_classes = []

    def post(self,request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if email is None:
            raise ValidationError("email is required")
        if otp is None:
            raise ValidationError("email is required")
        student_obj = Student.objects.filter(user__email=email).first()
        if student_obj is None:
            raise NotFound("No studnet with this email found")
        response_template = get_response_template()
        if otp == student_obj.otp:
            student_obj.otp_verified = True
            student_obj.save()
            response_template['data'] = "OTP verfication succeeded"
            return Response(response_template)
        raise ValidationError("Incorrect OTP")


class ResetPasswordAPIView(APIView):
    permission_classes = []

    def patch(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        student_obj = Student.objects.filter(user__email=email).first()
        if email is None:
            raise ValidationError("email is required")
        if student_obj is None:
            raise NotFound("No studnet with this email found")
        if student_obj.otp_verified:
            student_obj.user.set_password(password)
            student_obj.user.save()
            student_obj.otp_verified = False
            student_obj.save()
            response_template = get_response_template()
            response_template['data'] = "Password reset successfully."
            return Response(response_template)
        raise ValidationError("OTP is not verified yet")
