

from ciscoconfparse import CiscoConfParse

cisco_cfg_parse = CiscoConfParse("class1_cisco_ipsec.txt")

crypto_map = cisco_cfg_parse.find_objects(r"^crypto map CRYPTO")

for entry in crypto_map:
        print entry.children

print
print
print
print
print
print
	
crypto_map_dh2 = list()

for entry in crypto_map:
        if entry.re_search_children(r"set pfs group2"):
                crypto_map_dh2 = crypto_map_dh2.append(entry)
print crypto_map_dh2

