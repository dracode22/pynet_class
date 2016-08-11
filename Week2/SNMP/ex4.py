#!/usr/bin/env python


import snmp_helper


SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_DESCR = '1.3.6.1.2.1.1.1.0'


def main():

    router1 = ('184.105.247.70', 'galileo', 161)
    router2 = ('184.105.247.71', 'galileo', 161)
    
    for router in (router1, router2):
        
        for oid in (SYS_NAME, SYS_DESCR):
            snmp_data = snmp_helper.snmp_get_oid(router, oid)
            output = snmp_helper.snmp_extract(snmp_data)
            
            print output
        print "======"
    print
            
if __name__ == "__main__":
    main()

