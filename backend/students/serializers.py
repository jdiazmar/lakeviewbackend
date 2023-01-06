from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'grade', 'school', 'age', 'email', 'phone_number', 'user_id']
        depth = 1