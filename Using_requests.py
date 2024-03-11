import requests

# MISP configuration
misp_url = 'https://127.0.0.1/attributes/restSearch'
misp_key = 'J0TcdxuP80xvj26sirZaqidaV7525QnQhmAGhXHY'
verify_ssl = False  # Set to True if your MISP instance has a valid SSL certificate


def search_misp_attributes(type, value):
    # Search for attributes in MISP
    attributes = requests.post(misp_url, headers={'Authorization': misp_key, "Accept": "application/json", "Content-Type": "application/json"},
                               json={"value": value, "type": type, "returnFormat": "json"}, verify=verify_ssl)

    attributes = attributes.json()['response']
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


types_list = [
    "md5", "sha1", "sha256", "filename", "pdb", "filename|md5", "filename|sha1",
    "filename|sha256", "ip-src", "ip-dst", "hostname", "domain", "domain|ip",
    "email", "email-src", "eppn", "email-dst", "email-subject", "email-attachment",
    "email-body", "float", "git-commit-id", "url", "http-method", "user-agent",
    "ja3-fingerprint-md5", "jarm-fingerprint", "favicon-mmh3", "hassh-md5",
    "hasshserver-md5", "regkey", "regkey|value", "AS", "snort", "bro", "zeek",
    "community-id", "pattern-in-file", "pattern-in-traffic", "pattern-in-memory",
    "filename-pattern", "pgp-public-key", "pgp-private-key", "ssh-fingerprint",
    "yara", "stix2-pattern", "sigma", "gene", "kusto-query", "mime-type",
    "identity-card-number", "cookie", "vulnerability", "cpe", "weakness", "link",
    "comment", "text", "hex", "other", "named pipe", "mutex", "process-state",
    "target-user", "target-email", "target-machine", "target-org", "target-location",
    "target-external", "btc", "dash", "xmr", "iban", "bic", "bank-account-nr",
    "aba-rtn", "bin", "cc-number", "prtn", "phone-number", "threat-actor",
    "campaign-name", "campaign-id", "malware-type", "uri", "authentihash",
    "vhash", "ssdeep", "imphash", "telfhash", "pehash", "impfuzzy", "sha224",
    "sha384", "sha512", "sha512/224", "sha512/256", "sha3-224", "sha3-256",
    "sha3-384", "sha3-512", "tlsh", "cdhash", "filename|authentihash",
    "filename|vhash", "filename|ssdeep", "filename|imphash", "filename|impfuzzy",
    "filename|pehash", "filename|sha224", "filename|sha384", "filename|sha512",
    "filename|sha512/224", "filename|sha512/256", "filename|sha3-224",
    "filename|sha3-256", "filename|sha3-384", "filename|sha3-512", "filename|tlsh",
    "windows-scheduled-task", "windows-service-name", "windows-service-displayname",
    "whois-registrant-email", "whois-registrant-phone", "whois-registrant-name",
    "whois-registrant-org", "whois-registrar", "whois-creation-date",
    "x509-fingerprint-sha1", "x509-fingerprint-md5", "x509-fingerprint-sha256",
    "dns-soa-email", "size-in-bytes", "counter", "datetime", "port", "ip-dst|port",
    "ip-src|port", "hostname|port", "mac-address", "mac-eui-64",
    "email-dst-display-name", "email-src-display-name", "email-header",
    "email-reply-to", "email-x-mailer", "email-mime-boundary", "email-thread-index",
    "email-message-id", "github-username", "github-repository", "github-organisation",
    "jabber-id", "twitter-id", "dkim", "dkim-signature", "first-name",
    "middle-name", "last-name", "full-name", "date-of-birth", "place-of-birth",
    "gender", "passport-number", "passport-country", "passport-expiration",
    "redress-number", "nationality", "visa-number", "issue-date-of-the-visa",
    "primary-residence", "country-of-residence", "special-service-request",
    "frequent-flyer-number", "travel-details", "payment-details",
    "place-port-of-original-embarkation", "place-port-of-clearance",
    "place-port-of-onward-foreign-destination", "passenger-name-record-locator-number",
    "mobile-application-id", "azure-application-id", "chrome-extension-id", "cortex",
    "boolean", "anonymised"
]

index = 1
for t in types_list:
    print(f'{index}. {t}')
    index += 1

input_type = input("Enter the type of attribute to search for:")
input_value = input("Enter the value to search for:")
search_misp_attributes(input_type, input_value)

