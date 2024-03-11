from pymisp import PyMISP

# MISP configuration
misp_url = 'https://localhost'
misp_key = 'J0TcdxuP80xvj26sirZaqidaV7525QnQhmAGhXHY'
verify_ssl = False  # Set to True if your MISP instance has a valid SSL certificate

# Create a PyMISP instance
misp = PyMISP(misp_url, misp_key, verify_ssl)

def search_misp_attributes_ip_dst(ip_dst):
    # Search for attributes in MISP
    attributes = misp.search(controller='attributes', type_attribute='ip-dst', value=ip_dst)
    if len(attributes['Attribute']) == 0:
        print("No matching attributes found in MISP.")
        return False

    print("Attributes found:")
    cnt = 1
    for attribute in attributes['Attribute']:
        print(str(cnt)+". Full details:")
        print(attribute)
        print(f"- Type: {attribute['type']}, Value: {attribute['value']}")
        cnt += 1


input_ip_dst = input("Enter the IP destination address to search for:")
search_misp_attributes_ip_dst(input_ip_dst)
