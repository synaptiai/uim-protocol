# UIM Protocol Terminology

This page provides definitions for key terms used in the UIM Protocol specification. Terms are organized by category for easy reference.

## Core Protocol Terms

### Intent
**Definition**: An action that can be performed by a web service, including metadata and parameters required for execution.
**Related Terms**: Intent UID, Intent Metadata, Parameters
**Example**: SearchProducts, GetProductDetails, PlaceOrder

### Web Service
**Definition**: A service that publishes its capabilities (intents) using the UIM Protocol.
**Related Terms**: Service Provider, API
**Example**: An e-commerce platform that exposes intents for searching products and placing orders.

### AI Agent
**Definition**: An application or service that uses intents to interact with web services.
**Related Terms**: Client, Consumer
**Example**: A shopping assistant that helps users find products across multiple e-commerce platforms.

### Policy Adherence Token (PAT)
**Definition**: A token issued by a web service to an AI agent, encapsulating permissions, usage limits, and billing agreements.
**Related Terms**: ODRL Policy, UIM License
**Example**: A JWT token containing permissions and rate limits.

## Intent-Related Terms

### Intent UID
**Definition**: A unique identifier for an intent, following the format `namespace:intent_name:version`.
**Related Terms**: Intent, Namespace
**Example**: `ecommerce.com:SearchProducts:v1`

### Intent Metadata
**Definition**: Descriptive information about an intent, including its name, description, and category.
**Related Terms**: Intent, Tags
**Example**: Name: "SearchProducts", Description: "Search for products based on criteria", Tags: ["e-commerce", "search"]

### Parameters
**Definition**: Inputs required by an intent to perform its action, including name, type, and whether they are required.
**Related Terms**: Intent, Input Parameters, Output Parameters
**Example**: `query`, `category`, `price_range`

### Input Parameters
**Definition**: Parameters that are provided by the AI agent to the web service when executing an intent.
**Related Terms**: Parameters, Intent
**Example**: `query: "laptop"`, `category: "electronics"`

### Output Parameters
**Definition**: Parameters that are returned by the web service to the AI agent after executing an intent.
**Related Terms**: Parameters, Intent
**Example**: `products: [...]`, `total_results: 42`

### Endpoint
**Definition**: The API endpoint where an intent can be executed.
**Related Terms**: API, URL
**Example**: `https://api.ecommerce.com/products/search`

## Policy-Related Terms

### ODRL Policy
**Definition**: A policy expressed using the Open Digital Rights Language (ODRL) that defines permissions, prohibitions, and obligations.
**Related Terms**: Permission, Prohibition, Obligation
**Example**: A policy that allows executing intents with a rate limit of 1000 requests per hour.

### UIM License
**Definition**: A set of rules and conditions that govern the usage of data returned by an intent, including permissions, prohibitions, and obligations.
**Related Terms**: ODRL Policy, PAT
**Example**: `UIM-BY-NC-v1.0` - A license that allows non-commercial use with attribution.

### Permission
**Definition**: An allowed action specified in a policy.
**Related Terms**: ODRL Policy, Prohibition, Obligation
**Example**: Permission to execute an intent with a rate limit of 1000 requests per hour.

### Prohibition
**Definition**: A disallowed action specified in a policy.
**Related Terms**: ODRL Policy, Permission, Obligation
**Example**: Prohibition against exceeding the rate limit.

### Obligation
**Definition**: An action that must be performed as a condition of using a service.
**Related Terms**: ODRL Policy, Permission, Prohibition
**Example**: Obligation to pay for intent execution.

## Discovery-Related Terms

### Discovery Endpoint
**Definition**: The API endpoint where AI agents can query for available intents.
**Related Terms**: Intent, API Endpoint
**Example**: `/api/intents/search`

### DNS TXT Record
**Definition**: A DNS record that contains text information, used in the UIM Protocol to provide discovery information.
**Related Terms**: agents.json
**Example**: `uim-agents-file=https://example.com/agents.json`

### agents.json
**Definition**: A JSON file that contains information about a web service and its available intents.
**Related Terms**: DNS TXT Record, Intent
**Example**: A file containing service information, intents, and policy information.

## Security-Related Terms

### Authentication
**Definition**: The process of verifying the identity of an AI agent.
**Related Terms**: Authorization, PAT
**Example**: Using a PAT to authenticate an AI agent.

### Authorization
**Definition**: The process of determining whether an authenticated AI agent has permission to perform a specific action.
**Related Terms**: Authentication, Permission
**Example**: Checking if an AI agent has permission to execute a specific intent.

### Digital Signature
**Definition**: A cryptographic mechanism used to verify the authenticity and integrity of data.
**Related Terms**: Public Key, Private Key
**Example**: Signing a policy with a private key to prove agreement.

## Architecture-Related Terms

### Centralized Architecture
**Definition**: An architecture where a central repository manages intent registration, discovery, and execution.
**Related Terms**: Decentralized Architecture, Hybrid Approach
**Example**: A central repository that manages intents from multiple web services.

### Decentralized Architecture
**Definition**: An architecture where AI agents interact directly with web services without a central intermediary.
**Related Terms**: Centralized Architecture, Hybrid Approach
**Example**: AI agents discovering web services through DNS TXT records and interacting directly with them.

### Hybrid Approach
**Definition**: An architecture that combines elements of centralized and decentralized architectures.
**Related Terms**: Centralized Architecture, Decentralized Architecture
**Example**: Centralized discovery with decentralized execution.

## Implementation-Related Terms

### Execution Endpoint
**Definition**: The API endpoint where AI agents can execute intents.
**Related Terms**: Intent, API Endpoint
**Example**: `/api/intents/execute`

### Rate Limit
**Definition**: A limit on the number of requests an AI agent can make to a web service within a specific time period.
**Related Terms**: PAT, Policy
**Example**: 1000 requests per hour.

### Billing Information
**Definition**: Information about the cost of executing intents and payment methods.
**Related Terms**: PAT, Policy
**Example**: $0.01 per intent execution.

## Data-Related Terms

### Data Minimization
**Definition**: The principle of collecting and storing only the data necessary for the intended purpose.
**Related Terms**: Privacy, Security
**Example**: Designing intents to require only the minimum necessary parameters.

### Anonymization
**Definition**: The process of removing personally identifiable information from data.
**Related Terms**: Privacy, Security
**Example**: Removing user IDs and email addresses from data returned by intents.

### Data Retention
**Definition**: The period of time for which data is stored before being deleted.
**Related Terms**: Privacy, Security
**Example**: Storing data for 30 days before deleting it.
