import os
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from .serializers import EducationSerializer,JuniorCertTestSerializer,ExperienceSerializer,ReferenceSerializer,CvSerializer, SkillSerializer,QualitiesSerializer, LeavingCertTestSerializer, StudentSerializer
from .models import CV,Education,JuniorCertTest,Experience,Reference,JobTitle,Qualities,Skills,LeavingCertTest
from users.models import Student
from django.template.loader import render_to_string
from weasyprint import HTML
from rest_framework.exceptions import  ValidationError
from rest_framework import status
from rest_framework.response import Response


class CvViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CvSerializer
    lookup_field = 'id'

    # def get_object(self,id):
    #     try:
    #         queryset=Student.objects.get(id=self.request.user.student.id)
    #         return queryset
    #     except Exception as e:
    #         raise ValidationError(e)
        
    # def get(self, request):
    #     user=Student.objects.get(id=self.request.user.student.id)
    #     test = self.get_object(user.id)
    #     serializer = StudentSerializer(test)
    #     return Response(serializer.data, status.HTTP_200_OK)
    def get(self, request):
        """Fetch All Chocies"""
        try:
            cv=CV.objects.all()
            serializer = CvSerializer(cv, many=True)
            return Response(serializer.data)
    
        except Exception as e:
           return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class CVUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CvSerializer
    queryset = CV.objects.all()


class EducationViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class EducationViewUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

class JuniorCertTestViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JuniorCertTestSerializer

    def create(self, request, *args, **kwargs):
        try:
            many = isinstance(request.data, list)
            serializer = self.get_serializer(data=request.data, many=many)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, headers=headers)
        except Exception as e:
            raise e
class JuniorViewUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JuniorCertTestSerializer
    queryset = JuniorCertTest.objects.all()

class LeavingCertTestViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LeavingCertTestSerializer

    def create(self, request, *args, **kwargs):
        try:
            many = isinstance(request.data, list)
            serializer = self.get_serializer(data=request.data, many=many)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, headers=headers)
        except Exception as e:
            raise e

class LeavingViewUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LeavingCertTestSerializer
    queryset = LeavingCertTest.objects.all()

class ExperienceViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExperienceSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class ExperienceViewUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class ReferenceViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReferenceSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class ReferenceViewUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReferenceSerializer
    queryset = Reference.objects.all()


class SkillsViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class SkillsUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer
    queryset = Skills.objects.all()


class QualityViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QualitiesSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

class QualityUpdate(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QualitiesSerializer
    queryset = Qualities.objects.all()


class GeneratePDF(CreateAPIView):
    def get(self, request):
        """Fetch All Notes By Officer"""
        try:

          student =self.request.user
          user_obj=Student.objects.get(id=student.id)
          cv_obj =CV.objects.get(user=student.id)
          education_obj=Education.objects.get(user=student.id)
          junior_cert_obj=JuniorCertTest.objects.get(user=student.id)
          leave_cert_obj=LeavingCertTest.objects.get(user=student.id)
          exp_obj=Experience.objects.get(user=student.id)
          skill_obj=Skills.objects.get(user=student.id)
          quality_obj=Qualities.objects.get(user=student.id)
          refer_obj=Reference.objects.get(cv=cv_obj.id)
          temp_name = "general/templates/" 
          cv_template = str(user_obj.first_name) +"-"+str(user_obj.last_name) +"-"+"cv" + ".html"
          open(temp_name + cv_template, "w").write(render_to_string('cv.html', {'student_detail': user_obj,'cv_detail':cv_obj,'education_detail':education_obj,'Junior_Cert_detail':junior_cert_obj,'Leave_Cert_detail':leave_cert_obj,'skill_detail':skill_obj,'qualities_detail':quality_obj,'Experience_detail':exp_obj,'Reference_detail':refer_obj}))
          HTML(temp_name + cv_template).write_pdf(str(user_obj.first_name)+'.pdf')
          file_location = f'{user_obj.first_name}.pdf'
          with open(file_location, 'rb') as f:
            file_data = f.read()
          response = HttpResponse(file_data, content_type='application/pdf')
          response['Content-Disposition'] = 'attachment; filename="'+ user_obj.first_name +'".pdf'
          return response
        except Exception as e:
          return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
