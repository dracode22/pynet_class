import yaml
import json

a_list = range(10)
a_list.append({})

a_list[-1]['ip_addr'] = '10.10.10.1'
a_list[-1]['hostname'] = 'Router1'
a_list[-1]['nested_list'] = range(3)


with open ("class1_yaml_file.yml", "w") as f:
    f.write(yaml.dump(a_list, default_flow_style = False))

with open ("class1_json_file.json", "w") as f:
        json.dump(a_list, f)

