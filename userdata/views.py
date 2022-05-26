from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from userdata.models import Userdata
from userdata.serializers import UserdataSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def userdata_list(request):
    if request.method == 'GET':
        userdata = Userdata.objects.all()
        
        username = request.GET.get('username', None)
        if username is not None:
            userdata = userdata.filter(title__icontains=username)
        
        userdata_serializer = UserdataSerializer(userdata, many=True)
        return JsonResponse(userdata_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        userdata_data = JSONParser().parse(request)
        userdata_serializer = UserdataSerializer(data=userdata_data)
        if userdata_serializer.is_valid():
            userdata_serializer.save()
            return JsonResponse(userdata_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(userdata_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Userdata.objects.all().delete()
        return JsonResponse({'message': '{} User(s) were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userdata_detail(request, pk):
    try: 
        userdata = Userdata.objects.get(pk=pk) 
    except Userdata.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        userdata_serializer = UserdataSerializer(userdata) 
        return JsonResponse(userdata_serializer.data) 
 
    elif request.method == 'PUT': 
        userdata_data = JSONParser().parse(request) 
        userdata_serializer = UserdataSerializer(userdata, data=userdata_data) 
        if userdata_serializer.is_valid(): 
            userdata_serializer.save() 
            return JsonResponse(userdata_serializer.data) 
        return JsonResponse(userdata_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        serdata.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def userdata_list_published(request):
    userdata = Userdata.objects.filter(published=True)
        
    if request.method == 'GET': 
        userdata_serializer = UserdataSerializer(userdata, many=True)
        return JsonResponse(userdata_serializer.data, safe=False)
    
