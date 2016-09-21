#!/usr/bin/env python

from net_system.models import NetworkDevice
from datetime import datetime
from netmiko import ConnectHandler
import django

import threading



def show_version(a_device):

    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address, username=creds.username, password=creds.password, port=a_device.port, secret='')

    print
    print '='*37,a_device.device_name,'='*37
    print remote_conn.send_command_expect("show version")
    print '='*80
    print

django.setup()

start_time = datetime.now()
devices = NetworkDevice.objects.all()

for a_device in devices:
    my_thread = threading.Thread(target=show_version, args=(a_device,))
    my_thread.start()


main_thread = threading.currentThread()

for a_thread in threading.enumerate():
    if a_thread != main_thread:
        print a_thread
        a_thread.join()

elapsed_time = datetime.now() - start_time

print "Elapsed time: {}".format(elapsed_time)

