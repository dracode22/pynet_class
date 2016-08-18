

from snmp_helper import snmp_get_oid_v3, snmp_extract
import line_graph
import time




def get_interface_stats(snmp_device, snmp_user, stat_type, row_number):


	oid_dict = {
		'in_octets': '1.3.6.1.2.1.2.2.1.10',
		'out_octets':   '1.3.6.1.2.1.2.2.1.16',
		'in_ucast_pkts':    '1.3.6.1.2.1.2.2.1.11',
		'out_ucast_pkts':    '1.3.6.1.2.1.2.2.1.17',
	}
	
	if not stat_type in oid_dict.keys():
		raise ValueError("Invalid value for stat_type: {}" %stat_type)
		
		
		
	row_number = int(row_number)
	
	oid = oid_dict[stat_type]
	oid = oid + '.' str(row_number)
	
	
	snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid)
	return int(snmp_extract(snmp_data))
	
	
def main ():

	snmp_user = ('pysnmp', 'galileo1', 'galileo1'
	snmp_device = ('184.105.247.70', 161)
	
	
	row_number = 5
	
	graph_stats = {
		"in_octets" = [],
		"out_octets" = [],
		"in_ucast_pkts" = []
		"out_ucast_pkts" =[],
	}
	
	base_count_dict = {}
	
	for time in range (0, 65, 5):
		print "\n%20s %-60%s" %("time", time_track)
		
		
		for entry in ("in_octets", "out_octets", "in_ucast_pkts", "out_ucast_pkts"):
			snmp_retrieved_count = get_interface_stats(snmp_device, snmp_user, entry, row_number)
			
			base_count = base_count_dict.get(entry)
			
			if base_count:
				graph_stats[entry].append(snmp_retrieved_count - base_count)
				print "%20s %-60s" %(entry, graph_stats[entry][-1])
				
				
			base_count_dict[entry] = snmp_retrieved_count
			
		time.sleep(10)
		
		
	print
	
	if debug:
		print graph_stats
	
	x_labels = []
	
	for x_label in range (5, 65, 5):
		x_labels.append(str(x_label))
		
	if debug:
		print x_labels
	
	if line_graph.twoline("pynet-rtr1-octets.svg", "pynet-rtr1 Fa4 Input/Output Bytes",
						graph_stats["in_octets"], "In Octets", graph_stats["out_octets"],
						"Out Octets", x_labels):
		print "In/Out octets graph created"
		
	if line_graph.twoline("pynet-rtr1-pkts.svg", "pynet-rtr1 Fa4 Input/Output Unicast Packets",
						graph_stats["in_ucast_pkts"], "In Packets", graph_stats["out_ucast_pkts"],
						
						"Out Packets", x_labels):
						
		print "In/Out Packets graph created"
	print

if __name__ == "__main__"
	main()
		
		
		
