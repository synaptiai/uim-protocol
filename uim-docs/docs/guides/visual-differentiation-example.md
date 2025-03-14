# Visual Differentiation Example

This page demonstrates how to use the visual differentiation styling to clearly distinguish between specification content and implementation content.

## Using Admonition Blocks

### Specification Content

You can use the `spec` admonition to highlight specification content:

!!! spec "Specification: Intent Format"
    An intent must follow this format:
    
    ```json
    {
      "intent_uid": "namespace:intent_name:version",
      "parameters": {
        "param1": "value1",
        "param2": "value2"
      }
    }
    ```
    
    The `intent_uid` is a required field and must follow the format `namespace:intent_name:version`.

### Implementation Content

You can use the `implementation` admonition to highlight implementation content:

!!! implementation "Implementation: JavaScript Example"
    Here's how you might implement an intent in JavaScript:
    
    ```javascript title="Implementation: Creating an Intent"
    function createIntent(namespace, intentName, version, parameters) {
      return {
        intent_uid: `${namespace}:${intentName}:${version}`,
        parameters: parameters || {}
      };
    }
    
    // Example usage
    const searchIntent = createIntent(
      'ecommerce.com',
      'SearchProducts',
      'v1',
      {
        query: 'laptop',
        category: 'electronics'
      }
    );
    ```

## Using Section Headers

You can also use section headers to differentiate between specification and implementation content:

## Specification: Intent Discovery

The UIM Protocol defines a standard way for AI agents to discover available intents from web services. This is done through DNS TXT records and the `agents.json` file.

## Implementation: Intent Discovery in Node.js

Here's an example of how you might implement intent discovery in Node.js:

```javascript title="Implementation: Intent Discovery"
const dns = require('dns');
const axios = require('axios');

async function discoverIntents(domain) {
  try {
    // Look up DNS TXT records
    const txtRecords = await dns.promises.resolveTxt(domain);
    
    // Find the record with the agents.json URL
    const agentsRecord = txtRecords.find(record => 
      record[0].startsWith('uim-agents-file=')
    );
    
    if (!agentsRecord) {
      throw new Error('No agents.json URL found in DNS TXT records');
    }
    
    // Extract the URL
    const agentsUrl = agentsRecord[0].split('=')[1];
    
    // Fetch the agents.json file
    const response = await axios.get(agentsUrl);
    
    return response.data;
  } catch (error) {
    console.error('Error discovering intents:', error);
    throw error;
  }
}
```

## Using Code Block Titles

You can also use code block titles to differentiate between specification and implementation content:

```json title="Specification: agents.json Format"
{
  "service_info": {
    "name": "Example E-commerce Service",
    "description": "An e-commerce service that provides product search and ordering capabilities",
    "logo_url": "https://example.com/logo.png",
    "website": "https://example.com",
    "terms_url": "https://example.com/terms",
    "privacy_url": "https://example.com/privacy"
  },
  "intents": [
    {
      "intent_uid": "ecommerce.com:SearchProducts:v1",
      "name": "Search Products",
      "description": "Search for products based on criteria",
      "endpoint": "https://api.example.com/uim/intents/search",
      "parameters": {
        "query": {
          "type": "string",
          "description": "Search query",
          "required": true
        },
        "category": {
          "type": "string",
          "description": "Product category",
          "required": false
        }
      }
    }
  ],
  "policy_url": "https://example.com/uim-policy.json"
}
```

```python title="Implementation: Python Intent Discovery"
import dns.resolver
import requests

def discover_intents(domain):
    try:
        # Look up DNS TXT records
        txt_records = dns.resolver.resolve(domain, 'TXT')
        
        # Find the record with the agents.json URL
        agents_url = None
        for record in txt_records:
            for txt in record.strings:
                txt_str = txt.decode('utf-8')
                if txt_str.startswith('uim-agents-file='):
                    agents_url = txt_str.split('=')[1]
                    break
            if agents_url:
                break
        
        if not agents_url:
            raise Exception('No agents.json URL found in DNS TXT records')
        
        # Fetch the agents.json file
        response = requests.get(agents_url)
        response.raise_for_status()
        
        return response.json()
    except Exception as e:
        print(f'Error discovering intents: {e}')
        raise
