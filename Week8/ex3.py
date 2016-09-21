#!/usr/bin/env python

from net_system.models import NetworkDevice
import django



django.setup()



test_rtr1 = NetworkDevice(
    device_name='test-rtr1',
    device_type='cisco_ios',
    ip_address='22.22.22.22',
    port=22,
)
test_rtr1.save()

test_rtr2 = NetworkDevice.objects.get_or_create(
    device_name='test-rtr2',
    device_type='cisco_ios',
    ip_address='22.22.22.22',
    port=22,
)


devices = NetworkDevice.objects.all()
for a_device in devices:
    print a_device


