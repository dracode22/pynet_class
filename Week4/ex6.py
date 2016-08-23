#!/urs/bin/env python



from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx
from getpass import getpass

def main():


    password = getpass()
    
    
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
        
        net_connect = ConnectHandler(**a_dict)
        output = net_connect.send_command("show arp")
        
    
    
        print "Device name:{}".format(net_connect.ip)

        print output
    
    
if __name__ == "__main__":
    main()
    
