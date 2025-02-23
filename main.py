import json

# The data can be seen as a tree, where the existence of the "properties" key 
# indicates that the node has children and the "type" key indicates that it has no children. 

def count_keys(data={}, key="", depth=1):
    count = 0
    if "type" in data:
        count += 1
    elif "properties" in data:
        for property_key, property in data["properties"].items():
            count += count_keys(
                data=property,
                key=f"{key}.{property_key}",
                depth=depth-1)
    if depth >= 1:
        print(f"{key}: {count}")
    return count


# Load data from file
with open('mappings.json', 'r') as file:
    data = json.load(file)

for key, data in data.items():
    count_keys(data=data,
                    key=key,
                    depth=2)
