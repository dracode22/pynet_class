from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable


a_device = Device(host="184.105.247.76", user='pyclass', password='88newclass')
a_device.open()
a_device.timeout = 120
routes = RouteTable(a_device)
routes.get()



for route, param in routes.items():
    print route
    for k, v in param:
        print k, v
    print ''
    
