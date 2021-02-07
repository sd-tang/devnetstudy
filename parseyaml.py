import json
import yaml

yaml_file = open("example.yml","r")

pythondata = yaml.safe_load(yaml_file)

print("Juniper:", pythondata['Juniper'])

print("List of VMware products: %s" % pythondata['VMware'])

print("\n\n")

print(json.dumps(pythondata))
