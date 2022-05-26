from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from userdata.models import Userdata
from userdata.serializers import UserdataSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def userdata_list(request):
    # GET list of user, POST a new user, DELETE all users
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def userdata_detail(request, pk):
    # find user by pk (id)
    try: 
        userdata = Userdata.objects.get(pk=pk) 
    except Userdata.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE user
    
        
@api_view(['GET'])
def userdata_list_published(request):
    # GET all published user
