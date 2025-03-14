# Service Provider Implementation Guide

This guide provides step-by-step instructions for implementing the UIM Protocol in a web service. It covers service registration, intent definition, policy management, and intent execution.

## Overview

Web services use the UIM Protocol to expose their capabilities to AI agents through well-defined intents. This guide will walk you through the process of implementing the UIM Protocol in your web service, from service registration to intent execution.

## Prerequisites

Before implementing the UIM Protocol in your web service, you should have:

- A basic understanding of the UIM Protocol concepts (intents, metadata, PATs)
- A web service with an API
- Knowledge of HTTP requests and JSON processing
- Cryptographic capabilities for signing and verifying signatures

## Implementation Steps

### 1. Set Up Your Development Environment

First, set up your development environment with the necessary libraries for HTTP requests, JSON processing, and cryptography. Here's an example using Node.js:

```javascript
// Required libraries
const express = require('express');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const fs = require('fs');
```

### 2. Generate Key Pair

Generate an RSA key pair for your web service. This will be used for signing PATs and verifying signatures:

```javascript
function generateKeyPair() {
  return crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem'
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem'
    }
  });
}

// Generate and save keys
const { privateKey, publicKey } = generateKeyPair();
fs.writeFileSync('private-key.pem', privateKey);
fs.writeFileSync('public-key.pem', publicKey);
```

### 3. Define Your Intents

Define the intents that your web service will expose to AI agents:

```javascript
const intents = [
  {
    intent_uid: 'example.com:search-products:v1',
    intent_name: 'SearchProducts',
    description: 'Search for products based on criteria',
    input_parameters: [
      { name: 'query', type: 'string', required: true, description: 'Search query' },
      { name: 'category', type: 'string', required: false, description: 'Product category' },
      { name: 'price_range', type: 'string', required: false, description: 'Price range (e.g., "10-100")' },
      { name: 'sort_by', type: 'string', required: false, description: 'Sort criteria' }
    ],
    output_parameters: [
      { name: 'products', type: 'array', description: 'List of matching products' },
      { name: 'total_results', type: 'integer', description: 'Total number of matching products' }
    ],
    endpoint: 'https://api.example.com/products/search',
    tags: ['e-commerce', 'search', 'products']
  },
  {
    intent_uid: 'example.com:get-product-details:v1',
    intent_name: 'GetProductDetails',
    description: 'Get detailed information about a specific product',
    input_parameters: [
      { name: 'product_id', type: 'string', required: true, description: 'Product ID' }
    ],
    output_parameters: [
      { name: 'product', type: 'object', description: 'Product details' }
    ],
    endpoint: 'https://api.example.com/products/details',
    tags: ['e-commerce', 'product', 'details']
  }
];
```

### 4. Define Your Policy

Define the policy that AI agents must adhere to when using your web service:

```javascript
const policy = {
  '@context': 'http://www.w3.org/ns/odrl.jsonld',
  'uid': 'http://example.com/policy/12345',
  'type': 'Set',
  'profile': 'http://example.com/profile/odrl-uim',
  'permission': [
    {
      'target': 'http://example.com/api/intents',
      'action': 'execute',
      'constraint': [
        {
          'leftOperand': 'http://example.com/vocab/rateLimit',
          'operator': 'lte',
          'rightOperand': 1000,
          'unit': 'http://example.com/vocab/hour'
        }
      ],
      'duty': [
        {
          'action': 'pay',
          'target': 'http://example.com/vocab/intentPrice',
          'amount': 0.01,
          'unit': 'http://example.com/vocab/USD'
        }
      ]
    }
  ],
  'prohibition': [
    {
      'target': 'http://example.com/api/intents',
      'action': 'exceedRateLimit'
    }
  ],
  'obligation': [
    {
      'action': 'signPayload',
      'assignee': 'http://example.com/ai-agent/1',
      'target': 'http://example.com/vocab/payload',
      'constraint': [
        {
          'leftOperand': 'http://example.com/vocab/publicKey',
          'operator': 'use',
          'rightOperand': 'MIIBIjANBgkqh...'
        }
      ]
    }
  ]
};
```

### 5. Create the `agents.json` File

Create an `agents.json` file that describes your web service and its intents:

```javascript
const agentsJson = {
  'service-info': {
    'name': 'Example E-commerce Service',
    'description': 'Provides e-commerce functionalities',
    'service_url': 'https://api.example.com',
    'service_logo_url': 'https://example.com/logo.png',
    'service_terms_of_service_url': 'https://example.com/terms',
    'service_privacy_policy_url': 'https://example.com/privacy'
  },
  'intents': intents,
  'uim-public-key': publicKey,
  'uim-policy-file': 'https://example.com/uim-policy.json',
  'uim-api-discovery': 'https://api.example.com/uim/intents/search',
  'uim-compliance': {
    'standards': ['ISO27001', 'GDPR'],
    'regional-compliance': {
      'EU': 'GDPR',
      'US-CA': 'CCPA'
    },
    'notes': 'Data is encrypted in transit and at rest.'
  },
  'uim-license': 'https://uimprotocol.com/licenses/uim-by-nc-v1.0'
};

// Save the agents.json file
fs.writeFileSync('public/agents.json', JSON.stringify(agentsJson, null, 2));
```

### 6. Configure DNS TXT Records

Configure DNS TXT records to help AI agents discover your web service:

```
uim-agents-file=https://example.com/agents.json
uim-api-discovery=https://api.example.com/uim/intents/search
uim-policy-file=https://example.com/uim-policy.json
uim-license=https://uimprotocol.com/licenses/uim-by-nc-v1.0
```

### 7. Implement the Discovery API

Implement the discovery API that allows AI agents to search for intents:

```javascript
const app = express();
app.use(express.json());

// Intent search endpoint
app.get('/uim/intents/search', (req, res) => {
  const { query, tags, intent_name, uid, namespace, description } = req.query;
  
  // Filter intents based on query parameters
  let filteredIntents = [...intents];
  
  if (query) {
    const queryLower = query.toLowerCase();
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_name.toLowerCase().includes(queryLower) ||
      intent.description.toLowerCase().includes(queryLower)
    );
  }
  
  if (tags) {
    const tagList = tags.split(',');
    filteredIntents = filteredIntents.filter(intent => 
      tagList.some(tag => intent.tags.includes(tag))
    );
  }
  
  if (intent_name) {
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_name.toLowerCase() === intent_name.toLowerCase()
    );
  }
  
  if (uid) {
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_uid === uid
    );
  }
  
  if (namespace) {
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_uid.split(':')[0] === namespace
    );
  }
  
  if (description) {
    const descLower = description.toLowerCase();
    filteredIntents = filteredIntents.filter(intent => 
      intent.description.toLowerCase().includes(descLower)
    );
  }
  
  // Pagination
  const page = parseInt(req.query.page) || 1;
  const pageSize = parseInt(req.query.page_size) || 10;
  const startIndex = (page - 1) * pageSize;
  const endIndex = startIndex + pageSize;
  const paginatedIntents = filteredIntents.slice(startIndex, endIndex);
  
  res.json({
    intents: paginatedIntents,
    pagination: {
      total_results: filteredIntents.length,
      total_pages: Math.ceil(filteredIntents.length / pageSize),
      current_page: page,
      page_size: pageSize
    }
  });
});

// Intent details endpoint
app.get('/uim/intents/:intent_uid', (req, res) => {
  const intent = intents.find(i => i.intent_uid === req.params.intent_uid);
  
  if (!intent) {
    return res.status(404).json({
      error: {
        code: 'NOT_FOUND',
        message: `The intent '${req.params.intent_uid}' was not found.`
      }
    });
  }
  
  res.json(intent);
});
```

### 8. Implement the Policy API

Implement the policy API that allows AI agents to retrieve the policy:

```javascript
// Policy endpoint
app.get('/uim-policy.json', (req, res) => {
  res.json(policy);
});
```

### 9. Implement the PAT Issuance API

Implement the PAT issuance API that allows AI agents to request PATs:

```javascript
// PAT issuance endpoint
app.post('/pat/issue', (req, res) => {
  const { agent_id, signed_policy, agent_public_key } = req.body;
  
  // Validate request
  if (!agent_id || !signed_policy || !agent_public_key) {
    return res.status(400).json({
      error: {
        code: 'INVALID_PARAMETER',
        message: 'Missing required parameters.'
      }
    });
  }
  
  try {
    // Verify the signature
    const policyJson = JSON.stringify(policy);
    const verifier = crypto.createVerify('SHA256');
    verifier.update(policyJson);
    const isValid = verifier.verify(
      agent_public_key,
      Buffer.from(signed_policy, 'hex')
    );
    
    if (!isValid) {
      return res.status(400).json({
        error: {
          code: 'INVALID_SIGNATURE',
          message: 'The signature is invalid.'
        }
      });
    }
    
    // Generate PAT
    const pat = {
      iss: 'example.com',
      sub: agent_id,
      exp: Math.floor(Date.now() / 1000) + 86400, // 24 hours
      nbf: Math.floor(Date.now() / 1000),
      jti: crypto.randomBytes(16).toString('hex'),
      scope: intents.map(intent => `${intent.intent_uid}:execute`),
      pol: 'https://example.com/uim-policy.json',
      lmt: {
        rate: 100,
        period: 3600
      }
    };
    
    // Sign PAT
    const token = jwt.sign(pat, privateKey, { algorithm: 'RS256' });
    
    res.json({
      'uim-pat': token,
      'expires_at': new Date(pat.exp * 1000).toISOString()
    });
  } catch (error) {
    console.error('Error issuing PAT:', error);
    res.status(500).json({
      error: {
        code: 'INTERNAL_SERVER_ERROR',
        message: 'An unexpected error occurred on the server.'
      }
    });
  }
});
```

### 10. Implement the Intent Execution API

Implement the intent execution API that allows AI agents to execute intents:

```javascript
// Intent execution endpoint
app.post('/uim/execute', (req, res) => {
  const { intent_uid, parameters } = req.body;
  
  // Validate request
  if (!intent_uid || !parameters) {
    return res.status(400).json({
      error: {
        code: 'INVALID_PARAMETER',
        message: 'Missing required parameters.'
      }
    });
  }
  
  // Verify PAT
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({
      error: {
        code: 'UNAUTHORIZED',
        message: 'Missing or invalid Authorization header.'
      }
    });
  }
  
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, publicKey, { algorithms: ['RS256'] });
    
    // Check if the PAT allows executing this intent
    if (!decoded.scope.includes(`${intent_uid}:execute`)) {
      return res.status(403).json({
        error: {
          code: 'FORBIDDEN',
          message: 'The PAT does not grant permission to execute this intent.'
        }
      });
    }
    
    // Check rate limit
    // In a real implementation, you would use a rate limiting library or database
    
    // Find the intent
    const intent = intents.find(i => i.intent_uid === intent_uid);
    if (!intent) {
      return res.status(404).json({
        error: {
          code: 'NOT_FOUND',
          message: `The intent '${intent_uid}' was not found.`
        }
      });
    }
    
    // Validate parameters
    for (const param of intent.input_parameters) {
      if (param.required && !parameters[param.name]) {
        return res.status(400).json({
          error: {
            code: 'INVALID_PARAMETER',
            message: `Missing required parameter: ${param.name}`
          }
        });
      }
    }
    
    // Execute the intent
    // In a real implementation, you would call your actual business logic here
    if (intent_uid === 'example.com:search-products:v1') {
      // Simulate a product search
      const products = [
        {
          id: '123',
          name: 'Laptop',
          price: 1000,
          description: 'A powerful laptop'
        }
      ];
      
      res.json({
        products,
        total_results: products.length
      });
    } else if (intent_uid === 'example.com:get-product-details:v1') {
      // Simulate getting product details
      res.json({
        product: {
          id: parameters.product_id,
          name: 'Laptop',
          price: 1000,
          description: 'A powerful laptop',
          specifications: {
            processor: 'Intel Core i7',
            memory: '16GB',
            storage: '512GB SSD'
          }
        }
      });
    } else {
      res.status(400).json({
        error: {
          code: 'INTENT_NOT_SUPPORTED',
          message: `The intent '${intent_uid}' is not supported.`
        }
      });
    }
  } catch (error) {
    if (error.name === 'JsonWebTokenError') {
      return res.status(401).json({
        error: {
          code: 'UNAUTHORIZED',
          message: 'Invalid PAT.'
        }
      });
    } else if (error.name === 'TokenExpiredError') {
      return res.status(401).json({
        error: {
          code: 'UNAUTHORIZED',
          message: 'PAT has expired.'
        }
      });
    }
    
    console.error('Error executing intent:', error);
    res.status(500).json({
      error: {
        code: 'INTERNAL_SERVER_ERROR',
        message: 'An unexpected error occurred on the server.'
      }
    });
  }
});
```

### 11. Start the Server

Start the server:

```javascript
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

## Complete Example

Here's a complete example of a web service that implements the UIM Protocol:

```javascript
const express = require('express');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const fs = require('fs');

// Generate key pair
function generateKeyPair() {
  return crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: {
      type: 'spki',
      format: 'pem'
    },
    privateKeyEncoding: {
      type: 'pkcs8',
      format: 'pem'
    }
  });
}

// Load or generate keys
let privateKey, publicKey;
try {
  privateKey = fs.readFileSync('private-key.pem', 'utf8');
  publicKey = fs.readFileSync('public-key.pem', 'utf8');
} catch (error) {
  console.log('Generating new key pair...');
  const keys = generateKeyPair();
  privateKey = keys.privateKey;
  publicKey = keys.publicKey;
  fs.writeFileSync('private-key.pem', privateKey);
  fs.writeFileSync('public-key.pem', publicKey);
}

// Define intents
const intents = [
  {
    intent_uid: 'example.com:search-products:v1',
    intent_name: 'SearchProducts',
    description: 'Search for products based on criteria',
    input_parameters: [
      { name: 'query', type: 'string', required: true, description: 'Search query' },
      { name: 'category', type: 'string', required: false, description: 'Product category' },
      { name: 'price_range', type: 'string', required: false, description: 'Price range (e.g., "10-100")' },
      { name: 'sort_by', type: 'string', required: false, description: 'Sort criteria' }
    ],
    output_parameters: [
      { name: 'products', type: 'array', description: 'List of matching products' },
      { name: 'total_results', type: 'integer', description: 'Total number of matching products' }
    ],
    endpoint: 'https://api.example.com/products/search',
    tags: ['e-commerce', 'search', 'products']
  },
  {
    intent_uid: 'example.com:get-product-details:v1',
    intent_name: 'GetProductDetails',
    description: 'Get detailed information about a specific product',
    input_parameters: [
      { name: 'product_id', type: 'string', required: true, description: 'Product ID' }
    ],
    output_parameters: [
      { name: 'product', type: 'object', description: 'Product details' }
    ],
    endpoint: 'https://api.example.com/products/details',
    tags: ['e-commerce', 'product', 'details']
  }
];

// Define policy
const policy = {
  '@context': 'http://www.w3.org/ns/odrl.jsonld',
  'uid': 'http://example.com/policy/12345',
  'type': 'Set',
  'profile': 'http://example.com/profile/odrl-uim',
  'permission': [
    {
      'target': 'http://example.com/api/intents',
      'action': 'execute',
      'constraint': [
        {
          'leftOperand': 'http://example.com/vocab/rateLimit',
          'operator': 'lte',
          'rightOperand': 1000,
          'unit': 'http://example.com/vocab/hour'
        }
      ],
      'duty': [
        {
          'action': 'pay',
          'target': 'http://example.com/vocab/intentPrice',
          'amount': 0.01,
          'unit': 'http://example.com/vocab/USD'
        }
      ]
    }
  ],
  'prohibition': [
    {
      'target': 'http://example.com/api/intents',
      'action': 'exceedRateLimit'
    }
  ],
  'obligation': [
    {
      'action': 'signPayload',
      'assignee': 'http://example.com/ai-agent/1',
      'target': 'http://example.com/vocab/payload',
      'constraint': [
        {
          'leftOperand': 'http://example.com/vocab/publicKey',
          'operator': 'use',
          'rightOperand': 'MIIBIjANBgkqh...'
        }
      ]
    }
  ]
};

// Create agents.json
const agentsJson = {
  'service-info': {
    'name': 'Example E-commerce Service',
    'description': 'Provides e-commerce functionalities',
    'service_url': 'https://api.example.com',
    'service_logo_url': 'https://example.com/logo.png',
    'service_terms_of_service_url': 'https://example.com/terms',
    'service_privacy_policy_url': 'https://example.com/privacy'
  },
  'intents': intents,
  'uim-public-key': publicKey,
  'uim-policy-file': 'https://example.com/uim-policy.json',
  'uim-api-discovery': 'https://api.example.com/uim/intents/search',
  'uim-compliance': {
    'standards': ['ISO27001', 'GDPR'],
    'regional-compliance': {
      'EU': 'GDPR',
      'US-CA': 'CCPA'
    },
    'notes': 'Data is encrypted in transit and at rest.'
  }
};

// Ensure public directory exists
if (!fs.existsSync('public')) {
  fs.mkdirSync('public');
}

// Save agents.json
fs.writeFileSync('public/agents.json', JSON.stringify(agentsJson, null, 2));

// Create Express app
const app = express();
app.use(express.json());
app.use(express.static('public'));

// Intent search endpoint
app.get('/uim/intents/search', (req, res) => {
  const { query, tags, intent_name, uid, namespace, description } = req.query;
  
  // Filter intents based on query parameters
  let filteredIntents = [...intents];
  
  if (query) {
    const queryLower = query.toLowerCase();
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_name.toLowerCase().includes(queryLower) ||
      intent.description.toLowerCase().includes(queryLower)
    );
  }
  
  if (tags) {
    const tagList = tags.split(',');
    filteredIntents = filteredIntents.filter(intent => 
      tagList.some(tag => intent.tags.includes(tag))
    );
  }
  
  if (intent_name) {
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_name.toLowerCase() === intent_name.toLowerCase()
    );
  }
  
  if (uid) {
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_uid === uid
    );
  }
  
  if (namespace) {
    filteredIntents = filteredIntents.filter(intent => 
      intent.intent_uid.split(':')[0] === namespace
    );
  }
  
  if (description) {
    const descLower = description.toLowerCase();
    filteredIntents = filteredIntents.filter(intent => 
      intent.description.toLowerCase().includes(descLower)
    );
  }
  
  // Pagination
  const page = parseInt(req.query.page) || 1;
  const pageSize = parseInt(req.query.page_size) || 10;
  const startIndex = (page - 1) * pageSize;
  const endIndex = startIndex + pageSize;
  const paginatedIntents = filteredIntents.slice(startIndex, endIndex);
  
  res.json({
    intents: paginatedIntents,
    pagination: {
      total_results: filteredIntents.length,
      total_pages: Math.ceil(filteredIntents.length / pageSize),
      current_page: page,
      page_size: pageSize
    }
  });
});

// Intent details endpoint
app.get('/uim/intents/:intent_uid', (req, res) => {
  const intent = intents.find(i => i.intent_uid === req.params.intent_uid);
  
  if (!intent) {
    return res.status(404).json({
      error: {
        code: 'NOT_FOUND',
        message: `The intent '${req.params.intent_uid}' was not found.`
      }
    });
  }
  
  res.json(intent);
});

// Policy endpoint
app.get('/uim-policy.json', (req, res) => {
  res.json(policy);
});

// PAT issuance endpoint
app.post('/pat/issue', (req, res) => {
  const { agent_id, signed_policy, agent_public_key } = req.body;
  
  // Validate request
  if (!agent_id || !signed_policy || !agent_public_key) {
    return res.status(400).json({
      error: {
        code: 'INVALID_PARAMETER',
        message: 'Missing required parameters.'
      }
    });
  }
  
  try {
    // Verify the signature
    const policyJson = JSON.stringify(policy);
    const verifier = crypto.createVerify('SHA256');
    verifier.update(policyJson);
    const isValid = verifier.verify(
      agent_public_key,
      Buffer.from(signed_policy, 'hex')
    );
    
    if (!isValid) {
      return res.status(400).json({
        error: {
          code: 'INVALID_SIGNATURE',
          message: 'The signature is invalid.'
        }
      });
    }
    
    // Generate PAT
    const pat = {
      iss: 'example.com',
      sub: agent_id,
      exp: Math.floor(Date.now() / 1000) + 86400, // 24 hours
      nbf: Math.floor(Date.now() / 1000),
      jti: crypto.randomBytes(16).toString('hex'),
      scope: intents.map(intent => `${intent.intent_uid}:execute`),
      pol: 'https://example.com/uim-policy.json',
      lmt: {
        rate: 100,
        period: 3600
      }
    };
    
    // Sign PAT
    const token = jwt.sign(pat, privateKey, { algorithm: 'RS256' });
    
    res.json({
      'uim-pat': token,
      'expires_at': new Date(pat.exp * 1000).toISOString()
    });
  } catch (error) {
    console.error('Error issuing PAT:', error);
    res.status(500).json({
      error: {
        code: 'INTERNAL_SERVER_ERROR',
        message: 'An unexpected error occurred on the server.'
      }
    });
  }
});

// Intent execution endpoint
app.post('/uim/execute', (req, res) => {
  const { intent_uid, parameters } = req.body;
  
  // Validate request
  if (!intent_uid || !parameters) {
    return res.status(400).json({
      error: {
        code: 'INVALID_PARAMETER',
        message: 'Missing required parameters.'
      }
    });
  }
  
  // Verify PAT
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({
      error: {
        code: 'UNAUTHORIZED',
        message: 'Missing or invalid Authorization header.'
      }
    });
  }
  
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, publicKey, { algorithms: ['RS256'] });
    
    // Check if the PAT allows executing this intent
    if (!decoded.scope.includes(`${intent_uid}:execute`)) {
      return res.status(403).json({
        error: {
          code: 'FORBIDDEN',
          message: 'The PAT does not grant permission to execute this intent.'
        }
      });
    }
    
    // Check rate limit
    // In a real implementation, you would use a rate limiting library or database
    
    // Find the intent
    const intent = intents.find(i => i.intent_uid === intent_uid);
    if (!intent) {
      return res.status(404).json({
        error: {
          code: 'NOT_FOUND',
          message: `The intent '${intent_uid}' was not found.`
        }
      });
    }
    
    // Validate parameters
    for (const param of intent.input_parameters) {
      if (param.required && !parameters[param.name]) {
        return res.status(400).json({
          error: {
            code: 'INVALID_PARAMETER',
            message: `Missing required parameter: ${param.name}`
          }
        });
      }
    }
    
    // Execute the intent
    // In a real implementation, you would call your actual business logic here
    if (intent_uid === 'example.com:search-products:v1') {
      // Simulate a product search
      const products = [
        {
          id: '123',
          name: 'Laptop',
          price: 1000,
          description: 'A powerful laptop'
        }
      ];
      
      res.json({
        products,
        total_results: products.length
      });
    } else if (intent_uid === 'example.com:get-product-details:v1') {
      // Simulate getting product details
      res.json({
        product: {
          id: parameters.product_id,
          name: 'Laptop',
          price: 1000,
          description: 'A powerful laptop',
          specifications: {
            processor: 'Intel Core i7',
            memory: '16GB',
            storage: '512GB SSD'
          }
        }
      });
    } else {
      res.status(400).json({
        error: {
          code: 'INTENT_NOT_
