

from ciscoconfparse import CiscoConfParse


print '========CLASS1 EX 8 =============='
cisco_cfg_parse = CiscoConfParse("class1_cisco_ipsec.txt")

crypto_map = cisco_cfg_parse.find_objects(r"^crypto map CRYPTO")

for entry in crypto_map:
    print entry.text
    for child in entry.children:
        print child.text

print
print
print
print '========CLASS1 EX 9============= '
print
print
	
crypto_map_dh2 = list()

for entry in crypto_map:
        if entry.re_search_children(r"set pfs group2"):
                print entry.text
                crypto_map_dh2.append(entry)




print
print
print
print
print '========CLASS1 EX 10============= '
print

crypto_map_no_aes = cisco_cfg_parse.find_objects_wo_child(r"^crypto map CRYPTO", r"set transform-set AES-SHA")
for entry in crypto_map_no_aes:
    print entry.text
    for child in entry.re_search_children(r"transform-set"):
        print child.text

