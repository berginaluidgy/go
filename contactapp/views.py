from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contact,many

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def welcome(request):
    data=request.data
    contactall=contact.objects.create(name=data['name'],num=data['num'],nameid=data['num'])
    return Response({'satuts':status.HTTP_200_OK})
# @api_view(['POST'])
# def share(request):
#     nameidp=many.objects.get(nameid='')
    
@api_view(['get','post'])
def myshare(request,nameid2):
    print(request.get_host()+'/share/'+str(nameid2))
    if request.method=='POST':
        body=contact.objects.get(nameid=nameid2)
        return Response({'nbr':body.nbr,'lk':request.get_host()+'/share/'+str(nameid2)})
    else:
        body2=contact.objects.get(nameid=nameid2)
        body2.nbr+=1
        body2.save()
        # return Response({'satuts':status.HTTP_200_OK})
        return redirect('yonselkoutklee.vercel.app/')
        # return Response({'satuts':status.HTTP_200_OK})
