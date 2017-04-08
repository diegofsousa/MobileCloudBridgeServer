from django.shortcuts import render

import requests
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Server

class StatusView(APIView):

	def get(self, request, format=None):
		try:
			lista = []
			for server in Server.objects.all():
				try:
					r = requests.get('http://'+server.ip+':8000/api')
					print(r.status_code)
					print(json.loads(r.content.decode()))
					if r.status_code == 200 and json.loads(r.content.decode()) == 'true':
						lista.append([[server.name], ['Ok']])
					else:
						lista.append([[server.name], ['Não conectado']])
				except Exception as e:
					print(e)
					lista.append([[server.name], ['Não conectado']])

			user = Server.objects.all()
			return Response(json.dumps(lista))
		except Exception as e:
			print(e)
			return Response('Erro na conexão')

class OperationView(ApiView):
	def post(self, request, format=None):
		try:
			listaIter = []
			listaStr = request.data.split(',')
			for i in listaStr:listaIter.append(int(i))
			listaIter.sort()
			print(listaIter)
			return Response(listaIter, status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

