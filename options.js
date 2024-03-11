const typesList = [
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

const mispUrl = 'https://127.0.0.1/attributes/restSearch';
const mispKey = 'J0TcdxuP80xvj26sirZaqidaV7525QnQhmAGhXHY';
const verifySSL = false;  // Set to true if your MISP instance has a valid SSL certificate
var taburl = ""; 
async function searchMispAttributes(type, value) {
    try {
        const response = await fetch(mispUrl, {
            method: 'POST',
            headers: {
                'Authorization': mispKey,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                value: value,
                type: type,
                returnFormat: 'json',
            }),
        });

        if (!response.ok) {
            return (`<p>HTTP error! Status: ${response.status}</p>`);
        }

        const data = await response.json();
        const attributes = data.response.Attribute;

        if (attributes.length === 0) {
            return ('<p>No matching attributes found in MISP.</p>');
        }

        var returnString = "";

        returnString+= '<p>Attributes found:</p>';
        let cnt = 1;
        for (const attribute of attributes) {
            returnString += `<p><strong>${cnt}. Full details:</strong><br>`;
            returnString += '<pre>'+JSON.stringify(attribute)+'</pre><br>';
            returnString += `- Type: ${attribute.type}, Value: ${attribute.value}</p>`;
            cnt += 1;
        }

        return returnString;
    } catch (error) {
        console.error('Error searching MISP attributes:', error.message);
        return '<p>Error searching MISP attributes</p>';
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const selectElement = document.getElementById('typeSelect');

    typesList.forEach(type => {
        const option = document.createElement('option');
        option.value = type;
        option.text = type;
        selectElement.appendChild(option);
    });

    document.getElementById('saveButton').addEventListener('click', submitHandler);
});

async function submitHandler() {
    const type = document.getElementById('typeSelect').value;
    const value = document.getElementById('valueInput').value;

    console.log("Button clicked");
    console.log(type, value);

    const res = await searchMispAttributes(type, value);
    document.getElementById("result").innerHTML = res;
}