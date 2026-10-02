import json

# Cargar el archivo JSON
with open('interfaces.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(f"=== ROUTER: {data['router_id']} ({data['location']}) ===")
print("Interfaces Activas (UP):")

# Filtrar e imprimir solo interfaces activas
for iface in data['interfaces']:
    if iface['status'] == 'up':
        print(f" - Interfaz: {iface['name']} | IP: {iface['ip_address']}/{iface['netmask']} | VLAN: {iface['vlan']}")