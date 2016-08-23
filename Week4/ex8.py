#!/urs/bin/env python



from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx
from getpass import getpass

def main():


    password = getpass()
    
    
    for a_dict in (pynet1, pynet2):
        a_dict['password'] = password
        
        net_connect = ConnectHandler(**a_dict)
        net_connect.send_config_from_file(config_file='config_file.txt')
            
        output = net_connect.send_command("show run | i logging")
        
        print "Device name:{}".format(net_connect.ip)

        print output
    
    
if __name__ == "__main__":
    main()
    
    
    
    

