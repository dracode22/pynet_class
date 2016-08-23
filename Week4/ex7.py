#!/urs/bin/env python



from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx
from getpass import getpass

def main():


    password = getpass()
    
    
    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
        
    net_connect2 = ConnectHandler(**pynet2)
    net_connect2.config_mode()
    net_connect2.send_command("logging buffered 21110")
    net_connect2.send_command("end")
    
    output = net_connect2.send_command("show run | i logging")
        
    
    
    print output    
    
    
if __name__ == "__main__":
    main()
    
