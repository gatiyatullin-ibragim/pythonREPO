import json

file_path = "sample-data.json"
with open(file_path, "r") as file:
    data = json.load(file)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<15} {'Speed':<10} {'MTU':<5}")
print("-" * 80)


for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else "-"
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {description:<15} {speed:<10} {mtu:<5}")
