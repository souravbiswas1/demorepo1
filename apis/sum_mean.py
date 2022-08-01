#Importing libraries---
import os
import pandas as pd
import numpy as np
import json
# from bson import json_util
from django.shortcuts import render
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
import pickle
from django.conf import settings


@api_view(['GET'])
def calculate_sum_mean(request):
	def calculate_sum(number1,number2):
		_sum_ = number1 + number2

		key1 = ['Sum of the numbers']
		val1 = [_sum_]
		keyval1 = dict(zip(key1,val1))
		return keyval1

	def calculate_mean(number1,number2):
		_mean_ = (number1 + number2)/2

		key1 = ['Avg of the numbers']
		val1 = [_mean_]
		keyval1 = dict(zip(key1,val1))
		return keyval1


	if request.method =="GET":
		if request.GET.get('method') == 'sum' :
			try:
				resp_sum = calculate_sum(int(request.GET.get('Num1')),int(request.GET.get('Num2')))
				return Response(resp_sum)
			except Exception as e:
				print(e)
				return Response("Error in Sum for insufficient data",status=status.HTTP_400_BAD_REQUEST)
		elif request.GET.get('method') == 'mean' :
			try:
				resp_mean = calculate_mean(int(request.GET.get('Num1')),int(request.GET.get('Num2')))
				return Response(resp_mean)
			except Exception as e:
				print(e)
				return Response("Error in Mean for insufficient data",status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response("Error in GET request",status=status.HTTP_400_BAD_REQUEST)
