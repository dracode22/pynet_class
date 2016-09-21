#!/usr/bin/env python

from net_system.models import NetworkDevice
import django



django.setup()
devices = NetworkDevice.objects.all()

for a_device in devices:
    if 'cisco' in a_device.device_type:
        a_device.vendor = 'Cisco'
    elif 'juniper' in a_device.device_type:
        a_device.vendor = 'Juniper'
    elif 'arista' in a_device.device_type:
        a_device.vendor = 'Arista'
    a_device.save()
    
for a_device in devices:
    print a_device, a_device.vendor
    
    
    
