from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

# @api_view(['GET', 'POST'])
# def student_list(request):
#     if request.method == 'GET':
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view([ 'GET','POST'])
@permission_classes([IsAuthenticated])
def student_detail(request):
    print(
        'User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        students = Student.objects.filter(user_id=request.user.id)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)



# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk):
#     student = get_object_or_404(student, pk=pk)
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def student_list(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'POST', 'PUT','DELETE'])
# @permission_classes([IsAuthenticated])
# def student_detail(request):
#     print(
#         'User ', f"{request.user.id} {request.user.email} {request.user.username}")
#     if request.method =='POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         students = Student.objects.filter(user_id=request.user.id)
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(students, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         students.delete()
#         return Response(status.HTTP_204_NO_CONTENT)
