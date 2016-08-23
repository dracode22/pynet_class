#!/usr/bin/env python

import multiprocessing
from datetime import datetime


from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException, NetMikoAuthenticationException


from test_devices import pynet1, pynet2, juniper_srx



def print_output(results):
    
    print "\n Successful devices:"
    for a_dict in results:
        for identifier, val in a_dict.iteritems():
            success, out_string) = val
            
            if success:
            
            print 'Device = {0}\n'.format(identifier)
            print out_string
            
            
    print "\n\n Failed devices:\n"
    for a_dict in result:
        for identifier, val in a_dict.iteritems():
            (success, out_string) = val
            if not success:
                print 'Device failed = {0}\n'.format(identifier)
                
                
    print "\n End time: " + str(datetime.no())
    

def worker_cmd(a_device, mp_queue, cmd='show arp'):
    identifier = '{ip}:{port}'.format(**a_device)
    return_data = {}
    
    
    
    try:
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command(cmd)
        
        
        return_data[identifier] = (True, output)
        
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        return_data[identifier] = (False, e)
        
        
    mp_queue.put(return_data)
    
    
    
    
def main():


    password = getpass()
    
    
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
        
        try:
            a_dict['port']
        except KeyError:
            a_dict['port'] = 22
            
            
    mp_queue - multiprocessing.Queue()
    processes = []
    
    
    
    print "\Start time: " + str(datetime.now())
    
    for a_device in (pynet1, pynet2, juniper_srx):
        p = multiprocessing.Process(target=worker_cmd, args=(a_device,mp_queue))
        processes.append(p)
        
        
        p.start()
        
    for p in processes:
        p.join()
        
        
    results = []
    for p in processes:
        results.append(mp_queue.get())
        
    print_output(results)

    
if __name__ == "__main__":
    main()

