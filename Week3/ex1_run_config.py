
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
                    
            
            elif last_changed < 
                    
                    
            
    
    

