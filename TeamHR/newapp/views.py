from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from newapp.models import  wallet
from newapp.serializers import walletserializer
import requests,json
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from newapp.forms import UserForm
import os
import requests
from requests.auth import HTTPBasicAuth
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'team_hr.html')
def storeuser(request):
    return render(request,'store.html')
def transferuser(request):
    return render(request,'transfer.html')
def loaduser(request):
    return render(request,'load.html')


def createUser(request):
    try:
        wallet_id = request.GET['id']
        user_name = request.GET['name']
        money = request.GET['money']
        url = "http://127.0.0.1:8000/postman/"

        payload = {"wallet_id":wallet_id  , "user_name":user_name, "money":money}
        payload = json.dumps(payload)
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data = payload)
        data = response.text

        
    except MultiValueDictKeyError:
        is_private = False
    return render(request, 'temp.html',{'data':data})
def loadinguser(request):
    try:
        wallet_id = request.GET['id']
        user_name = request.GET['name']
    
        url = "http://127.0.0.1:8000/postman/"

        payload = {"wall_id":wallet_id  , "user_name":user_name}
        payload = json.load(payload)
        
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data = payload)
        return Response(payload["money"])
        data = response.text


    except MultiValueDictKeyError:
        is_private = False
    # return render(request, 'temp.html')
   
        

class walletView(APIView):
    def get(self,request):
        queryset = wallet.objects.filter(wallet_id=request.data.get("wall_id")).values().first()
        return Response(queryset)
    def post(self,request):
        queryset=request.data
        serializer = walletserializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()
            # emailSend(request.data.get("Email"),request.data.get("Name"))
        return Response({"success ": "the user with the name '{}' is update". format(save_data.user_name)})   
    def put(self,request,pk):
        queryset =get_object_or_404(wallet.objects.all(), pk=pk)
        parsed_data=request.data 
        serializer = walletserializer(instance=queryset, data=parsed_data, partial=True)
       
