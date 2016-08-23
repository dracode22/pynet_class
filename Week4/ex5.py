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
    
    
    print "Config mode:{}".format(net_connect2.check_config_mode())
    print "Current prompt: {}".format(net_connect2.find_prompt())
    
    
    
if __name__ == "__main__":
    main()
    
