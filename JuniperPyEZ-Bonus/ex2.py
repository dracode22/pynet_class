
from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
a_device = Device(host="184.105.247.76", user='pyclass', password='88newclass')
a_device.open()
a_device.timeout = 120
ports = EthPortTable(a_device)
ports.get()

for int in ports.keys():
    print '=========='
    print "Stats for interface {}".format(int)
    for k,v in ports[int].items():
        if k == 'rx_packets' or k == 'tx_packets':
            print k, v
    print '=========='

