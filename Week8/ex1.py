#!/usr/bin/env python

from net_system.models import NetworkDevice, Credentials
import django

django.setup()

devices = NetworkDevice.objects.all()
creds = Credentials.objects.all()



std_creds = creds[0]
arista_creds = creds[1]


for a_device in devices:
    if 'arista' in a_device.device_type:
        a_device.credentials = arista_creds
    else:
        a_device.credentials = std_creds
    a_device.save()
    
    
for a_device in devices:
    print a_device, a_device.credentials

