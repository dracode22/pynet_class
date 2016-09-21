#!/usr/bin/env python


from datetime import datetime
from netmiko import ConnectHandler

from net_system.models import NetworkDevice
import django

from multiprocessing import Process




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

procs =[]

for a_device in devices:
    my_proc = Process(target=show_version, args=(a_device,))
    my_proc.start()
    procs.append(my_proc)



for a_proc in procs:
    print a_proc
    a_proc.join()
    

elapsed_time = datetime.now() - start_time

print "Elapsed time: {}".format(elapsed_time)

