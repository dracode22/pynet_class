#!/usr/bin/env python

from net_system.models import NetworkDevice
import django



django.setup()



test_rtr1 = NetworkDevice.objects.get(device_name='test-rtr1')
test_rtr2 = NetworkDevice.objects.get(device_name='test-rtr2')

for a_device in test_rtr1, test_rtr2:
    a_device.delete()

devices = NetworkDevice.objects.all()
for a_device in devices:
    print a_device
