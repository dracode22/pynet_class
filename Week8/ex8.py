#!/usr/bin/env python


from datetime import datetime
from netmiko import ConnectHandler

from net_system.models import NetworkDevice
import django

from multiprocessing import Process, Queue




def show_version_queue(a_device, output_q):
    
    output_dict = {}
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address, username=creds.username, password=creds.password, port=a_device.port, secret='')

    
    output = '='*37+str(a_device.device_name)+'='*37 + "\n"
    output += remote_conn.send_command_expect("show version")
    output += '='*80 + "\n"
    output_dict[a_device.device_name] = output
    output_q.put(output_dict)

django.setup()

start_time = datetime.now()
output_q = Queue(maxsize=20)
devices = NetworkDevice.objects.all()

procs =[]

for a_device in devices:
    my_proc = Process(target=show_version_queue, args=(a_device, output_q))
    my_proc.start()
    procs.append(my_proc)



for a_proc in procs:
    print a_proc
    a_proc.join()
    
while not output_q.empty():
    my_dict = output_q.get()
    for k, v in my_dict.iteritems():
        print v
    

elapsed_time = datetime.now() - start_time

print "Elapsed time: {}".format(elapsed_time)

