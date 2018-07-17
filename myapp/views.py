# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

# Create your views here.
@api_view(['POST','GET'])
def add(request):
    if request.method == 'GET':
	#print in the command line.
	print("Ok report")
        return Response(1, status=200)
    elif request.method == 'POST':
	#print in the command line.
	print("Bad Request")
        return Response(2, status=404)

