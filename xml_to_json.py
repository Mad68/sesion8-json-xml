import xml.etree.ElementTree as ET
import json
# 1. Parsear el XML
tree = ET.parse('routing_table.xml')
root = tree.getroot()
# 2. Convertir cada nodo <route> a un diccionario de Python
routes_list = []
for route in root.findall('.//route'):
    route_data = {
        "network": route.find('network').text,
        "mask": route.find('mask').text,
        "next_hop": route.find('next_hop').text,
        "protocol": route.find('protocol').text,
        "metric": int(route.find('metric').text)
    }
    routes_list.append(route_data)
# 3. Construir la estructura principal
output_data = {
    "router_id": root.attrib['id'],
    "routes": routes_list
}
# 4. Guardar como archivo JSON identado (4 espacios)
with open('routing_table_normalized.json', 'w', encoding='utf-8') as json_file:
    json.dump(output_data, json_file, indent=4)
print("✔ Conversión de XML a JSON realizada con éxito. Archivo 'routing_table_normalized.json' generado.")