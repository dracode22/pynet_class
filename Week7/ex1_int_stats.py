# Use Arista's eAPI to obtain 'show interfaces' from the switch.
# Parse the 'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the switch.
# Accomplish this using Arista's pyeapi.
 
 
 
import pyeapi
import re

pynet_sw3 = pyeapi.connect_to('pynet-sw3')

show_int = pynet_sw3.enable("show interfaces")
for key in show_int[0]['result']['interfaces'].keys():
    print '\n'
    print "===={}====".format(key)
    key_str = str(key)
    matchObj = re.match(r'^Vlan[1-4094]$', key_str)
    if matchObj:
        print "This is a VLAN interface and Arista doesn't have any stats for VLANs"
    else:
        in_octets = show_int[0]['result']['interfaces'][key]['interfaceCounters']['inOctets']
        out_octets = show_int[0]['result']['interfaces'][key]['interfaceCounters']['outOctets']
        print "Total In Octets  {}".format(in_octets)
        print "Total Out Octets {}".format(out_octets)




