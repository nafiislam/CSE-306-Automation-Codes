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
  document.getElementById("checkVulnerabilityButton").addEventListener("click", handleClick);
});

chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  const url = tabs[0].url;
  taburl = url;
  document.getElementById("url-display").textContent = `Current URL: ${url}`;
  console.log(window.location.href)
});

async function handleClick() {
  console.log("Button clicked");
  const res = await searchMispAttributes('url', taburl);
  document.getElementById("result").innerHTML = res;
}