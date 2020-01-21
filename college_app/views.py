from django.shortcuts import render
from .models import College, Student
from college_app.serializers import CollegeSerializer, StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import (CreateCollegeService, GetCollegeService, DeleteCollegeService, PutCollegeService,
                       CreateStudentService, GetStudentService, DeleteStudentService, PutStudentService)


class CollegeView(APIView):
    def post(self, request):
        data = request.data
        college_serializer = CollegeSerializer(data=request.data)

        if college_serializer.is_valid(raise_exception=True):
            CreateCollegeService.execute({'college_data': request.data})
            return Response(college_serializer.data, status=201)
        return Response(college_serializer.errors, status=400)

    def get(self, request, pk=None):
        college_gt = GetCollegeService.execute({'pk': pk})
        if pk:
            serializer = CollegeSerializer(college_gt)
        else:
            serializer = CollegeSerializer(college_gt, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        DeleteCollegeService.execute({'pk': pk})
        return Response(data={'Message': 'deleted'}, status=200)

    def put(self, request, pk):
        college_put = College.objects.get(pk=pk)
        data = request.data
        serializer = CollegeSerializer(college_put, data=request.data)
        if serializer.is_valid():
            #PutCollegeService.execute({'pk': pk})
            PutCollegeService.execute({'college_put': college_put, 'data': request.data})             # data sent to services
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):


    def post(self, request):
        data = request.data
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            CreateStudentService.execute({'student_data': request.data})

            return Response(student_serializer.data, status=201)
        return Response(student_serializer.errors, status=400)

    def get(self, request, pk=None):
        student_get = GetStudentService.execute({'pk': pk})
        if pk:
            serializer = StudentSerializer(student_get)
        else:
            serializer = StudentSerializer(student_get, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        """
        """
        student_dlt = DeleteStudentService.execute({'pk': pk})
        return Response(data={'message': 'deleted'}, status=200)

    def put(self, request, pk):
        """
        """
        student_put = Student.objects.get(pk=pk)
        data = request.data
        serializer = StudentSerializer(student_put, data=request.data)
        if serializer.is_valid():
            PutStudentService.execute({'student_put': student_put, 'data': request.data})       # data sent to services
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
