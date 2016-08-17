import cPickle as pickle
import os.path
from getpass import getpass
from datetime import datetime

from snmp_helper import snmp_get_oid_v3, snmp_extract
from email_helper import send_mail


# Constants
DEBUG = True

# 300 seconds (converted to hundredths of seconds)
RELOAD_WINDOW = 300 * 100

# Uptime when running config last changed
RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'

# Relevant SNMP OIDs
SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_UPTIME = '1.3.6.1.2.1.1.3.0'


def get_saved_dicts(file_name):
	
	if not os.path.isfile(file_name):
		return {}
		
	net_dicts = {}
	with open(file_name, 'r') as f:
		dicts = pickle.load(f)
		for key in dicts.keys():
			net_dicts[dicts[device_name]] = dicts
		
		return (net_dicts)

def send_notification(device):

	current_time = datetime.now()
	name_of_device = str(device[device_name])
	
	
	sender = 'stelica.dragnia@gmail.com'
	recipient = 'stelica.dragnia@gmail'
	subject = 'Device {0} was modified' .format(name_of_device)
	
	message = '''

The running configuration of {0} was modified at: {1}

'''.format(name_of_device, current_time)

	if send_mail(recipient, subject, message, sender):
		print 'Email notification sent to %s ' %recipient
		return True



def main():
    
    snmp_user = ('pysnmp', 'galileo1', 'galileo1')
    pynet_rtr1 = ('184.105.247.70', 161)
    pynet_rtr2 = ('184.105.247.71', 161)
    
    prev_data = get_saved_dicts('devices.pkl')
    
    
    current_data = {}
    
    
    for device in (pynet_rtr1, pynet_rtr2):
        snmp_data = []
        
        for oid in (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED):
            try:
                value = snmp_extract(snmp_get_oid_v3(device, snmp_user, oid=oid))
                snmp_data.append(int(value))
            except ValueError:
                snmp_data.append(value)
            
            device_name, uptime, last_changed = snmp_data
            
        
        if device_name in prev_data:
            prev_dev = prev_data[device_name]
            
            if uptime < prev_dev['uptime'] or last_changed < prev_dev['last_changed']
            
                if last_changed < RELOAD_WINDOW:
                    print 'Device reloaded but not changed'
                    current_data['device'] = {'device_name': device_name, 'uptime' = uptime, 'last_changed' = last_changed}
                    
                else:
                
                    print ' Device reloaded and changed'
                    send_notification(current_data[device_name])
                    current_data['device'] = {'device_name': device_name, 'uptime' = uptime, 'last_changed' = last_changed}
            
            elif last_changed > prev_dev['last_changed']
                print ' Device changed'
				send_notification(current_data[device_name])
				current_data['device'] = {'device_name': device_name, 'uptime' = uptime, 'last_changed' = last_changed}				

            elif last_changed == prev_dev['last_changed']
                print ' Device not changed'
				current_data['device'] = {'device_name': device_name, 'uptime' = uptime, 'last_changed' = last_changed}	
		
		else:
			current_data['device'] = {'device_name': device_name, 'uptime' = uptime, 'last_changed' = last_changed}
		
	with open('devices.pkl', 'w') as f:
		for key in current_data.keys():
			pickle.dump(key, f)
			
		print
		
if __name__ == '__main__':
	main()
	
			
                    
