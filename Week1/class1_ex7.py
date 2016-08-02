import yaml
import json
import pprint



with open ("class1_yaml_file.yml") as f:
	new_list_yaml = yaml.load(f)

	
with open ("class1_json_file.json") as f:
	new_list_json = json.load(f)


print
pprint.pprint(new_list_json)
pprint.pprint(new_list_yaml)
print
	
