"""
WSGI config for CloudServerBridgeAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import netifaces

from django.core.wsgi import get_wsgi_application
try:
	print('IP local wifi: ' + netifaces.ifaddresses('wlan0')[2][0]['addr'])
except Exception as e:
	print('Interface Wifi não detectada')

try:
	print('IP local cabo: ' + netifaces.ifaddresses('eth0')[2][0]['addr'])
except Exception as e:
	print('Interface cabeada não detectada')



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CloudServerBridgeAPI.settings")

application = get_wsgi_application()
