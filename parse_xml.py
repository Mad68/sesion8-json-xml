import xml.etree.ElementTree as ET

# Cargar y parsear el XML
tree = ET.parse('routing_table.xml')
root = tree.getroot()

print(f"=== Dispositivo ID: {root.attrib['id']} ===")
print("Tabla de Enrutamiento Extraída:")

# Recorrer todos los elementos <route>
for route in root.findall('.//route'):
    net = route.find('network').text
    mask = route.find('mask').text
    nexthop = route.find('next_hop').text
    proto = route.find('protocol').text
    metric = route.find('metric').text
    print(f" - Red: {net}/{mask} | Next-Hop: {nexthop} | Protocolo: {proto} | Métrica: {metric}")