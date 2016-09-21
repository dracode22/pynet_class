#!/usr/bin/env python

from net_system.models import NetworkDevice
from datetime import datetime
from netmiko import ConnectHandler
import django



def show_version(a_device):
    
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address, username=creds.username, password=creds.password, port=a_device.port, secret='')
    
    print
    print '='*40,a_device.device_name,'='*40
    print remote_conn.send_command_expect("show version")
    print '='*80
    print
    
django.setup()

start_time = datetime.now()
devices = NetworkDevice.objects.all()

for a_device in devices:
    show_version(a_device)
    
elapsed_time = datetime.now() - start_time

print "Elapsed time: {}".format(elapsed_time)






