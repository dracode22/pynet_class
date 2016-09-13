import argparse
import pyeapi




parser = argparse.ArgumentParser(description='Add a VLAN')

parser.add_argument('--name', dest='add_vlan',help='Add the VLAN specified', action='store_true')

parser.add_argument('--remove', dest='remove_vlan',help='Remove the VLAN specified', action='store_true')

parser.add_argument('vlan_name', help='A String that will become the VLAN name')

parser.add_argument('vlan_number', type=int,help='an integer that will become the VLAN number')


args = parser.parse_args()

vlan_number = args.vlan_number
vlan_name = args.vlan_name



#Verify if VLAN exists


pynet_sw3 = pyeapi.connect_to('pynet-sw3')
show_vlan = pynet_sw3.enable("show vlan")
for vlan in show_vlan[0]['result']['vlans'].keys():
    if int(vlan) == vlan_number:
        vlan_exists = True
        print "VLAN {} Already exists".format(vlan_number)
    else:
        vlan_exists = False
    
    
    

if args.add_vlan and not(vlan_exists):

    commands = [ 'vlan ' + str (vlan_number), 'name ' + vlan_name]
    print 'Adding VLAN: {} name: {}'.format(vlan_number, vlan_name)
    pynet_sw3.config(commands)
   
elif args.remove_vlan and vlan_exists:
    commands = [ 'no vlan ' + str (vlan_number)]
    print 'Removing VLAN: {} name: {}'.format(vlan_number, vlan_name)
    pynet_sw3.config(commands) 
