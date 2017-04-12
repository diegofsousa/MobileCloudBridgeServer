from django.shortcuts import render, get_object_or_404

import requests
from requests import ConnectTimeout
from requests.exceptions import Timeout
#requests.exceptions.RequestException
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Server

class StatusView(APIView):
	'''
	O verbo get desta Classe Based View, retorna o estado de cada servidor.
	O tempo de espera pela requisição (TTL) é reduzido (1 s/requisição) por conta
	dos testes em pequena escala.
	'''

	def get(self, request, format=None):
		try:
			lista = []
			i = 0
			a = Server.objects.count()


			for server in Server.objects.all():
				print(server.name)
				try:
					r = requests.get('http://'+server.ip+':8000/api', timeout=1)
					print(r.status_code)
					print(json.loads(r.content.decode()))
					if r.status_code == 200 and json.loads(r.content.decode()) == 'true':
						lista.append([[server.name], ['Ok']])
					else:
						lista.append([[server.name], ['Não conectado']])
				except Exception as e:
					print(e)
					#continue
					lista.append([[server.name], ['Limite de TTL atingido']])
			return Response(json.dumps(lista))
		except Exception as e:
			print(e)
			return Response('Erro na conexão')

class OrderView(APIView):
	'''
	O verbo post desta Class Based View replica outra requisição ao servidor escolhido
	e retorna ao cliente a lista requisitada ordenada.
	'''

	def post(self, request, servername, format=None):
		instanciaServer = get_object_or_404(Server, name=servername)
		#print(request.data.split(","))
		print(request.data)
		try:
			URL = 'http://'+instanciaServer.ip+':8000/api/order'
			client = requests.session()
			client.get(URL) # sets cookie
			#csrftoken = client.cookies['csrftoken']
			print(request.data['data'].split(","))
			payload = {
			'data':request.data['data'],
			}
			r = client.post(URL, data=payload, headers=dict(Referer=URL))
			print(r)
			return Response(list(r), status=status.HTTP_201_CREATED)
		except Exception as e:
			print(e)
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class SumView(APIView):
	'''
	O verbo post desta Class Based View replica outra requisição ao servidor escolhido
	e retorna ao cliente a soma da lista requisitada.
	'''

	def post(self, request, servername, format=None):
		instanciaServer = get_object_or_404(Server, name=servername)
		print(request.data['data'].split(","))
		#print(request.data)
		try:
			URL = 'http://'+instanciaServer.ip+':8000/api/sum'
			client = requests.session()
			client.get(URL) # sets cookie
			#csrftoken = client.cookies['csrftoken']
			print(request.data['data'].split(","))
			payload = {
			'data':request.data['data'],
			}
			r = client.post(URL, data=payload, headers=dict(Referer=URL))
			print(r)
			return Response(list(r), status=status.HTTP_201_CREATED)
		except Exception as e:
			print(e)
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class MaxView(APIView):
	'''
	O verbo post desta Class Based View replica outra requisição ao servidor escolhido
	e retorna ao cliente o maior numero da lista requisitada.
	'''

	def post(self, request, servername, format=None):
		instanciaServer = get_object_or_404(Server, name=servername)
		print(request.data['data'].split(","))
		print(request.data)
		try:
			URL = 'http://'+instanciaServer.ip+':8000/api/max'
			client = requests.session()
			client.get(URL) # sets cookie
			#csrftoken = client.cookies['csrftoken']
			print(request.data['data'].split(","))
			payload = {
			'data':request.data['data'],
			}
			r = client.post(URL, data=payload, headers=dict(Referer=URL))
			print(r)
			return Response(list(r), status=status.HTTP_201_CREATED)
		except Exception as e:
			print(e)
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

class MinView(APIView):
	'''
	O verbo post desta Class Based View replica outra requisição ao servidor escolhido
	e retorna ao cliente o menor numero da lista requisitada.
	'''

	def post(self, request, servername, format=None):
		instanciaServer = get_object_or_404(Server, name=servername)
		print(request.data['data'].split(","))
		print(request.data)
		try:
			URL = 'http://'+instanciaServer.ip+':8000/api/min'
			client = requests.session()
			client.get(URL) # sets cookie
			#csrftoken = client.cookies['csrftoken']
			print(request.data['data'].split(","))
			payload = {
			'data':request.data['data'],
			}
			r = client.post(URL, data=payload, headers=dict(Referer=URL))
			print(r)
			return Response(list(r), status=status.HTTP_201_CREATED)
		except Exception as e:
			print(e)
			return Response({"message":"403 Forbidden"}, status=status.HTTP_409_CONFLICT)

