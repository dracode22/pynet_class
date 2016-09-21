


from jnpr.junos import Device
a_device = Device(host="184.105.247.76", user='pyclass', password='88newclass')
a_device.open()
a_device.timeout = 120
print a_device.facts

