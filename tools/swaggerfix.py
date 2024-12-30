import json

def find_instances(obj, key, value, path=[]):
    instances = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            new_path = path + [k]
            if k == key and v == value:
                instances.append(new_path)
            instances += find_instances(v, key, value, path=new_path)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            new_path = path + [i]
            instances += find_instances(v, key, value, path=new_path)
    return instances


file_path = 'swagger/compute.swagger.json'
with open(file_path, 'r') as file:
    json_data = json.load(file)

instances = find_instances(json_data, "name", "body")

# Print the paths of instances
for i in instances:
    json_data[i[0]][i[1]][i[2]][i[3]][i[4]]["name"] = json_data[i[0]][i[1]][i[2]]["operationId"] + "Body"

# remove id required
json_data['definitions']['Disk']['required'] = ['sizeGib']

with open('fix.swagger.json', 'w') as file:
    json.dump(json_data, file, indent=2)
