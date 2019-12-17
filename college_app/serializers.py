from .models import College, Student
from rest_framework import serializers


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    # college = CollegeSerializer()

    class Meta:
        model = Student
        fields = '__all__'
