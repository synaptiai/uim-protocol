
--------------------------------------------------------------------------------

### File: README.md
```
Path: README.md
Size: 48.11 KB
Last Modified: 2024-09-30 21:04:55
```

**Contents:**
```
<div style="text-align: center;">
  <img src="images/logo.png" alt="logo" width="100" height="100">
</div>

# The Unified Intent Mediator Protocol

## Getting started

1. Get familiar with the [concepts and motivations](uim-concept.md) behind the UIM protocol or just read the specification below.
2. Dive into the [technical exploration](uim-technical-exploration.md) of the UIM protocol to understand and explore the details and technical choices behind the protocol.
3. Explore the [prototypes implementations](uim-prototypes-intro.md) to see the UIM protocol in action (WIP)

## Get Involved: We Need Your Feedback

We’re inviting developers, AI providers, service operators, and tech/AI enthusiasts to review the draft specification, test the implementation, and share feedback. Your input is crucial to refining and improving the protocol.

### How to Contribute

1. Review the Draft Proposal: Check out the draft specification and explore the protocol’s design and implementation.
2. Join the Discussion: Start a conversation in the Discussions tab. We’d love to hear your thoughts on the protocol’s design, potential use cases, or any concerns.
3. Raise Issues: Found a bug or have suggestions? Open an Issue to let us know or contribute directly by submitting a Pull Request. See our [Contributing Guidelines](CONTRIBUTING.md) for more information.
4. Share the Word: Help us spread the word about the UIM protocol by sharing this repository with your network. Write a blog post, tweet, or share the project with your colleagues. We appreciate your support!

---

## Protocol Draft Proposal

**Date:** September 30, 2024 - **Version:** 0.2

## Abstract

The Unified Intent Mediator (UIM) protocol defines a standardized framework for AI agents to interact with web services through well-defined intents, metadata, and execution methods. By introducing consistency and security in these interactions, UIM enhances efficiency, scalability, and reliability for AI-driven applications. This specification provides comprehensive guidelines for implementing the UIM protocol, ensuring interoperability, security, and compliance across different systems.

Key components include:

- **Intents**: Structured actions that web services can expose, defining specific tasks such as searching products, placing orders, or retrieving data. Each intent has a unique identifier, metadata, and required parameters.

- **Metadata and Parameters**: Each intent comes with metadata (name, description, category) and defined parameters, providing context and specific input requirements.

- **Policy Adherence Tokens (PATs)**: Digitally signed tokens issued by web services that encapsulate permissions, billing, and compliance rules, streamlining policy enforcement and automating billing.

- **Discovery and Execution APIs**: AI agents can query discovery APIs to find available intents and use execution APIs to perform actions. Execution involves validation, interaction with the service’s API, response formatting, and error handling.

- **DNS TXT Records and agents.json Files**: Innovative methods for endpoint discovery, allowing AI agents to find and authenticate API endpoints using familiar internet protocols.

- **Integration with Open Digital Rights Language (ODRL)**: Provides a structured approach to managing permissions, prohibitions, and obligations, ensuring clear and enforceable rules between AI agents and web services.

- **UIM Licensing Scheme**: An alternative method to the ODRL (Open Digital Rights Language) policy for defining the permissions, conditions, and prohibitions for data returned by web services. It specifies the license under which the data returned by intents can be used according to the [UIM Licensing Scheme](uim-licensing-scheme.md).

## Table of Contents

1. [Introduction](#1-introduction)
   - [1.1 Motivation](#11-motivation)
   - [1.2 Scope](#12-scope)
   - [1.3 Out of Scope](#13-out-of-scope)
2. [Terminology](#2-terminology)
3. [Key Concepts](#3-key-concepts)
   - [3.1 Intents](#31-intents)
   - [3.2 Metadata and Parameters](#32-metadata-and-parameters)
   - [3.3 The Execute Method](#33-the-execute-method)
   - [3.4 Policy Adherence Tokens (PATs)](#34-policy-adherence-tokens-pats)
   - [3.5 AI Agents](#35-ai-agents)
4. [System Architecture](#4-system-architecture)
   - [4.1 Centralized Architecture](#41-centralized-architecture)
   - [4.2 Decentralized Architecture](#42-decentralized-architecture)
   - [4.3 Hybrid Approach](#43-hybrid-approach)
5. [Core Components](#5-core-components)
   - [5.1 Intent Discovery and Execution Endpoints](#51-intent-discovery-and-execution-endpoints)
   - [5.2 Unique Intent Identifier (UID) Format](#52-unique-intent-identifier-uid-format)
   - [5.3 Intent Metadata](#53-intent-metadata)
   - [5.4 Discovery Through DNS TXT Records and `agents.json` Files](#54-discovery-through-dns-txt-records-and-agentsjson-files)
   - [5.5 Policy Adherence Tokens (PATs) and ODRL Integration](#55-policy-adherence-tokens-pats-and-odrl-integration)
   - [5.6 Incorporating Billing Information into PATs](#56-incorporating-billing-information-into-pats)
   - [5.7 Policy Adherence Tokens (PATs) and UIM Policy Scheme Integration](#57-policy-adherence-tokens-pats-and-uim-policy-scheme-integration)
   - [5.8 Service Management APIs](#58-service-management-apis)
   - [5.9 Intent Management APIs](#59-intent-management-apis)
6. [General API Guidelines and Standards](#6-general-api-guidelines-and-standards)
   - [6.1 Pagination](#61-pagination)
   - [6.2 Security and Compliance](#62-security-and-compliance)
   - [6.3 Monitoring and Analytics](#63-monitoring-and-analytics)
   - [6.4 Scalability](#64-scalability)
   - [6.5 Error Management Strategy](#65-error-management-strategy)
7. [Practical Examples and Use Cases](#7-practical-examples-and-use-cases)
   - [7.1 E-commerce Platform Integration](#71-e-commerce-platform-integration)
   - [7.2 Real Estate Data Retrieval](#72-real-estate-data-retrieval)
8. [Security Considerations](#8-security-considerations)
9. [Privacy Considerations](#9-privacy-considerations)
10. [Appendix](#10-appendix)
    - [A. Standard Error Codes and Messages](#a-standard-error-codes-and-messages)
    - [B. Complete `agents.json` File Example](#b-complete-agentsjson-file-example)
    - [C. Sample ODRL Policy](#c-sample-odrl-policy)
    - [D. Sample PAT Structure](#d-sample-pat-structure)
    - [E. Sample API Requests and Responses](#e-sample-api-requests-and-responses)
    - [F. High Level System Architecture Diagram](#f-high-level-system-architecture-diagram)

## 1. Introduction

![Abstract UIM architecture](images/abstract.png)

### 1.1 Motivation

As Artificial Intelligence (AI) technology advances, there is a growing need for efficient, standardized interactions between AI agents and web services. Traditional methods such as web scraping and simulated user interactions are inefficient, unreliable, and often non-compliant with legal and ethical standards.

#### Challenges in Current AI-Agent Interactions

1. **Web Scraping Issues**
   - **Inconsistency**: Unpredictable changes in HTML structures lead to data extraction failures.
   - **Legal and Ethical Concerns**: Potential violations of terms of service and data privacy laws.

2. **Simulated Browser Interactions**
   - **Performance Overhead**: High resource consumption affects scalability.
   - **Dynamic Content Handling**: Difficulty managing JavaScript-rendered content, pop-ups, and CAPTCHAs.

3. **Lack of Standardization**
   - **Diverse APIs**: Inconsistent API designs require custom integrations.
   - **Data Formats**: Multiple data formats necessitate different parsers.

4. **Limited Access to Deep Functionality**
   - **Restricted Features**: Inability to access advanced functionalities due to API and/or data limitations.
   - **Inefficient Automation**: Hinders the development of sophisticated AI capabilities.

5. **Security and Compliance Challenges**
   - **Complex Authentication**: Varied authentication mechanisms complicate integration.
   - **Regulatory Compliance**: Navigating data protection laws like GDPR or copyright issues is challenging.

![Challenges in AI-Agent interactions with web services](images/challenges-spec.png)

### 1.2 Scope

The Unified Intent Mediator (UIM) protocol addresses these challenges by introducing a standardized, secure method for direct AI agent-web service interaction. This specification aims to:

- **Define the structure and format of intents.**
- **Establish mechanisms for discovery and execution of intents.**
- **Integrate Open Digital Rights Language (ODRL) for policy management.**
- **Utilize Policy Adherence Tokens (PATs) for secure interactions.**
- **Provide comprehensive guidelines for implementation, ensuring interoperability and compliance.**

### 1.3 Out of Scope

While the Unified Intent Mediator (UIM) Protocol Specification aims to provide a comprehensive framework for AI agents to interact with web services, certain aspects are intentionally excluded to maintain focus and clarity. The following elements are not within the scope of this specification in its current version:

- **Implementation Details of AI Agents and Web Services**: The specification does not dictate the internal architecture or programming paradigms (e.g., object-oriented, functional programming) that AI agents or web services should adopt. It does not prescribe specific programming languages, frameworks, or libraries to be used in implementing the protocol.
- **Specific Authentication and Authorization Mechanisms**: Details regarding how credentials are stored, rotated, or managed are beyond the scope of this document.
- **Legal and Regulatory Compliance Beyond Data Privacy**: The specification does not cover compliance with laws beyond data privacy regulations like GDPR and CCPA. It excludes areas such as export controls, accessibility laws, and sector-specific regulations (e.g., HIPAA for healthcare). Issues related to copyright, trademarks, or patents are not addressed.
- **User Interface and Experience Design**: The specification does not prescribe how users should interact with AI agents or how agents present information to users.
- **Business Models and Economic Considerations**: While incorporating billing information into PATs is discussed, the specification does not guide on how services should price their intents or services. The specifics of service-level agreements (SLAs), terms of service (ToS), or contractual obligations beyond what’s included in ODRL policies are not covered.
- **Security Threat Modeling and Mitigation Techniques**: While high-level security considerations are included, specific threat models, vulnerability assessments, or detailed mitigation strategies (e.g., against SQL injection, cross-site scripting) are not.
- **Detailed Workflow Implementations**: It does not delve into the specific business logic that should be implemented within intents. Detailed workflows or sequence diagrams for complex processes are not provided beyond high-level overviews.

## 2. Terminology

- **Intent**: An action that can be performed by a web service, including metadata and parameters required for execution.  
- **Parameters**: Inputs required by an intent to perform its action, including name, type, and whether they are required.  
- **Service**: A web service that publishes its capabilities (intents) using the UIM protocol.  
- **Endpoint**: The API endpoint where an intent can be executed.  
- **Metadata**: Descriptive information about an intent, including its name, description, and category.
- **Policy Adherence Token (PAT)**: A token issued by a web service to an AI agent, encapsulating permissions, usage limits, and billing agreements.
- **AI Agent**: An application or service that uses intents to interact with web services.
- **Discovery Endpoint**: The API endpoint where AI agents can query for available intents.
- **Execution Endpoint**: The API endpoint where AI agents can execute intents.
- **Policy Endpoint**: The API endpoint where AI agents can request PATs from web services.
- **Open Digital Rights Language (ODRL)**: A standardized language for expressing policies governing the usage of digital content and services.
- **UIM License**: A set of rules and conditions that govern the usage of data returned by an intent, including permissions, prohibitions, and obligations.

## 3. Key Concepts

### 3.1 Intents

**Definition**: Intents are predefined actions that an AI agent can perform on a web service. They encapsulate specific tasks, including necessary parameters and execution details.

**Examples**:

- **SearchProducts**
- **GetProductDetails**
- **PlaceOrder**

#### Unique Intent Identifier (UID) Format

The UID ensures that AI agents can uniquely identify and call intents from different service providers.

**Format**:

```js
namespace:intent_name:version
```

- **namespace**: Typically the domain or unique identifier of the service provider.
- **intent_name**: A descriptive and unique name within the namespace.
- **version**: Indicates the version of the intent.

**Examples**:

- `ecommerce.com:SearchProducts:v1`
- `weather.com:GetForecast:v2`

### 3.2 Metadata and Parameters

Each intent includes:

- **Metadata**: Name, description, category, and tags.
- **Input Parameters**: Required to execute the intent.
- **Output Parameters**: Expected results from the intent execution.

![Intent](images/intent-format.png)

**Example**:

```json
{
  "intent_uid": "ecommerce.com:SearchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on criteria",
  "input_parameters": [
    {"name": "query", "type": "string", "required": true, "description": "Search term"},
    {"name": "category", "type": "string", "required": false, "description": "Product category"},
    {"name": "price_range", "type": "string", "required": false, "description": "Price range filter"},
    {"name": "sort_by", "type": "string", "required": false, "description": "Sorting criteria"}
  ],
  "output_parameters": [
    {"name": "products", "type": "array", "description": "List of products"},
    {"name": "total_results", "type": "integer", "description": "Total number of results"}
  ],
  "endpoint": "https://api.ecommerce.com/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

### 3.3 The Execute Method

Responsible for:

1. **Input Validation**: Ensuring all required parameters are present and correctly formatted.
2. **Authentication**: Verifying the AI agent's identity and PAT.
3. **Authorization**: Ensuring the AI agent has the necessary permissions as per the PAT and policies.
4. **Execution**: Performing the action defined by the intent.
5. **Response Formatting**: Standardizing the response for consistent interpretation by AI agents.
6. **Error Handling**: Managing exceptions and providing meaningful feedback.

![The execution method](images/execute-method.png)

### 3.4 Policy Adherence Tokens (PATs)

**Definition**: Digitally signed tokens that encapsulate permissions, usage limits, billing agreements, and compliance terms. They ensure secure and compliant interactions between AI agents and web services.

### 3.5 AI Agents

**Definition**: Applications or services that utilize intents to interact with web services.

**Responsibilities**:

- **Discovery**: Finding available intents and services.
- **Policy Agreement**: Requesting and managing PATs.
- **Execution**: Performing intents according to policies.

![AI-agent responsibilities](images/ai-discovery.png)

## 4. System Architecture

### 4.1 Centralized Architecture

#### Overview

A central repository manages:

- **Intent Registration**: Web services register their intents with the central repository.
- **Discovery**: AI agents discover intents via the central system.
- **Execution**: AI agents execute intents through the central system, which forwards requests to the appropriate web service.
- **Policy Management**: Centralized issuance and validation of PATs.

#### Workflow Description

1. **Service Registration**: Web services register their intents and policies with the central repository.
2. **Intent Discovery**: AI agents query the central repository to discover available intents.
3. **Policy Agreement**: AI agents obtain PATs from the central repository after agreeing to policies.
4. **Execution**: AI agents execute intents via the central repository.
5. **Response Handling**: The central repository forwards responses from web services to AI agents.

![Centralized Architecture](images/central-arch.png)

#### Pros and Cons

- **Pros**:
  - Simplified discovery and integration for AI agents.
  - Unified policy enforcement and compliance management.
- **Cons**:
  - Single point of failure.
  - Scalability challenges with increasing load.
  - Potential bottleneck affecting performance.

### 4.2 Decentralized Architecture

#### Overview

AI agents interact directly with web services without a central intermediary.

#### Workflow Description

1. **Discovery via DNS TXT and `agents.json`**: AI agents discover web services through DNS records and retrieve `agents.json` files.
2. **Policy Retrieval and Agreement**: AI agents obtain ODRL policies and request PATs directly from web services.
3. **Intent Execution**: AI agents execute intents directly with web services using the obtained PATs.
4. **Response Handling**: Web services respond directly to AI agents.

![Decentralized Architecture](images/decentral-arch.png)

#### Pros and Cons

- **Pros**:
  - Enhanced scalability due to distributed interactions.
  - Greater control and autonomy for web services.
- **Cons**:
  - Increased complexity for AI agents managing diverse policies.
  - Potential inconsistencies in policy enforcement across services.

### 4.3 Hybrid Approach

#### Overview

Combines centralized discovery with decentralized execution and PAT issuance.

#### Workflow Description

1. **Centralized Discovery**: AI agents use the central repository to discover available intents and services.
2. **Decentralized Policy Agreement**: AI agents retrieve policies and obtain PATs directly from web services.
3. **Direct Execution**: AI agents execute intents directly with web services using the obtained PATs.
4. **Response Handling**: Web services respond directly to AI agents.

![Hybrid Approach](images/hybrid-arch.png)

#### Pros and Cons

- **Pros**:
  - Efficient discovery through a centralized system.
  - Maintains autonomy and control for web services in execution and policy management.
- **Cons**:
  - Coordination complexity between central and decentralized components.
  - Diverse compliance requirements increase AI agent complexity.

## 5. Core Components

### 5.1 Intent Discovery and Execution Endpoints

#### Purpose

Enable AI agents to:

- **Discover** available intents.
- **Execute** intents securely.

#### Implementation

- **Centralized Context**: Unified discovery endpoint managed by the central repository.
- **Decentralized Context**: Each web service hosts its own discovery and execution endpoints.
- **Hybrid Context**: Centralized discovery with decentralized execution endpoints.

#### API Endpoints

1. **Intent Discovery**

   - **Endpoint**: `/api/intents/search`
   - **Method**: `GET`
   - **Parameters**:
     - `query`: Natural language search term.
     - `service_name`
     - `intent_name`
     - `uid`
     - `namespace`
     - `description`
     - `tags`

   **Example Request**:

   ```curl
   GET /api/intents/search?intent_name=SearchProducts
   ```

   **Example Response**:

   ```json
   {
     "intents": [
       {
         "service_name": "E-commerce Platform",
         "intent_name": "SearchProducts",
         "intent_uid": "ecommerce.com:SearchProducts:v1",
         "description": "Search for products based on criteria",
         "input_parameters": [
           {"name": "query", "type": "string", "required": true}
         ],
         "output_parameters": [
           {"name": "products", "type": "array", "description": "List of products"}
         ],
         "endpoint": "https://api.ecommerce.com/products/search",
         "tags": ["e-commerce", "search", "products"]
       }
     ]
   }
   ```

2. **Execute Intent**

   - **Endpoint**: `/api/intents/execute`
   - **Method**: `POST`
   - **Headers**:
     - `Authorization`: Bearer PAT-12345
     - `Content-Type`: application/json

   **Example Request**:

   ```json
   POST /api/intents/execute
   Authorization: Bearer PAT-12345
   Content-Type: application/json

   {
     "intent_uid": "ecommerce.com:SearchProducts:v1",
     "parameters": {
       "query": "laptops"
     }
   }
   ```

   **Example Response**:

   ```json
   {
     "products": [
       {
         "product_id": "123",
         "name": "Gaming Laptop",
         "price": 1500
       },
       {
         "product_id": "124",
         "name": "Ultrabook",
         "price": 1200
       }
     ],
     "total_results": 2
   }
   ```

### 5.2 Unique Intent Identifier (UID) Format

As detailed in [Section 3.1](#31-intents), the UID format is crucial for unique identification.

### 5.3 Intent Metadata

Metadata provides detailed information about an intent, helping AI agents understand how to interact with it.

**Fields**:

- `intent_uid`
- `intent_name`
- `description`
- `input_parameters`
- `output_parameters`
- `endpoint`
- `tags`
- `service_info`

### 5.4 Discovery Through DNS TXT Records and `agents.json` Files

#### Purpose

Facilitate service discovery in a decentralized architecture.

#### DNS TXT Records

Provide quick discovery of services and pointers to detailed information.

**Fields**:

1. **uim-agents-file**: URL of the `agents.json` file.
2. **uim-api-discovery**: URL of the API discovery endpoint.
3. **uim-policy-file**: URL of the ODRL policy file.
4. **uim-license**: The UIM license for the service.

**Example Record**:

```txt
uim-agents-file=https://example.com/agents.json
uim-api-discovery=https://api.example.com/intents/search
uim-policy-file=https://example.com/uim-policy.json
uim-license=https://uimprotocol.com/licenses/uim-by-nc-v1.0
```

#### `agents.json` Files

Contain detailed information about the service and available intents.

**Structure**:

- **service-info**
- **intents**
- **uim-public-key**
- **uim-policy-file**
- **uim-api-discovery**
- **uim-compliance**
- **uim-license**

**Complete `agents.json` File Example** is provided in [Appendix B](#b-complete-agentsjson-file-example).

### 5.5 Policy Adherence Tokens (PATs) and ODRL Integration

#### Purpose

Ensure secure, compliant interactions by encapsulating policies, permissions, and obligations.

#### ODRL Integration

Utilize the **Open Digital Rights Language (ODRL)** to define policies. A comprehensive [ODRL vocabulary draft document](uim-odrl-vocab.md) is provided for the UIM protocol namespace. It defines namespaces, vocabulary terms, JSON-LD context, and policy examples. It also includes recommendations for implementers and references for further reading.

**Key Concepts**:

- **Policy**: Represents the agreement between AI agents and web services, detailing permissions, prohibitions, and obligations.
- **Permission**: Specifies allowed actions for AI agents.
- **Prohibition**: Specifies actions that AI agents are not allowed to perform.
- **Obligation**: Specifies actions that AI agents must perform under certain conditions.
- **Asset**: The resource or service the policy applies to.
- **Party**: The entities involved in the policy (e.g., AI agents and web services).

**Sample ODRL Policy** is provided in [Appendix C](#c-sample-odrl-policy).

#### PAT Issuance Workflow with ODRL policies

1. **Policy Retrieval and Agreement**:
   - AI agent retrieves the ODRL policy from the specified endpoint.
   - AI agent digitally signs the policy using its private key and sends it to the web service alongside its public key to request a PAT.

2. **PAT Issuance**:
   - Web service verifies the AI agent's signature and agreement.
   - Web service issues a PAT, which includes the agreed policy details, permissions, obligations, and a validity period.
   - The PAT is digitally signed by the web service.

3. **Using PAT in Requests**:
   - AI agent includes the PAT in the `Authorization` header of each request.
   - Web service verifies the PAT's signature and validity before processing the request.

**PAT Structure**:

**Sample PAT** is provided in [Appendix D](#d-sample-pat-structure).

#### Including PAT in Requests

The AI agent includes the PAT in the `Authorization` header:

```txt
Authorization: Bearer PAT-12345
```

#### Verification Process

1. **Extract PAT**: Web service extracts the PAT from the request header.
2. **Verify Signature**: Web service verifies the PAT's signature using its public key.
3. **Check Validity**: Web service checks the PAT's validity period.
4. **Authorize Request**: Web service checks if the PAT permissions match the requested action.
5. **Process Request**: If valid, the web service processes the request; otherwise, it rejects it.

### 5.6 Incorporating Billing Information into PATs

#### Purpose

Simplifies transactions by including billing details within the PAT.

#### Workflow

1. **Billing Information Submission**: AI agent submits billing info during PAT request.
2. **PAT Issuance**: PAT includes the agreed policy details, permissions, obligations, and a validity period.
3. **Automated Billing**: Web service processes payments automatically as intents are executed.

**Benefits**:

- Streamlined process.
- Automated billing.
- Improved user experience.
- Enhanced compliance.

### 5.7 Policy Adherence Tokens (PATs) and UIM Policy Scheme Integration

#### Purpose

The [UIM Licensing Scheme](uim-licensing-scheme.md) aims to standardize how licensing information is conveyed in the agents.json file, providing a clear, machine-readable format that AI agents can interpret to understand the legal and commercial restrictions around data usage. It simplifies the licensing process and offers web services a straightforward way to communicate their terms without the need to define a complete ODRL policy.

#### PAT Issuance Workflow with UIM Licenses

Web services can provide a custom license using the `uim-license` property, which allows them to define permissions, conditions, and restrictions in a simplified manner, tailored to their specific needs. AI agents can then interpret this license to understand the terms and conditions of data usage.

When an AI agent interacts with a web service, it should first check for a `uim-license`. If both the uim-license property and an ODRL policy are specified, the ODRL policy takes precedence for defining permissions, prohibitions, and obligations.

1. **License Retrieval and Agreement**:
   - **AI Agent retrieves the UIM license** from the specified endpoint or resource metadata (e.g., `agents.json`).
   - **AI Agent notes the license reference**, including:
     - **License Code** (e.g., `UIM-BY-NC-v1.0`).
     - **License URL** (e.g., `https://uimprotocol.com/licenses/uim-by-nc-v1.0`).
   - **AI Agent prepares an authorization request** that refers directly to the license:
     - **License Reference**: Includes the license URL.
     - **Agreement Assertion**: Indicates agreement to comply with the entire license.
     - **Digital Signature (Optional)**: May digitally sign the license reference to confirm agreement and authenticity.

2. **PAT Issuance**:
   - **Authorization Server evaluates the AI Agent's request**:
     - **Verifies the license reference** is valid and recognized.
     - **Confirms the agent's agreement** to comply with the license.
     - **No need for detailed scopes and claims**: The license itself defines the permissions, conditions, and prohibitions.
   - **Authorization Server issues a PAT**, which includes:
     - **License Reference**: The license URL of the agreed-upon license.
     - **Validity Period**: Specifies how long the PAT is valid.
     - **Token Signature**: The PAT is digitally signed by the authorization server to ensure integrity and authenticity.

3. **Using PAT in Requests**:
   - **AI Agent includes the PAT** in the `Authorization` header of each request to the web service:
  
     ```http
     Authorization: Bearer <PAT_token>
     ```

   - **Web Service verifies the PAT's signature and validity** before processing each request:
     - **Validates the token's signature** to confirm it was issued by the trusted authorization server.
     - **Checks the token's expiration** to ensure it is still valid.
     - **Retrieves the license reference** from the PAT and verifies it is still valid and recognized. If not, the web service may reject the request.
   - **Web Service processes the request** if the PAT is valid.

**Notes**:

- **Optional Digital Signature**: While not required in this flow, the agent may digitally sign the policy reference or the authorization request to provide an additional layer of assurance regarding the agent's identity and agreement.

- **Dynamic Licenses**: If license are subject to change, the license reference should include a version number or timestamp to ensure both parties are referencing the same license terms.

### 5.8 Service Management APIs

APIs that allow web services to manage their registration, including creating, updating, and deleting services. Used in the centralized architecture.

#### Register Service

- **Endpoint**: `/api/services`
- **Method**: `POST`
- **Description**: Registers a new service.

**Request Body**:

```json
{
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities",
  "service_terms_of_service_url": "https://api.ecommerce.com/terms",
  "service_privacy_policy_url": "https://api.ecommerce.com/privacy",
  "service_logo_url": "https://api.ecommerce.com/logo.png"
}
```

#### Update Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: `PUT`
- **Description**: Updates an existing service.

#### Delete Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: `DELETE`
- **Description**: Deletes a registered service.

#### Retrieve Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: `GET`
- **Description**: Retrieves the details of a registered service.

### 5.9 Intent Management APIs

APIs for web services to manage their intents. Used in the centralized architecture.

#### List All Intents for a Service

- **Endpoint**: `/api/services/{service_id}/intents`
- **Method**: `GET`
- **Description**: Lists all intents for a specific service.

#### Retrieve Intent Details

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific intent.

#### Create Intent

- **Endpoint**: `/api/services/{service_id}/intents`
- **Method**: `POST`
- **Description**: Creates a new intent for a service.

**Request Body**:

```json
{
  "intent_uid": "ecommerce.com:GetProductDetails:v1",
  "intent_name": "GetProductDetails",
  "description": "Fetches detailed information about a specific product using its unique identifier",
  "input_parameters": [
    {"name": "product_id", "type": "string", "required": true}
  ],
  "output_parameters": [
    {"name": "product_details", "type": "object", "required": true}
  ],
  "endpoint": "https://api.ecommerce.com/products/details",
  "tags": ["e-commerce", "product", "details"]
}
```

#### Update Intent

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: `PUT`
- **Description**: Updates the details of an existing intent.

#### Delete Intent

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: `DELETE`
- **Description**: Deletes an existing intent.

## 6. General API Guidelines and Standards

### 6.1 Pagination

To handle large data sets, list endpoints support pagination.

#### Parameters

- **page**: Page number (default: 1).
- **page_size**: Items per page (default: 10).

**Example Request**:

```curl
GET /api/services/12345/intents?page=2&page_size=5
```

#### Response Headers

- **X-Total-Count**
- **X-Total-Pages**
- **X-Current-Page**
- **X-Page-Size**

### 6.2 Security and Compliance

- **Authentication**: Use OAuth 2.0 for secure authentication.
- **Encryption**: All communications MUST use HTTPS.
- **Compliance**: Adhere to regulations like GDPR and CCPA.
- **Data Protection**: Implement data encryption at rest and in transit.

### 6.3 Monitoring and Analytics

- **Real-time Monitoring**: Provide dashboards for API usage and performance.
- **Logging and Alerts**: Implement systems to track activity and respond to issues.
- **Audit Trails**: Maintain logs for compliance and troubleshooting.

### 6.4 Scalability

- **Caching**: Implement caching mechanisms for frequently accessed data.
- **Load Balancing**: Distribute traffic efficiently to handle high volumes.
- **Auto-scaling**: Utilize auto-scaling to adjust resources based on demand.

### 6.5 Error Management Strategy

#### Comprehensive Error Handling Approach

- **Layered Error Handling**:
  1. **Client-Side Errors (4xx)**: Issues with the client's request.
  2. **Server-Side Errors (5xx)**: Issues on the server side.
  3. **Protocol-Level Errors**: Specific to UIM protocol operations.

#### Standard Error Response Structure

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Descriptive error message.",
    "details": {
      "additional": "context-specific information"
    }
  }
}
```

**Detailed error codes and messages** are provided in [Appendix A](#a-standard-error-codes-and-messages).

#### Error Handling Guidelines

- **Consistent Structure**: Ensure all error responses follow the standard format.
- **Clear Messages**: Provide descriptive and actionable error messages.
- **Security Considerations**: Avoid exposing sensitive internal details.
- **Documentation**: Document all error codes and scenarios.

## 7. Practical Examples and Use Cases

### 7.1 E-commerce Platform Integration

**Scenario**: An AI shopping assistant helps users find products across multiple e-commerce platforms.

**Workflow**:

1. **Discovery**: The AI agent searches for the `SearchProducts` intent across registered e-commerce services.
2. **Policy Agreement**: The agent retrieves the ODRL policy and obtains a PAT from each service.
3. **Execution**: The agent executes the `SearchProducts` intent with user-provided criteria.
4. **Aggregation**: Results from multiple platforms are aggregated and presented to the user.
5. **Purchase**: The user selects a product, and the agent uses the `PlaceOrder` intent to complete the purchase.

![Ecommerce Example](images/ecommerce-example.png)

**Benefits**:

- **User Convenience**: One-stop shop across multiple platforms.
- **Service Monetization**: E-commerce platforms gain additional sales channels.

### 7.2 Real Estate Data Retrieval

**Scenario**: A real estate analytics tool aggregates property data for market analysis.

**Workflow**:

1. **Discovery**: The AI agent discovers real estate services offering the `SearchProperty` intent.
2. **Policy Agreement**: The agent agrees to policies and obtains PATs.
3. **Data Retrieval**: Executes `SearchProperty` intents to gather property listings.
4. **Analysis**: Aggregates and analyzes data to provide market insights.
5. **Compliance**: Ensures data usage complies with service policies.

![Real Estate Example](images/realestate-example.png)

**Benefits**:

- **Comprehensive Data**: Access to diverse property listings.
- **Enhanced Analytics**: Improved market analysis capabilities.

## 8. Security Considerations

- **Authentication and Authorization**: AI agents MUST authenticate using secure methods like OAuth 2.0. Web services MUST verify PATs and ensure that AI agents have the necessary permissions.
- **Data Integrity**: All tokens and sensitive data SHOULD be digitally signed to prevent tampering.
- **Confidentiality**: Sensitive information, including billing details, MUST be encrypted and securely stored.
- **Replay Attacks**: PATs SHOULD include nonce values or timestamps to prevent replay attacks.
- **Input Validation**: Web services MUST validate all inputs to prevent injection attacks.

## 9. Privacy Considerations

- **Data Minimization**: AI agents and web services SHOULD minimize the collection and storage of personal data.
- **Compliance**: Adherence to regulations like GDPR and CCPA is REQUIRED where applicable.
- **User Consent**: When personal data is involved, explicit user consent MUST be obtained.
- **Transparency**: Privacy policies SHOULD be clearly communicated through the `service_privacy_policy_url`.
- **Anonymization**: Where possible, data SHOULD be anonymized to protect user identities.

## 10. Appendix

### A. Standard Error Codes and Messages

#### Client-Side Errors (4xx)

| Error Code             | Message                                                    | Description                                |
|------------------------|------------------------------------------------------------|--------------------------------------------|
| INVALID_PARAMETER      | "The parameter '{param}' is required."                     | Missing or invalid parameter.              |
| UNAUTHORIZED           | "Unauthorized access. Authentication is required."         | Missing or invalid authentication token.   |
| FORBIDDEN              | "Access to this resource is forbidden."                    | Insufficient permissions.                  |
| NOT_FOUND              | "The requested resource '{resource}' was not found."       | Resource not found.                        |
| METHOD_NOT_ALLOWED     | "The HTTP method '{method}' is not allowed for this endpoint." | Unsupported HTTP method.                   |
| CONFLICT               | "The request could not be completed due to a conflict."    | Resource conflict.                         |
| UNSUPPORTED_MEDIA_TYPE | "The media type '{type}' is not supported."                | Unsupported content type.                  |

#### Server-Side Errors (5xx)

| Error Code              | Message                                                   | Description                      |
|-------------------------|-----------------------------------------------------------|----------------------------------|
| INTERNAL_SERVER_ERROR   | "An unexpected error occurred on the server."             | Generic server error.            |
| SERVICE_UNAVAILABLE     | "The service is temporarily unavailable."                 | Server down or overloaded.       |
| GATEWAY_TIMEOUT         | "The server did not receive a timely response."           | Upstream server timeout.         |
| NOT_IMPLEMENTED         | "The requested functionality is not implemented."         | Feature not supported.           |

#### Protocol-Level Errors

| Error Code              | Message                                                   | Description                                |
|-------------------------|-----------------------------------------------------------|--------------------------------------------|
| INTENT_EXECUTION_FAILED | "The intent '{intent}' could not be executed."            | Execution failure due to various reasons.  |
| INTENT_NOT_SUPPORTED    | "The intent '{intent}' is not supported by this service." | Intent not recognized or supported.        |
| VERSION_CONFLICT        | "The intent version '{version}' is not supported."        | Version mismatch.                          |
| INTENT_DEPRECATED       | "The intent '{intent}' has been deprecated."              | Intent no longer available.                |

### B. Complete `agents.json` File Example

```json
{
  "service-info": {
    "name": "fakerealestate.com",
    "description": "Provides property listings and real estate data.",
    "service_url": "https://fakerealestate.com",
    "service_logo_url": "https://fakerealestate.com/logo.png",
    "service_terms_of_service_url": "https://fakerealestate.com/terms",
    "service_privacy_policy_url": "https://fakerealestate.com/privacy"
  },
  "intents": [
    {
      "intent_uid": "fakerealestate.com:SearchProperty:v1",
      "intent_name": "SearchProperty",
      "description": "Search properties based on criteria",
      "input_parameters": [
        {"name": "location", "type": "string", "required": true, "description": "City or ZIP code"},
        {"name": "min_price", "type": "integer", "required": false, "description": "Minimum price"},
        {"name": "max_price", "type": "integer", "required": false, "description": "Maximum price"},
        {"name": "property_type", "type": "string", "required": false, "description": "Type of property"}
      ],
      "output_parameters": [
        {"name": "properties", "type": "array", "description": "List of matching properties"},
        {"name": "total_results", "type": "integer", "description": "Total number of results"}
      ],
      "endpoint": "https://fakerealestate.com/api/execute/SearchProperty",
      "tags": ["real estate", "search"],
      "rate_limit": "1000/hour",
      "price": "0.01 USD"
    }
    // Additional intents can be added here
  ],
  "uim-public-key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQE...",
  "uim-policy-file": "https://fakerealestate.com/uim-policy.json",
  "uim-api-discovery": "https://fakerealestate.com/uim/intents/search",
  "uim-compliance": {
    "standards": ["ISO27001", "GDPR"],
    "regional-compliance": {
      "EU": "GDPR",
      "US-CA": "CCPA"
    },
    "notes": "Data is encrypted in transit and at rest."
  },
  "uim-license": "https://uimprotocol.com/licenses/uim-by-nc-v1.0"
}
```

### C. Sample ODRL Policy

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "uid": "http://fakerealestate.com/policy/12345",
  "type": "Set",
  "permission": [
    {
      "target": "http://fakerealestate.com/api/intents",
      "action": "execute",
      "constraint": [
        {
          "leftOperand": "http://fakerealestate.com/vocab/rateLimit",
          "operator": "lte",
          "rightOperand": 1000,
          "unit": "http://fakerealestate.com/vocab/hour"
        }
      ],
      "duty": [
        {
          "action": "pay",
          "target": "http://fakerealestate.com/vocab/intentPrice",
          "amount": 0.01,
          "unit": "http://fakerealestate.com/vocab/USD"
        }
      ]
    }
  ],
  "prohibition": [
    {
      "target": "http://fakerealestate.com/api/intents",
      "action": "exceedRateLimit"
    }
  ],
  "obligation": [
    {
      "action": "signPayload",
      "assignee": "http://aiagent.com/agent/1",
      "target": "http://fakerealestate.com/vocab/payload",
      "constraint": [
        {
          "leftOperand": "http://fakerealestate.com/vocab/publicKey",
          "operator": "use",
          "rightOperand": "MIIBIjANBgkqh..."
        }
      ]
    }
  ],
  "party": [
    {
      "function": "assigner",
      "identifier": "http://fakerealestate.com"
    },
    {
      "function": "assignee",
      "identifier": "http://aiagent.com/agent/1"
    }
  ],
  "asset": "http://fakerealestate.com/api/intents"
}
```

### D. Sample PAT Structure

```json
{
  "pat": {
    "uid": "pat-12345",
    "issued_to": "ai-agent-1",
    "issued_by": "fakerealestate.com",
    "policy_reference": "http://fakerealestate.com/policy/12345",
    "permissions": ["execute:intent/SearchProperty"],
    "obligations": ["pay:0.01 USD per intent"],
    "billing_info": {
      "payment_method": "credit_card",
      "billing_address": "123 AI Street, Tech City",
      "currency": "USD"
    },
    "valid_from": "2024-01-01T00:00:00Z",
    "valid_to": "2024-12-31T23:59:59Z"
  },
  "signature": "Base64-encoded-digital-signature"
}
```

### E. Sample API Requests and Responses

#### Intent Discovery Request

```curl
GET /api/intents/search?intent_name=SearchProperty
```

#### Intent Discovery Response

```json
{
  "intents": [
    {
      "service_name": "Fake Real Estate",
      "intent_name": "SearchProperty",
      "intent_uid": "fakerealestate.com:SearchProperty:v1",
      "description": "Search properties based on criteria",
      "input_parameters": [
        {"name": "location", "type": "string", "required": true}
      ],
      "output_parameters": [
        {"name": "properties", "type": "array", "description": "List of properties"}
      ],
      "endpoint": "https://fakerealestate.com/api/execute/SearchProperty",
      "tags": ["real estate", "search"]
    }
  ]
}
```

#### Execute Intent Request

```json
POST /api/intents/execute
Authorization: Bearer PAT-12345
Content-Type: application/json

{
  "intent_uid": "fakerealestate.com:SearchProperty:v1",
  "parameters": {
    "location": "New York",
    "min_price": 500000,
    "max_price": 1000000
  }
}
```

#### Execute Intent Response

```json
{
  "properties": [
    {
      "property_id": "NYC123",
      "address": "123 Main St, New York, NY",
      "price": 750000,
      "property_type": "Apartment"
    },
    {
      "property_id": "NYC124",
      "address": "456 Broadway, New York, NY",
      "price": 850000,
      "property_type": "Condo"
    }
  ],
  "total_results": 2
}
```

### F. High Level System Architecture Diagram

1. **Centralized Architecture**:

   - **AI Agent** interacts with the **Central Repository** for discovery, policy agreement, and execution.
   - **Central Repository** communicates with **Web Services** to forward execution requests and receive responses.
  ![Centralized flow](images/central-arch-box.png)

2. **Decentralized Architecture**:

   - **AI Agent** discovers **Web Services** via DNS TXT records and `agents.json` files.
   - **AI Agent** communicates directly with **Web Services** for policy agreement and intent execution.
  ![Decentralized flow](images/decentral-arch-box.png)

3. **Hybrid Approach**:

   - **AI Agent** uses the **Central Repository** for intent discovery.
   - **AI Agent** interacts directly with **Web Services** for policy agreement and execution.
  ![Hybrid flow](images/hybrid-arch-box.png)

---

## Milestones for the UIM Protocol Development

The UIM Protocol is intended to be a community-driven and open standards project. The development of the protocol will be divided into five phases, each with specific milestones and goals. The following sections outline the milestones for each phase.

### **Phase 1: Draft Proposal and Initial Community Feedback**

- **Milestone 1.1**: Publish the Draft Proposal
  - Publish the initial draft of the UIM Protocol on GitHub, outlining the core components, specifications, and goals.
- **Milestone 1.2**: Community Engagement and Outreach
  - Launch the Discord server and start discussions on GitHub. Share the proposal on social media and tech communities.
- **Milestone 1.3**: Gather Feedback and Conduct Surveys
  - Encourage community feedback through GitHub issues, discussions, and feedback forms to identify key concerns and suggestions.

### **Phase 2: Refinement and Iterative Updates**

- **Milestone 2.1**: Analyze Feedback and Prioritize Changes
  - Review feedback, prioritize updates, and refine the protocol’s design and documentation based on community input.
- **Milestone 2.2**: Release Updated Drafts
  - Publish updated drafts addressing key feedback points and improvements. Highlight changes and continue discussions.
- **Milestone 2.3**: Host Webinars and Q&A Sessions
  - Organize sessions to discuss updates, answer questions, and engage directly with contributors.

### **Phase 3: Testing and Proof-of-Concept Implementations**

- **Milestone 3.1**: Develop Proof-of-Concept Implementations
  - Build example AI agents and web services using the protocol to validate functionality and identify gaps.
- **Milestone 3.2**: Community Testing and Bug Reporting
  - Encourage community members to test implementations, raise issues, and contribute code or documentation improvements.
- **Milestone 3.3**: Security and Compliance Review
  - Conduct a detailed review of security features and compliance mechanisms to ensure robustness.

### **Phase 4: Final Refinements and Preparation for v1.0 Release**

- **Milestone 4.1**: Finalize the Protocol Specification
  - Incorporate feedback from testing and finalize all sections of the specification.
- **Milestone 4.2**: Complete Documentation and Guides
  - Develop comprehensive documentation, including installation guides, API references, and best practice guides.
- **Milestone 4.3**: Pre-Release Candidate
  - Release a pre-v1.0 candidate version for final review by the community.

### **Phase 5: Version 1.0 Release and Promotion**

- **Milestone 5.1**: Official v1.0 Release
  - Publish the final version of the UIM Protocol, including all associated resources.
- **Milestone 5.2**: Launch Campaign and Public Announcements
  - Announce the v1.0 release across all channels, including social media, tech forums, newsletters, and webinars.
- **Milestone 5.3**: Post-Release Support and Community Engagement
  - Continue engaging with the community, support early adopters, and gather feedback for future updates.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
```

--------------------------------------------------------------------------------

### File: faq.md
```
Path: faq.md
Size: 3.15 KB
Last Modified: 2024-09-20 16:49:44
```

**Contents:**
```
# Unified Intent Mediator (UIM) Protocol: FAQ

### 1. What is the Unified Intent Mediator (UIM) Protocol?
The Unified Intent Mediator (UIM) Protocol is a standardized framework designed to streamline interactions between AI agents and web services. It defines a common language and set of rules for communication, allowing AI agents to discover, understand, and execute actions (called "intents") offered by various web services in a secure, compliant, and efficient manner.

### 2. How does the UIM Protocol work in a decentralized architecture?
In a decentralized architecture, web services publish their capabilities as "intents" through DNS TXT records and agents.json files. AI agents then crawl these resources to discover and interact directly with web services, eliminating the need for a central intermediary. This approach offers scalability, autonomy, and preserves data ownership for web services.

### 3. What are Policy Adherence Tokens (PATs) and why are they important?
PATs are digitally signed tokens issued by web services to AI agents, granting them permission to execute specific actions. These tokens encapsulate compliance requirements, usage limits, and billing agreements, ensuring secure and regulated interactions. PATs streamline policy enforcement and simplify billing processes within the UIM ecosystem.

### 4. How does the UIM Protocol handle billing and monetization?
The UIM Protocol supports various monetization strategies, including transaction fees, usage-based billing, subscription models, and revenue-sharing partnerships. Web services have the flexibility to choose the most suitable model for their offerings, while the protocol ensures secure and transparent billing processes.

### 5. What is the role of ODRL in the UIM Protocol?
The Open Digital Rights Language (ODRL) is integrated into the UIM Protocol to provide a standardized way to define and manage permissions, prohibitions, and obligations between AI agents and web services. This integration ensures clear, verifiable, and enforceable policies, enhancing security and compliance within the ecosystem.

### 6. What are the benefits of using a hybrid architecture for the UIM Protocol?
A hybrid architecture combines centralized discovery with decentralized execution and PAT issuance. This approach offers the benefits of both worlds: a unified discovery mechanism for AI agents while preserving the autonomy, scalability, and customized security of decentralized interactions.

### 7. How does the UIM Protocol ensure security and compliance?
Security and compliance are paramount in the UIM Protocol. It utilizes HTTPS for secure communication, OAuth 2.0 for authentication, and enforces compliance with regulations like GDPR and CCPA. Additionally, PATs and ODRL integration strengthen security by defining and enforcing access control and usage policies.

### 8. How can I get involved in the development of the UIM Protocol?
The UIM Protocol is an open-source project, and community involvement is highly encouraged. You can contribute by reviewing the draft specification, joining discussions on platforms like Discord and GitHub, raising issues, submitting pull requests, and sharing the project with your network.
```

--------------------------------------------------------------------------------

### File: intent_examples.md
```
Path: intent_examples.md
Size: 28.69 KB
Last Modified: 2024-09-03 16:20:31
```

**Contents:**
```
# AI Agent Intent Examples

## AI-Agent Driven E-Commerce Integration for Personalized Shopping Experiences

* **searchProducts**: "Find products based on user preferences, keywords, and categories”  
  * Parameters: query (string), category (string, optional), priceRange (string, optional), sortBy (string, optional)  
* **getProductDetails**: "Retrieve detailed information about a specific product.”  
  * Parameters: productId (string)  
* **addToCart**: "Add a selected product to the user's shopping cart.”  
  * Parameters: productId (string), quantity (integer)  
* **checkoutCart**: "Proceed to checkout with the current items in the user's cart.”  
  * Parameters: paymentMethod (string), shippingAddress (string)  
* **trackOrder**: "Monitor the status of an order and provide updates.”  
  * Parameters: orderId (string)

## Financial Service Automation Using AI-Agent Driven Interactions

* **checkAccountBalance**: "Retrieve the current balance of the user's accounts.”  
  * Parameters: accountId (string)  
* **monitorTransactions**: "Track recent transactions and notify users of any unusual activity.”  
  * Parameters: accountId (string), startDate (string, optional), endDate (string, optional)  
* **transferFunds**: "Facilitate secure money transfers between accounts or to other users.”  
  * Parameters: fromAccountId (string), toAccountId (string), amount (float)  
* **payBill**: "Schedule and automate recurring bill payments.”  
  * Parameters: billerId (string), amount (float), dueDate (string)  
* **financialPlanning**: "Provide personalized financial advice and budgeting tips based on user spending patterns.”  
  * Parameters: accountId (string), goals (string, optional)

## AI-Agent Powered Social Media Content Management

* **schedulePost**: "Automate the scheduling and posting of content across multiple social media platforms.”  
  * Parameters: content (string), platforms (array of strings), scheduledTime (string)  
* **curateContent**: "Suggest relevant content for sharing based on trending topics and user interests.”  
  * Parameters: interests (array of strings), platforms (array of strings, optional)  
* **respondToComments**: "Automatically respond to comments and messages with predefined templates.”  
  * Parameters: postId (string), responseTemplate (string)  
* **analyzePerformance**: "Provide analytics and insights on post performance and audience engagement.”  
  * Parameters: postId (string), metrics (array of strings, optional)  
* **manageAdCampaigns**: "Create, monitor, and optimize social media advertising campaigns.”  
  * Parameters: campaignDetails (object), budget (float)

## Healthcare Service Booking and Management Through AI Agents

* **bookAppointment**: "Schedule medical appointments with healthcare providers.”  
  * Parameters: providerId (string), date (string), time (string), reason (string, optional)  
* **managePrescriptions**: "Track prescription refills and notify users when it’s time to renew.”   
  * Parameters: prescriptionId (string), refillDate (string)  
* **accessMedicalRecords**: "Retrieve and display the user's medical history and records.”   
  * Parameters: userId (string)  
* **symptomChecker**: "Provide initial diagnosis and health advice based on reported symptoms.”  
  * Parameters: symptoms (array of strings)  
* **healthReminders**: "Send reminders for medication, appointments, and health check-ups.”  
  * Parameters: reminderType (string), date (string), time (string)

## AI-Agent Enabled News and Media Content Curation

* **personalizedNewsFeed**: "Curate a personalized news feed based on user interests and preferences.”  
  * Parameters: interests (array of strings), sources (array of strings, optional)  
* **breakingNewsAlerts**: "Notify users of important news events as they happen.”   
  * Parameters: categories (array of strings, optional)  
* **summarizeArticle**: "Provide concise summaries of long articles for quick reading.”  
  * Parameters: articleUrl (string)  
* **saveForLater**: "Allow users to save articles and videos to view later.”  
  * Parameters: contentUrl (string)  
* **exploreTopics**: "Suggest related topics and articles based on user reading history.”  
  * Parameters: currentTopic (string)

## Secure Fund Transfer Systems Utilizing AI-Agent Interfaces

* **initiateTransfer**: "Facilitate secure transfers between user accounts and other recipients.”  
  * Parameters: fromAccountId (string), toAccountId (string), amount (float)  
* **trackTransfer**: "Monitor the status of fund transfers and provide updates to users.”  
  * Parameters: transferId (string)  
* **setTransferLimits**: "Allow users to set daily or monthly transfer limits for added security.”  
  * Parameters: accountId (string), limit (float)  
* **verifyRecipient**: "Confirm recipient details before completing transfers to prevent errors.”  
  * Parameters: recipientId (string)  
* **transactionHistory**: "Provide a detailed history of all past transfers for user reference.”  
  * Parameters: accountId (string), startDate (string, optional), endDate (string, optional)

## AI-Agent Powered Travel and Booking Platforms

* **searchFlights**: "Find and compare flights based on user preferences.”  
  * Parameters: origin (string), destination (string), departureDate (string), returnDate (string, optional)  
* **bookAccommodation**: "Reserve hotels or vacation rentals according to user criteria.”  
  * Parameters: location (string), checkInDate (string), checkOutDate (string), roomType (string, optional)  
* **createItinerary**: "Generate travel itineraries including flights, accommodations, and activities.”  
  * Parameters: tripDetails (object)  
* **trackBookings**: "Monitor booking statuses and send reminders for upcoming trips.”  
  * Parameters: bookingId (string)  
* **travelRecommendations**: "Suggest destinations, activities, and dining options based on user interests.”  
  * Parameters: interests (array of strings), location (string, optional)

## Automated Customer Support Through AI-Agent Interactions

* **answerFAQ**: "Provide instant responses to frequently asked questions.”  
  * Parameters: question (string)  
* **createSupportTicket**: "Create and track support tickets for user inquiries.”  
  * Parameters: issueDescription (string), priority (string, optional)  
* **liveChatSupport**: "Offer real-time chat support with AI-driven responses.”  
  * Parameters: userMessage (string)  
* **resolveIssue**: "Guide users through troubleshooting steps to resolve common issues.”  
  * Parameters: issueType (string)  
* **collectFeedback**: "Collect and analyze user feedback to improve services.”  
  * Parameters: feedback (string), rating (integer)

## AI-Agent Driven Data Analytics for Business Insights

* **generateReport**: "Create detailed business reports based on collected data.”  
  * Parameters: reportType (string), timePeriod (string, optional)  
* **predictiveAnalytics**: "Provide forecasts and predictive insights based on historical data.”  
  * Parameters: dataSetId (string), predictionType (string)  
* **identifyTrends**: "Highlight emerging trends and patterns in business data.”  
  * Parameters: dataSetId (string), trendType (string)  
* **trackKPIs**: "Monitor key performance indicators and alert users of any significant changes.”  
  * Parameters: kpi (string), threshold (float)  
* **dataVisualization**: "Present data in visually appealing charts and graphs for easier interpretation.”  
  * Parameters: dataSetId (string), visualizationType (string)

## AI-Agent Integration for Home Automation Systems

* **controlDevice**: "Manage and control smart home devices such as lights, thermostats, and security cameras.”  
  * Parameters: deviceId (string), command (string)  
* **automateRoutine**: "Set up and automate daily routines for home devices.”  
  * Parameters: routineName (string), schedule (string), devices (array of objects)  
* **monitorSecurity**: "Track home security status and send alerts for any suspicious activities.”  
  * Parameters: securityDeviceId (string)  
* **manageEnergyUsage**: "Optimize energy usage and provide recommendations for savings.”  
  * Parameters: deviceId (string), usageData (object)  
* **voiceControl**: "Enable voice control for various home automation tasks.”  
  * Parameters: command (string)

## AI-Agent Based Appointment Scheduling for Various Services

* **scheduleAppointment**: "Book appointments for services such as salons, car repairs, and healthcare.”  
  * Parameters: serviceId (string), date (string), time (string)  
* **manageCalendar**: "Sync appointments with user calendars and send reminders.”  
  * Parameters: calendarId (string)  
* **rescheduleAppointment**: "Allow users to easily reschedule appointments.”  
  * Parameters: appointmentId (string), newDate (string), newTime (string)  
* **cancelAppointment**: "Cancel scheduled appointments.”  
  * Parameters: appointmentId (string)  
* **recommendServices**: "Suggest related services or follow-up appointments based on user history.”  
  * Parameters: userId (string), currentService (string)

## AI-Agent Powered Online Education Platforms

* **recommendCourses**: "Suggest courses and learning materials based on user interests and progress. Parameters: userId (string), interests (array of strings)"  
* **trackProgress**: "Monitor user progress and provide feedback on performance. Parameters: userId (string), courseId (string)"  
* **automateGrading**: "Grade assignments and quizzes automatically. Parameters: courseId (string), assignmentId (string)"  
* **scheduleLessons**: "Arrange and remind users of upcoming lessons and study sessions. Parameters: courseId (string), lessonDate (string), lessonTime (string)"  
* **peerInteraction**: "Facilitate interactions with peers and instructors through forums and chat. Parameters: courseId (string), message (string)"

## AI-Agent Enabled Legal Service Consultations

* **bookConsultation**: "Schedule appointments with legal professionals. Parameters: lawyerId (string), date (string), time (string)"  
* **reviewDocuments**: "Upload and review legal documents with AI assistance. Parameters: documentId (string)"  
* **provideLegalAdvice**: "Provide preliminary legal advice based on user queries. Parameters: query (string)"  
* **trackCaseStatus**: "Monitor the status of ongoing legal cases. Parameters: caseId (string)"  
* **estimateCosts**: "Offer cost estimates for legal services based on user needs. Parameters: serviceType (string), details (object)"

## Personalized AI-Agent Driven Fitness and Wellness Platforms

* **recommendWorkouts**: "Suggest personalized workout plans based on user goals and fitness level. Parameters: userId (string), fitnessGoals (string)"  
* **trackFitnessProgress**: "Monitor and record fitness activities and progress. Parameters: userId (string), activityData (object)"  
* **provideNutritionAdvice**: "Provide dietary recommendations and meal plans. Parameters: userId (string), dietaryPreferences (string)"  
* **monitorHealthMetrics**: "Track vital health metrics and send alerts for any anomalies. Parameters: userId (string), healthData (object)"  
* **sendMotivationalReminders**: "Send motivational messages and reminders to keep users engaged. Parameters: userId (string), message (string)"

## AI-Agent Driven Job Search and Recruitment Platforms

* **recommendJobs**: "Suggest job listings based on user profile and preferences. Parameters: userId (string), jobPreferences (array of strings)"  
* **trackApplications**: "Monitor the status of job applications and send updates. Parameters: applicationId (string)"  
* **assistResumeBuilding**: "Help in creating and optimizing resumes and cover letters. Parameters: userId (string), resumeData (object)"  
* **prepareForInterviews**: "Provide tips and mock interview sessions to prepare users. Parameters: userId (string), interviewType (string)"  
* **suggestNetworkingOpportunities**: "Recommend networking events and professional connections. Parameters: userId (string), industry (string)"

## Real Estate Services Enhanced by AI-Agent Interactions

* **searchProperties**: "Find and compare properties based on user criteria. Parameters: location (string), propertyType (string), priceRange (string)"  
* **scheduleViewings**: "Arrange property viewings and send reminders. Parameters: propertyId (string), date (string), time (string)"  
* **estimatePropertyPrices**: "Provide market value estimates for properties. Parameters: propertyId (string)"  
* **manageDocuments**: "Assist in managing and reviewing real estate documents. Parameters: documentId (string)"  
* **matchAgents**: "Recommend real estate agents based on user preferences. Parameters: userId (string), location (string)"

## AI-Agent Powered Personal Finance Management Tools

* **trackBudget**: "Monitor and categorize expenses to help users stay within budget. Parameters: userId (string), budgetData (object)"  
* **setSavingsGoals**: "Set and track progress towards savings goals. Parameters: userId (string), goalAmount (float)"  
* **provideInvestmentAdvice**: "Offer personalized investment recommendations. Parameters: userId (string), investmentPreferences (string)"  
* **sendBillReminders**: "Notify users of upcoming bills and due dates. Parameters: userId (string), billDetails (object)"  
* **analyzeExpenses**: "Analyze spending patterns and suggest ways to save money. Parameters: userId (string), expenseData (object)"

## AI-Agent Based Entertainment and Media Recommendations

* **recommendContent**: "Suggest movies, TV shows, music, and books based on user preferences. Parameters: userId (string), contentType (string)"  
* **highlightTrendingContent**: "Show trending and popular content in various categories. Parameters: contentType (string)"  
* **createPersonalizedPlaylists**: "Generate and manage personalized playlists for music and videos. Parameters: userId (string), contentType (string)"  
* **notifyNewReleases**: "Alert users of new releases and upcoming content. Parameters: userId (string), contentType (string)"  
* **provideContentReviews**: "Offer reviews and ratings for various entertainment options. Parameters: contentId (string)"

## AI-Agent Enabled Event Planning and Management Platforms

* **discoverEvents**: "Find and suggest events based on user interests. Parameters: userId (string), eventType (string)"  
* **bookTickets**: "Facilitate ticket booking and payment for events. Parameters: eventId (string), ticketType (string)"  
* **manageEventSchedule**: "Organize and manage event schedules. Parameters: userId (string), eventDetails (object)"  
* **sendInvitations**: "Send and track invitations to events. Parameters: eventId (string), invitees (array of strings)"  
* **remindEvent**: "Notify users of upcoming events and any changes. Parameters: userId (string), eventId (string)"

## AI-Agent Powered Marketplace for Freelance Services

* **searchFreelancers**: "Find and compare freelance services based on user needs. Parameters: serviceType (string), location (string, optional)"  
* **hireFreelancer**: "Facilitate hiring and contract management for freelancers. Parameters: freelancerId (string), projectDetails (object)"  
* **trackProjectProgress**: "Monitor project progress and deliverables. Parameters: projectId (string)"  
* **processPayments**: "Handle payments and invoicing for freelance services. Parameters: projectId (string), amount (float)"  
* **collectReviews**: "Gather and display reviews and ratings for freelancers. Parameters: freelancerId (string), review (string), rating (integer)"

## AI-Agent Driven Supply Chain and Logistics Management

* **trackShipment**: "Monitor the status and location of shipments in real-time. Parameters: shipmentId (string)"  
* **manageInventory**: "Oversee inventory levels and send alerts for restocking. Parameters: warehouseId (string), productId (string)"  
* **processOrders**: "Automate order processing and fulfillment. Parameters: orderId (string)"  
* **evaluateSuppliers**: "Track and evaluate supplier performance. Parameters: supplierId (string)"  
* **optimizeLogistics**: "Provide recommendations for optimizing logistics and reducing costs. Parameters: logisticsData (object)"

## AI-Agent Enabled Customer Feedback and Survey Systems

* **createSurvey**: "Design and distribute customer surveys. Parameters: surveyDetails (object)"  
* **collectFeedback**: "Gather and analyze feedback from customers. Parameters: surveyId (string), customerId (string)"  
* **analyzeSentiment**: "Analyze customer feedback for sentiment and trends. Parameters: feedbackData (object)"  
* **generateReport**: "Produce detailed reports on survey results. Parameters: surveyId (string)"  
* **recommendActions**: "Suggest follow-up actions based on survey findings. Parameters: surveyId (string), recommendations (array of strings)"

## AI-Agent Powered Product Recommendation Engines

* **personalizedSuggestions**: "Provide personalized product recommendations based on user behavior. Parameters: userId (string), preferences (array of strings)"  
* **relatedProducts**: "Suggest related products based on current user selections. Parameters: productId (string)"  
* **highlightBestSellers**: "Show best-selling products in various categories. Parameters: category (string)"  
* **displayUserReviews**: "Show user reviews and ratings for products. Parameters: productId (string)"  
* **compareProducts**: "Allow users to compare similar products side-by-side. Parameters: productIds (array of strings)"

## AI-Agent Based Security and Surveillance Systems

* **monitorPremises**: "Continuously monitor premises using connected cameras and sensors. Parameters: cameraId (string), schedule (string)"  
* **alertIntrusion**: "Send real-time alerts in case of any detected intrusion or suspicious activity. Parameters: sensorId (string), alertType (string)"  
* **controlAccess**: "Manage and control access to secured areas. Parameters: accessPointId (string), command (string)"  
* **reportIncidents**: "Generate reports on security incidents and actions taken. Parameters: incidentId (string), reportDetails (object)"  
* **remoteControlSecurity**: "Allow remote control of security systems via AI agents. Parameters: systemId (string), command (string)"

## AI-Agent Driven Marketing and Advertising Platforms

* **manageAdCampaigns**: "Create, manage, and optimize ad campaigns. Parameters: campaignDetails (object), budget (float)"  
* **targetAudience**: "Identify and target specific audience segments for marketing. Parameters: audienceCriteria (object)"  
* **analyzeAdPerformance**: "Provide detailed analytics on ad campaign performance. Parameters: campaignId (string)"  
* **createMarketingContent**: "Assist in creating marketing content and advertisements. Parameters: contentDetails (object)"  
* **manageMarketingBudget**: "Track and manage marketing budgets and expenditures. Parameters: budgetDetails (object)"

## AI-Agent Enabled Restaurant Reservation Systems

* **searchRestaurants**: "Find restaurants based on user preferences and location. Parameters: location (string), cuisineType (string, optional)"  
* **bookTable**: "Facilitate table bookings at chosen restaurants. Parameters: restaurantId (string), date (string), time (string), partySize (integer)"  
* **recommendMenuItems**: "Suggest menu items based on user tastes and dietary preferences. Parameters: restaurantId (string), dietaryPreferences (string)"  
* **handleSpecialRequests**: "Manage special requests like dietary restrictions or seating preferences. Parameters: bookingId (string), specialRequest (string)"  
* **sendReservationReminders**: "Notify users of upcoming reservations. Parameters: bookingId (string)"

## AI-Agent Powered Personal Shopping Assistants

* **manageShoppingList**: "Create and manage shopping lists for users. Parameters: userId (string), listItems (array of strings)"  
* **searchForProducts**: "Find products based on user preferences and needs. Parameters: query (string), category (string, optional)"  
* **notifyPriceDrops**: "Notify users of price drops or special deals on desired items. Parameters: productId (string)"  
* **placeOrder**: "Place orders on behalf of users with preferred retailers. Parameters: retailerId (string), orderDetails (object)"  
* **trackDeliveries**: "Monitor and provide updates on the delivery status of orders. Parameters: orderId (string)"

## AI-Agent Driven Transportation and Ride-Hailing Services

* **bookRide**: "Schedule rides with ride-hailing services. Parameters: pickupLocation (string), destination (string), rideType (string)"  
* **optimizeRoute**: "Provide optimized routes for travel. Parameters: currentLocation (string), destination (string)"  
* **estimateFare**: "Estimate fares for different ride options. Parameters: pickupLocation (string), destination (string)"  
* **trackVehicle**: "Monitor the real-time location of booked vehicles. Parameters: bookingId (string)"  
* **manageSharedRides**: "Suggest and manage shared ride options to reduce costs. Parameters: pickupLocation (string), destination (string)"

## AI-Agent Enabled Environmental Monitoring and Management Systems

* **monitorAirQuality**: "Track and report air quality levels in real-time. Parameters: location (string), pollutantType (string, optional)"  
* **analyzeWaterQuality**: "Monitor and analyze water quality data. Parameters: location (string), sampleData (object)"  
* **optimizeWasteManagement**: "Optimize waste collection and disposal processes. Parameters: location (string), wasteType (string)"  
* **trackEnergyConsumption**: "Track and analyze energy usage patterns. Parameters: location (string), energyData (object)"  
* **sendEnvironmentalAlerts**: "Notify users of any detected environmental hazards or changes. Parameters: alertType (string), location (string)"

## AI-Agent Powered Community Management Platforms

* **coordinateEvents**: "Organize and promote community events. Parameters: eventDetails (object)"  
* **maintainMemberDirectory**: "Manage a directory of community members. Parameters: communityId (string)"  
* **facilitateDiscussions**: "Facilitate community discussions and forums. Parameters: topic (string), message (string)"  
* **manageResources**: "Manage and share community resources. Parameters: resourceId (string), details (object)"  
* **sendCommunityUpdates**: "Send updates and announcements to community members. Parameters: communityId (string), message (string)"

## AI-Agent Driven Financial Market Analysis Tools

* **analyzeMarketTrends**: "Analyze and report on market trends and patterns. Parameters: marketType (string), timePeriod (string)"  
* **recommendStocks**: "Provide personalized stock recommendations based on user preferences. Parameters: userId (string), riskTolerance (string)"  
* **managePortfolio**: "Assist in managing and optimizing investment portfolios. Parameters: userId (string), portfolioDetails (object)"  
* **evaluateInvestmentRisks**: "Evaluate and report on investment risks. Parameters: investmentId (string), riskFactors (array of strings)"  
* **sendMarketNewsAlerts**: "Notify users of market news and events that could impact investments. Parameters: marketType (string)"

## AI-Agent Enabled Language Translation and Localization Services

* **translateText**: "Translate text between different languages. Parameters: text (string), sourceLanguage (string), targetLanguage (string)"  
* **provideVoiceTranslation**: "Offer real-time voice translation for conversations. Parameters: sourceLanguage (string), targetLanguage (string)"  
* **localizeDocuments**: "Adapt documents for different regions and cultures. Parameters: documentId (string), targetLocale (string)"  
* **adaptContent**: "Modify content to suit cultural nuances and preferences. Parameters: contentId (string), targetLocale (string)"  
* **assistLanguageLearning**: "Help users learn new languages with personalized lessons. Parameters: userId (string), language (string)"

## AI-Agent Powered Virtual Travel and Tourism Guides

* **provideVirtualTours**: "Offer virtual tours of tourist attractions. Parameters: location (string), tourType (string)"  
* **createTravelItineraries**: "Generate personalized travel itineraries. Parameters: userId (string), destinations (array of strings)"  
* **recommendLocalAttractions**: "Suggest local attractions, restaurants, and activities. Parameters: location (string), interests (array of strings)"  
* **offerLanguageAssistance**: "Provide translation and language assistance for travelers. Parameters: sourceLanguage (string), targetLanguage (string)"  
* **sendTravelAlerts**: "Notify users of travel advisories and updates. Parameters: location (string), alertType (string)"

## AI-Agent Driven Smart City Infrastructure Management

* **manageTrafficFlow**: "Monitor and optimize traffic flow in real-time. Parameters: location (string), trafficData (object)"  
* **overseePublicServices**: "Manage public services such as waste collection and water supply. Parameters: serviceType (string), location (string)"  
* **optimizeEnergyUsage**: "Track and optimize energy usage across the city. Parameters: location (string), energyData (object)"  
* **monitorCitySecurity**: "Provide city-wide security monitoring and incident reporting. Parameters: location (string), securityData (object)"  
* **facilitateCitizenEngagement**: "Enable communication between city officials and citizens. Parameters: topic (string), message (string)"

## AI-Agent Enabled Human Resource Management Systems

* **assistRecruitment**: "Help in screening and recruiting candidates. Parameters: jobId (string), candidateDetails (object)"  
* **manageOnboarding**: "Oversee the onboarding process for new employees. Parameters: employeeId (string), onboardingDetails (object)"  
* **trackPerformance**: "Monitor and evaluate employee performance. Parameters: employeeId (string), metrics (array of strings)"  
* **recommendTrainingPrograms**: "Suggest training programs for employees. Parameters: employeeId (string), trainingNeeds (array of strings)"  
* **handleLeaveRequests**: "Manage employee leave requests and approvals. Parameters: employeeId (string), leaveType (string), startDate (string), endDate (string)"

## AI-Agent Powered Energy Management and Optimization Platforms

* **monitorEnergyConsumption**: "Track and analyze energy consumption patterns. Parameters: location (string), energyData (object)"  
* **recommendCostReduction**: "Provide recommendations for reducing energy costs. Parameters: location (string), usagePatterns (object)"  
* **integrateRenewableEnergy**: "Manage the integration of renewable energy sources. Parameters: energySource (string), capacity (float)"  
* **sendRealTimeAlerts**: "Notify users of any anomalies in energy usage. Parameters: location (string), alertType (string)"  
* **generateEfficiencyReports**: "Produce reports on energy efficiency and usage trends. Parameters: location (string), reportType (string)"

## AI-Agent Driven Personalized Learning Assistants

* **createLearningPathways**: "Generate personalized learning pathways based on user goals. Parameters: userId (string), learningGoals (array of strings)"  
* **monitorLearningProgress**: "Track and report on learning progress. Parameters: userId (string), courseId (string)"  
* **recommendLearningResources**: "Suggest learning resources and materials. Parameters: userId (string), interests (array of strings)"  
* **provideInteractiveQuizzes**: "Offer interactive quizzes and assessments. Parameters: userId (string), courseId (string)"  
* **sendStudyReminders**: "Notify users of study sessions and upcoming assessments. Parameters: userId (string), reminderType (string)"

## AI-Agent Enabled Telemedicine and Remote Healthcare Services

* **scheduleVirtualConsultations**: "Book and manage virtual consultations with healthcare providers. Parameters: providerId (string), date (string), time (string)"  
* **monitorSymptoms**: "Track and report symptoms to healthcare providers. Parameters: userId (string), symptoms (array of strings)"  
* **managePrescriptionsRemotely**: "Handle prescription refills and renewals. Parameters: userId (string), prescriptionId (string)"  
* **accessHealthRecords**: "Provide access to personal health records. Parameters: userId (string)"  
* **offerWellnessTips**: "Send personalized wellness and preventive care tips. Parameters: userId (string), wellnessGoals (array of strings)"

## AI-Agent Powered Automated Legal Document Generation

* **draftContracts**: "Automatically draft contracts based on user input. Parameters: userId (string), contractDetails (object)"  
* **reviewLegalDocuments**: "Analyze and suggest improvements to legal documents. Parameters: documentId (string)"  
* **ensureCompliance**: "Check documents for compliance with relevant regulations. Parameters: documentId (string), regulations (array of strings)"  
* **manageDocumentTemplates**: "Customize and manage legal document templates. Parameters: templateId (string)"  
* **facilitateESignatures**: "Enable electronic signatures for legal documents. Parameters: documentId (string)"

```

--------------------------------------------------------------------------------

### File: llm_context.md
```
Path: llm_context.md
Size: 95.78 KB
Last Modified: 2025-01-16 16:24:48
```

**Contents:**
```
# Project Directory Analysis
Generated on: 2025-01-16 16:24:48

## Ignored Patterns
```
- .DS_Store
- .dockerignore
- .env
- .flake8
- .git
- .gitignore
- .idea
- .pyproject.toml
- .pytest_cache
- .vscode
- LICENSE
- __pycache__
- data/
- input/
- node_modules
- output/
- repo2llm.py
- run.sh
- scripts/
- src/cache
- tests/
- utils/
- venv
```

## Directory Structure
```
./
├── centralized-discovery-service
│   ├── app
│   │   ├── crud
│   │   │   ├── __init__.py
│   │   │   ├── intent.py
│   │   │   └── service.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── intent.py
│   │   │   ├── service.py
│   │   │   └── tag.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   ├── discovery.py
│   │   │   └── search.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   ├── intent.py
│   │   │   ├── service.py
│   │   │   └── tag.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   ├── crawler.py
│   │   │   ├── dns_utils.py
│   │   │   └── nlp.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── main.py
│   ├── Dockerfile
│   ├── README.md
│   ├── docker-compose.yml
│   ├── pytest.ini
│   └── requirements.txt
├── images
│   ├── abstract-dark.png
│   ├── abstract.png
│   ├── adoption.png
│   ├── ai-agent-architecture.png
│   ├── ai-capabilities.png
│   ├── ai-discovery.png
│   ├── architecture-comparison.png
│   ├── billing-benefits.png
│   ├── blockchain.png
│   ├── catalyst.png
│   ├── central-arch-box.png
│   ├── central-arch.png
│   ├── centralized-repo.png
│   ├── challenges-spec.png
│   ├── challenges.png
│   ├── concept.png
│   ├── decentral-arch-box.png
│   ├── decentral-arch.png
│   ├── developer-ecosystem.png
│   ├── discoverability.png
│   ├── dns-txt-and-agents-txt.png
│   ├── dns-vs-txt.png
│   ├── ecommerce-example.png
│   ├── execute-method.png
│   ├── execution-method.png
│   ├── future-development.png
│   ├── future-timeline.png
│   ├── hybrid-arch-box.png
│   ├── hybrid-arch.png
│   ├── intent-discovery.png
│   ├── intent-format.png
│   ├── logo-white.png
│   ├── logo.png
│   ├── main-architecture.png
│   ├── mediator-platform.png
│   ├── odrl-benefits.png
│   ├── pat-implementation.png
│   ├── policy-fields.png
│   ├── policy-flow.png
│   ├── realestate-example.png
│   ├── revenue-sharing.png
│   ├── solution-comparison.png
│   ├── subscription.png
│   ├── transaction-flow.png
│   ├── uim-benefits.png
│   ├── uim-protocol.png
│   ├── usage-based.png
│   └── vocabulary.png
├── podcast
│   ├── UIM Protocol.m4a
│   └── transcript.txt
├── uim-mock-agent
│   ├── keys
│   │   └── http_localhost_4000
│   │       ├── private_key.pem
│   │       └── public_key.pem
│   ├── src
│   │   ├── cli_interface.py
│   │   ├── discovery.py
│   │   ├── error_handling.py
│   │   ├── intent_execution.py
│   │   ├── key_management.py
│   │   ├── pat_issuance.py
│   │   ├── policy_management.py
│   │   └── policy_signing.py
│   ├── README.md
│   └── requirements.txt
├── uim-mock-webservice
│   ├── keys
│   │   ├── private_key.pem
│   │   └── public_key.pem
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── README.md
├── faq.md
├── intent_examples.md
├── llm_context.md
├── uim-compliance-with-eu-tdm-regulation.md
├── uim-concept.md
├── uim-licensing-scheme.md
├── uim-odrl-vocab.md
├── uim-prototypes-intro.md
├── uim-tdmrep-relation.md
└── uim-technical-exploration.md
```

## File Contents

### File: CODE_OF_CONDUCT.md
```
Path: CODE_OF_CONDUCT.md
Size: 5.11 KB
Last Modified: 2024-09-03 15:45:12
```

**Contents:**
```
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
the Discussions section in Github.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
```

--------------------------------------------------------------------------------

### File: CONTRIBUTING.md
```
Path: CONTRIBUTING.md
Size: 5.36 KB
Last Modified: 2024-09-03 15:45:12
```

**Contents:**
```

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of
  any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address,
  without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official email address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[INSERT CONTACT METHOD].
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations
```

--------------------------------------------------------------------------------

### File: README.md
```
Path: README.md
Size: 48.11 KB
Last Modified: 2024-09-30 21:04:55
```

**Contents:**
```
<div style="text-align: center;">
  <img src="images/logo.png" alt="logo" width="100" height="100">
</div>

# The Unified Intent Mediator Protocol

## Getting started

1. Get familiar with the [concepts and motivations](uim-concept.md) behind the UIM protocol or just read the specification below.
2. Dive into the [technical exploration](uim-technical-exploration.md) of the UIM protocol to understand and explore the details and technical choices behind the protocol.
3. Explore the [prototypes implementations](uim-prototypes-intro.md) to see the UIM protocol in action (WIP)

## Get Involved: We Need Your Feedback

We’re inviting developers, AI providers, service operators, and tech/AI enthusiasts to review the draft specification, test the implementation, and share feedback. Your input is crucial to refining and improving the protocol.

### How to Contribute

1. Review the Draft Proposal: Check out the draft specification and explore the protocol’s design and implementation.
2. Join the Discussion: Start a conversation in the Discussions tab. We’d love to hear your thoughts on the protocol’s design, potential use cases, or any concerns.
3. Raise Issues: Found a bug or have suggestions? Open an Issue to let us know or contribute directly by submitting a Pull Request. See our [Contributing Guidelines](CONTRIBUTING.md) for more information.
4. Share the Word: Help us spread the word about the UIM protocol by sharing this repository with your network. Write a blog post, tweet, or share the project with your colleagues. We appreciate your support!

---

## Protocol Draft Proposal

**Date:** September 30, 2024 - **Version:** 0.2

## Abstract

The Unified Intent Mediator (UIM) protocol defines a standardized framework for AI agents to interact with web services through well-defined intents, metadata, and execution methods. By introducing consistency and security in these interactions, UIM enhances efficiency, scalability, and reliability for AI-driven applications. This specification provides comprehensive guidelines for implementing the UIM protocol, ensuring interoperability, security, and compliance across different systems.

Key components include:

- **Intents**: Structured actions that web services can expose, defining specific tasks such as searching products, placing orders, or retrieving data. Each intent has a unique identifier, metadata, and required parameters.

- **Metadata and Parameters**: Each intent comes with metadata (name, description, category) and defined parameters, providing context and specific input requirements.

- **Policy Adherence Tokens (PATs)**: Digitally signed tokens issued by web services that encapsulate permissions, billing, and compliance rules, streamlining policy enforcement and automating billing.

- **Discovery and Execution APIs**: AI agents can query discovery APIs to find available intents and use execution APIs to perform actions. Execution involves validation, interaction with the service’s API, response formatting, and error handling.

- **DNS TXT Records and agents.json Files**: Innovative methods for endpoint discovery, allowing AI agents to find and authenticate API endpoints using familiar internet protocols.

- **Integration with Open Digital Rights Language (ODRL)**: Provides a structured approach to managing permissions, prohibitions, and obligations, ensuring clear and enforceable rules between AI agents and web services.

- **UIM Licensing Scheme**: An alternative method to the ODRL (Open Digital Rights Language) policy for defining the permissions, conditions, and prohibitions for data returned by web services. It specifies the license under which the data returned by intents can be used according to the [UIM Licensing Scheme](uim-licensing-scheme.md).

## Table of Contents

1. [Introduction](#1-introduction)
   - [1.1 Motivation](#11-motivation)
   - [1.2 Scope](#12-scope)
   - [1.3 Out of Scope](#13-out-of-scope)
2. [Terminology](#2-terminology)
3. [Key Concepts](#3-key-concepts)
   - [3.1 Intents](#31-intents)
   - [3.2 Metadata and Parameters](#32-metadata-and-parameters)
   - [3.3 The Execute Method](#33-the-execute-method)
   - [3.4 Policy Adherence Tokens (PATs)](#34-policy-adherence-tokens-pats)
   - [3.5 AI Agents](#35-ai-agents)
4. [System Architecture](#4-system-architecture)
   - [4.1 Centralized Architecture](#41-centralized-architecture)
   - [4.2 Decentralized Architecture](#42-decentralized-architecture)
   - [4.3 Hybrid Approach](#43-hybrid-approach)
5. [Core Components](#5-core-components)
   - [5.1 Intent Discovery and Execution Endpoints](#51-intent-discovery-and-execution-endpoints)
   - [5.2 Unique Intent Identifier (UID) Format](#52-unique-intent-identifier-uid-format)
   - [5.3 Intent Metadata](#53-intent-metadata)
   - [5.4 Discovery Through DNS TXT Records and `agents.json` Files](#54-discovery-through-dns-txt-records-and-agentsjson-files)
   - [5.5 Policy Adherence Tokens (PATs) and ODRL Integration](#55-policy-adherence-tokens-pats-and-odrl-integration)
   - [5.6 Incorporating Billing Information into PATs](#56-incorporating-billing-information-into-pats)
   - [5.7 Policy Adherence Tokens (PATs) and UIM Policy Scheme Integration](#57-policy-adherence-tokens-pats-and-uim-policy-scheme-integration)
   - [5.8 Service Management APIs](#58-service-management-apis)
   - [5.9 Intent Management APIs](#59-intent-management-apis)
6. [General API Guidelines and Standards](#6-general-api-guidelines-and-standards)
   - [6.1 Pagination](#61-pagination)
   - [6.2 Security and Compliance](#62-security-and-compliance)
   - [6.3 Monitoring and Analytics](#63-monitoring-and-analytics)
   - [6.4 Scalability](#64-scalability)
   - [6.5 Error Management Strategy](#65-error-management-strategy)
7. [Practical Examples and Use Cases](#7-practical-examples-and-use-cases)
   - [7.1 E-commerce Platform Integration](#71-e-commerce-platform-integration)
   - [7.2 Real Estate Data Retrieval](#72-real-estate-data-retrieval)
8. [Security Considerations](#8-security-considerations)
9. [Privacy Considerations](#9-privacy-considerations)
10. [Appendix](#10-appendix)
    - [A. Standard Error Codes and Messages](#a-standard-error-codes-and-messages)
    - [B. Complete `agents.json` File Example](#b-complete-agentsjson-file-example)
    - [C. Sample ODRL Policy](#c-sample-odrl-policy)
    - [D. Sample PAT Structure](#d-sample-pat-structure)
    - [E. Sample API Requests and Responses](#e-sample-api-requests-and-responses)
    - [F. High Level System Architecture Diagram](#f-high-level-system-architecture-diagram)

## 1. Introduction

![Abstract UIM architecture](images/abstract.png)

### 1.1 Motivation

As Artificial Intelligence (AI) technology advances, there is a growing need for efficient, standardized interactions between AI agents and web services. Traditional methods such as web scraping and simulated user interactions are inefficient, unreliable, and often non-compliant with legal and ethical standards.

#### Challenges in Current AI-Agent Interactions

1. **Web Scraping Issues**
   - **Inconsistency**: Unpredictable changes in HTML structures lead to data extraction failures.
   - **Legal and Ethical Concerns**: Potential violations of terms of service and data privacy laws.

2. **Simulated Browser Interactions**
   - **Performance Overhead**: High resource consumption affects scalability.
   - **Dynamic Content Handling**: Difficulty managing JavaScript-rendered content, pop-ups, and CAPTCHAs.

3. **Lack of Standardization**
   - **Diverse APIs**: Inconsistent API designs require custom integrations.
   - **Data Formats**: Multiple data formats necessitate different parsers.

4. **Limited Access to Deep Functionality**
   - **Restricted Features**: Inability to access advanced functionalities due to API and/or data limitations.
   - **Inefficient Automation**: Hinders the development of sophisticated AI capabilities.

5. **Security and Compliance Challenges**
   - **Complex Authentication**: Varied authentication mechanisms complicate integration.
   - **Regulatory Compliance**: Navigating data protection laws like GDPR or copyright issues is challenging.

![Challenges in AI-Agent interactions with web services](images/challenges-spec.png)

### 1.2 Scope

The Unified Intent Mediator (UIM) protocol addresses these challenges by introducing a standardized, secure method for direct AI agent-web service interaction. This specification aims to:

- **Define the structure and format of intents.**
- **Establish mechanisms for discovery and execution of intents.**
- **Integrate Open Digital Rights Language (ODRL) for policy management.**
- **Utilize Policy Adherence Tokens (PATs) for secure interactions.**
- **Provide comprehensive guidelines for implementation, ensuring interoperability and compliance.**

### 1.3 Out of Scope

While the Unified Intent Mediator (UIM) Protocol Specification aims to provide a comprehensive framework for AI agents to interact with web services, certain aspects are intentionally excluded to maintain focus and clarity. The following elements are not within the scope of this specification in its current version:

- **Implementation Details of AI Agents and Web Services**: The specification does not dictate the internal architecture or programming paradigms (e.g., object-oriented, functional programming) that AI agents or web services should adopt. It does not prescribe specific programming languages, frameworks, or libraries to be used in implementing the protocol.
- **Specific Authentication and Authorization Mechanisms**: Details regarding how credentials are stored, rotated, or managed are beyond the scope of this document.
- **Legal and Regulatory Compliance Beyond Data Privacy**: The specification does not cover compliance with laws beyond data privacy regulations like GDPR and CCPA. It excludes areas such as export controls, accessibility laws, and sector-specific regulations (e.g., HIPAA for healthcare). Issues related to copyright, trademarks, or patents are not addressed.
- **User Interface and Experience Design**: The specification does not prescribe how users should interact with AI agents or how agents present information to users.
- **Business Models and Economic Considerations**: While incorporating billing information into PATs is discussed, the specification does not guide on how services should price their intents or services. The specifics of service-level agreements (SLAs), terms of service (ToS), or contractual obligations beyond what’s included in ODRL policies are not covered.
- **Security Threat Modeling and Mitigation Techniques**: While high-level security considerations are included, specific threat models, vulnerability assessments, or detailed mitigation strategies (e.g., against SQL injection, cross-site scripting) are not.
- **Detailed Workflow Implementations**: It does not delve into the specific business logic that should be implemented within intents. Detailed workflows or sequence diagrams for complex processes are not provided beyond high-level overviews.

## 2. Terminology

- **Intent**: An action that can be performed by a web service, including metadata and parameters required for execution.  
- **Parameters**: Inputs required by an intent to perform its action, including name, type, and whether they are required.  
- **Service**: A web service that publishes its capabilities (intents) using the UIM protocol.  
- **Endpoint**: The API endpoint where an intent can be executed.  
- **Metadata**: Descriptive information about an intent, including its name, description, and category.
- **Policy Adherence Token (PAT)**: A token issued by a web service to an AI agent, encapsulating permissions, usage limits, and billing agreements.
- **AI Agent**: An application or service that uses intents to interact with web services.
- **Discovery Endpoint**: The API endpoint where AI agents can query for available intents.
- **Execution Endpoint**: The API endpoint where AI agents can execute intents.
- **Policy Endpoint**: The API endpoint where AI agents can request PATs from web services.
- **Open Digital Rights Language (ODRL)**: A standardized language for expressing policies governing the usage of digital content and services.
- **UIM License**: A set of rules and conditions that govern the usage of data returned by an intent, including permissions, prohibitions, and obligations.

## 3. Key Concepts

### 3.1 Intents

**Definition**: Intents are predefined actions that an AI agent can perform on a web service. They encapsulate specific tasks, including necessary parameters and execution details.

**Examples**:

- **SearchProducts**
- **GetProductDetails**
- **PlaceOrder**

#### Unique Intent Identifier (UID) Format

The UID ensures that AI agents can uniquely identify and call intents from different service providers.

**Format**:

```js
namespace:intent_name:version
```

- **namespace**: Typically the domain or unique identifier of the service provider.
- **intent_name**: A descriptive and unique name within the namespace.
- **version**: Indicates the version of the intent.

**Examples**:

- `ecommerce.com:SearchProducts:v1`
- `weather.com:GetForecast:v2`

### 3.2 Metadata and Parameters

Each intent includes:

- **Metadata**: Name, description, category, and tags.
- **Input Parameters**: Required to execute the intent.
- **Output Parameters**: Expected results from the intent execution.

![Intent](images/intent-format.png)

**Example**:

```json
{
  "intent_uid": "ecommerce.com:SearchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on criteria",
  "input_parameters": [
    {"name": "query", "type": "string", "required": true, "description": "Search term"},
    {"name": "category", "type": "string", "required": false, "description": "Product category"},
    {"name": "price_range", "type": "string", "required": false, "description": "Price range filter"},
    {"name": "sort_by", "type": "string", "required": false, "description": "Sorting criteria"}
  ],
  "output_parameters": [
    {"name": "products", "type": "array", "description": "List of products"},
    {"name": "total_results", "type": "integer", "description": "Total number of results"}
  ],
  "endpoint": "https://api.ecommerce.com/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

### 3.3 The Execute Method

Responsible for:

1. **Input Validation**: Ensuring all required parameters are present and correctly formatted.
2. **Authentication**: Verifying the AI agent's identity and PAT.
3. **Authorization**: Ensuring the AI agent has the necessary permissions as per the PAT and policies.
4. **Execution**: Performing the action defined by the intent.
5. **Response Formatting**: Standardizing the response for consistent interpretation by AI agents.
6. **Error Handling**: Managing exceptions and providing meaningful feedback.

![The execution method](images/execute-method.png)

### 3.4 Policy Adherence Tokens (PATs)

**Definition**: Digitally signed tokens that encapsulate permissions, usage limits, billing agreements, and compliance terms. They ensure secure and compliant interactions between AI agents and web services.

### 3.5 AI Agents

**Definition**: Applications or services that utilize intents to interact with web services.

**Responsibilities**:

- **Discovery**: Finding available intents and services.
- **Policy Agreement**: Requesting and managing PATs.
- **Execution**: Performing intents according to policies.

![AI-agent responsibilities](images/ai-discovery.png)

## 4. System Architecture

### 4.1 Centralized Architecture

#### Overview

A central repository manages:

- **Intent Registration**: Web services register their intents with the central repository.
- **Discovery**: AI agents discover intents via the central system.
- **Execution**: AI agents execute intents through the central system, which forwards requests to the appropriate web service.
- **Policy Management**: Centralized issuance and validation of PATs.

#### Workflow Description

1. **Service Registration**: Web services register their intents and policies with the central repository.
2. **Intent Discovery**: AI agents query the central repository to discover available intents.
3. **Policy Agreement**: AI agents obtain PATs from the central repository after agreeing to policies.
4. **Execution**: AI agents execute intents via the central repository.
5. **Response Handling**: The central repository forwards responses from web services to AI agents.

![Centralized Architecture](images/central-arch.png)

#### Pros and Cons

- **Pros**:
  - Simplified discovery and integration for AI agents.
  - Unified policy enforcement and compliance management.
- **Cons**:
  - Single point of failure.
  - Scalability challenges with increasing load.
  - Potential bottleneck affecting performance.

### 4.2 Decentralized Architecture

#### Overview

AI agents interact directly with web services without a central intermediary.

#### Workflow Description

1. **Discovery via DNS TXT and `agents.json`**: AI agents discover web services through DNS records and retrieve `agents.json` files.
2. **Policy Retrieval and Agreement**: AI agents obtain ODRL policies and request PATs directly from web services.
3. **Intent Execution**: AI agents execute intents directly with web services using the obtained PATs.
4. **Response Handling**: Web services respond directly to AI agents.

![Decentralized Architecture](images/decentral-arch.png)

#### Pros and Cons

- **Pros**:
  - Enhanced scalability due to distributed interactions.
  - Greater control and autonomy for web services.
- **Cons**:
  - Increased complexity for AI agents managing diverse policies.
  - Potential inconsistencies in policy enforcement across services.

### 4.3 Hybrid Approach

#### Overview

Combines centralized discovery with decentralized execution and PAT issuance.

#### Workflow Description

1. **Centralized Discovery**: AI agents use the central repository to discover available intents and services.
2. **Decentralized Policy Agreement**: AI agents retrieve policies and obtain PATs directly from web services.
3. **Direct Execution**: AI agents execute intents directly with web services using the obtained PATs.
4. **Response Handling**: Web services respond directly to AI agents.

![Hybrid Approach](images/hybrid-arch.png)

#### Pros and Cons

- **Pros**:
  - Efficient discovery through a centralized system.
  - Maintains autonomy and control for web services in execution and policy management.
- **Cons**:
  - Coordination complexity between central and decentralized components.
  - Diverse compliance requirements increase AI agent complexity.

## 5. Core Components

### 5.1 Intent Discovery and Execution Endpoints

#### Purpose

Enable AI agents to:

- **Discover** available intents.
- **Execute** intents securely.

#### Implementation

- **Centralized Context**: Unified discovery endpoint managed by the central repository.
- **Decentralized Context**: Each web service hosts its own discovery and execution endpoints.
- **Hybrid Context**: Centralized discovery with decentralized execution endpoints.

#### API Endpoints

1. **Intent Discovery**

   - **Endpoint**: `/api/intents/search`
   - **Method**: `GET`
   - **Parameters**:
     - `query`: Natural language search term.
     - `service_name`
     - `intent_name`
     - `uid`
     - `namespace`
     - `description`
     - `tags`

   **Example Request**:

   ```curl
   GET /api/intents/search?intent_name=SearchProducts
   ```

   **Example Response**:

   ```json
   {
     "intents": [
       {
         "service_name": "E-commerce Platform",
         "intent_name": "SearchProducts",
         "intent_uid": "ecommerce.com:SearchProducts:v1",
         "description": "Search for products based on criteria",
         "input_parameters": [
           {"name": "query", "type": "string", "required": true}
         ],
         "output_parameters": [
           {"name": "products", "type": "array", "description": "List of products"}
         ],
         "endpoint": "https://api.ecommerce.com/products/search",
         "tags": ["e-commerce", "search", "products"]
       }
     ]
   }
   ```

2. **Execute Intent**

   - **Endpoint**: `/api/intents/execute`
   - **Method**: `POST`
   - **Headers**:
     - `Authorization`: Bearer PAT-12345
     - `Content-Type`: application/json

   **Example Request**:

   ```json
   POST /api/intents/execute
   Authorization: Bearer PAT-12345
   Content-Type: application/json

   {
     "intent_uid": "ecommerce.com:SearchProducts:v1",
     "parameters": {
       "query": "laptops"
     }
   }
   ```

   **Example Response**:

   ```json
   {
     "products": [
       {
         "product_id": "123",
         "name": "Gaming Laptop",
         "price": 1500
       },
       {
         "product_id": "124",
         "name": "Ultrabook",
         "price": 1200
       }
     ],
     "total_results": 2
   }
   ```

### 5.2 Unique Intent Identifier (UID) Format

As detailed in [Section 3.1](#31-intents), the UID format is crucial for unique identification.

### 5.3 Intent Metadata

Metadata provides detailed information about an intent, helping AI agents understand how to interact with it.

**Fields**:

- `intent_uid`
- `intent_name`
- `description`
- `input_parameters`
- `output_parameters`
- `endpoint`
- `tags`
- `service_info`

### 5.4 Discovery Through DNS TXT Records and `agents.json` Files

#### Purpose

Facilitate service discovery in a decentralized architecture.

#### DNS TXT Records

Provide quick discovery of services and pointers to detailed information.

**Fields**:

1. **uim-agents-file**: URL of the `agents.json` file.
2. **uim-api-discovery**: URL of the API discovery endpoint.
3. **uim-policy-file**: URL of the ODRL policy file.
4. **uim-license**: The UIM license for the service.

**Example Record**:

```txt
uim-agents-file=https://example.com/agents.json
uim-api-discovery=https://api.example.com/intents/search
uim-policy-file=https://example.com/uim-policy.json
uim-license=https://uimprotocol.com/licenses/uim-by-nc-v1.0
```

#### `agents.json` Files

Contain detailed information about the service and available intents.

**Structure**:

- **service-info**
- **intents**
- **uim-public-key**
- **uim-policy-file**
- **uim-api-discovery**
- **uim-compliance**
- **uim-license**

**Complete `agents.json` File Example** is provided in [Appendix B](#b-complete-agentsjson-file-example).

### 5.5 Policy Adherence Tokens (PATs) and ODRL Integration

#### Purpose

Ensure secure, compliant interactions by encapsulating policies, permissions, and obligations.

#### ODRL Integration

Utilize the **Open Digital Rights Language (ODRL)** to define policies. A comprehensive [ODRL vocabulary draft document](uim-odrl-vocab.md) is provided for the UIM protocol namespace. It defines namespaces, vocabulary terms, JSON-LD context, and policy examples. It also includes recommendations for implementers and references for further reading.

**Key Concepts**:

- **Policy**: Represents the agreement between AI agents and web services, detailing permissions, prohibitions, and obligations.
- **Permission**: Specifies allowed actions for AI agents.
- **Prohibition**: Specifies actions that AI agents are not allowed to perform.
- **Obligation**: Specifies actions that AI agents must perform under certain conditions.
- **Asset**: The resource or service the policy applies to.
- **Party**: The entities involved in the policy (e.g., AI agents and web services).

**Sample ODRL Policy** is provided in [Appendix C](#c-sample-odrl-policy).

#### PAT Issuance Workflow with ODRL policies

1. **Policy Retrieval and Agreement**:
   - AI agent retrieves the ODRL policy from the specified endpoint.
   - AI agent digitally signs the policy using its private key and sends it to the web service alongside its public key to request a PAT.

2. **PAT Issuance**:
   - Web service verifies the AI agent's signature and agreement.
   - Web service issues a PAT, which includes the agreed policy details, permissions, obligations, and a validity period.
   - The PAT is digitally signed by the web service.

3. **Using PAT in Requests**:
   - AI agent includes the PAT in the `Authorization` header of each request.
   - Web service verifies the PAT's signature and validity before processing the request.

**PAT Structure**:

**Sample PAT** is provided in [Appendix D](#d-sample-pat-structure).

#### Including PAT in Requests

The AI agent includes the PAT in the `Authorization` header:

```txt
Authorization: Bearer PAT-12345
```

#### Verification Process

1. **Extract PAT**: Web service extracts the PAT from the request header.
2. **Verify Signature**: Web service verifies the PAT's signature using its public key.
3. **Check Validity**: Web service checks the PAT's validity period.
4. **Authorize Request**: Web service checks if the PAT permissions match the requested action.
5. **Process Request**: If valid, the web service processes the request; otherwise, it rejects it.

### 5.6 Incorporating Billing Information into PATs

#### Purpose

Simplifies transactions by including billing details within the PAT.

#### Workflow

1. **Billing Information Submission**: AI agent submits billing info during PAT request.
2. **PAT Issuance**: PAT includes the agreed policy details, permissions, obligations, and a validity period.
3. **Automated Billing**: Web service processes payments automatically as intents are executed.

**Benefits**:

- Streamlined process.
- Automated billing.
- Improved user experience.
- Enhanced compliance.

### 5.7 Policy Adherence Tokens (PATs) and UIM Policy Scheme Integration

#### Purpose

The [UIM Licensing Scheme](uim-licensing-scheme.md) aims to standardize how licensing information is conveyed in the agents.json file, providing a clear, machine-readable format that AI agents can interpret to understand the legal and commercial restrictions around data usage. It simplifies the licensing process and offers web services a straightforward way to communicate their terms without the need to define a complete ODRL policy.

#### PAT Issuance Workflow with UIM Licenses

Web services can provide a custom license using the `uim-license` property, which allows them to define permissions, conditions, and restrictions in a simplified manner, tailored to their specific needs. AI agents can then interpret this license to understand the terms and conditions of data usage.

When an AI agent interacts with a web service, it should first check for a `uim-license`. If both the uim-license property and an ODRL policy are specified, the ODRL policy takes precedence for defining permissions, prohibitions, and obligations.

1. **License Retrieval and Agreement**:
   - **AI Agent retrieves the UIM license** from the specified endpoint or resource metadata (e.g., `agents.json`).
   - **AI Agent notes the license reference**, including:
     - **License Code** (e.g., `UIM-BY-NC-v1.0`).
     - **License URL** (e.g., `https://uimprotocol.com/licenses/uim-by-nc-v1.0`).
   - **AI Agent prepares an authorization request** that refers directly to the license:
     - **License Reference**: Includes the license URL.
     - **Agreement Assertion**: Indicates agreement to comply with the entire license.
     - **Digital Signature (Optional)**: May digitally sign the license reference to confirm agreement and authenticity.

2. **PAT Issuance**:
   - **Authorization Server evaluates the AI Agent's request**:
     - **Verifies the license reference** is valid and recognized.
     - **Confirms the agent's agreement** to comply with the license.
     - **No need for detailed scopes and claims**: The license itself defines the permissions, conditions, and prohibitions.
   - **Authorization Server issues a PAT**, which includes:
     - **License Reference**: The license URL of the agreed-upon license.
     - **Validity Period**: Specifies how long the PAT is valid.
     - **Token Signature**: The PAT is digitally signed by the authorization server to ensure integrity and authenticity.

3. **Using PAT in Requests**:
   - **AI Agent includes the PAT** in the `Authorization` header of each request to the web service:
  
     ```http
     Authorization: Bearer <PAT_token>
     ```

   - **Web Service verifies the PAT's signature and validity** before processing each request:
     - **Validates the token's signature** to confirm it was issued by the trusted authorization server.
     - **Checks the token's expiration** to ensure it is still valid.
     - **Retrieves the license reference** from the PAT and verifies it is still valid and recognized. If not, the web service may reject the request.
   - **Web Service processes the request** if the PAT is valid.

**Notes**:

- **Optional Digital Signature**: While not required in this flow, the agent may digitally sign the policy reference or the authorization request to provide an additional layer of assurance regarding the agent's identity and agreement.

- **Dynamic Licenses**: If license are subject to change, the license reference should include a version number or timestamp to ensure both parties are referencing the same license terms.

### 5.8 Service Management APIs

APIs that allow web services to manage their registration, including creating, updating, and deleting services. Used in the centralized architecture.

#### Register Service

- **Endpoint**: `/api/services`
- **Method**: `POST`
- **Description**: Registers a new service.

**Request Body**:

```json
{
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities",
  "service_terms_of_service_url": "https://api.ecommerce.com/terms",
  "service_privacy_policy_url": "https://api.ecommerce.com/privacy",
  "service_logo_url": "https://api.ecommerce.com/logo.png"
}
```

#### Update Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: `PUT`
- **Description**: Updates an existing service.

#### Delete Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: `DELETE`
- **Description**: Deletes a registered service.

#### Retrieve Service

- **Endpoint**: `/api/services/{service_id}`
- **Method**: `GET`
- **Description**: Retrieves the details of a registered service.

### 5.9 Intent Management APIs

APIs for web services to manage their intents. Used in the centralized architecture.

#### List All Intents for a Service

- **Endpoint**: `/api/services/{service_id}/intents`
- **Method**: `GET`
- **Description**: Lists all intents for a specific service.

#### Retrieve Intent Details

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: `GET`
- **Description**: Retrieves the details of a specific intent.

#### Create Intent

- **Endpoint**: `/api/services/{service_id}/intents`
- **Method**: `POST`
- **Description**: Creates a new intent for a service.

**Request Body**:

```json
{
  "intent_uid": "ecommerce.com:GetProductDetails:v1",
  "intent_name": "GetProductDetails",
  "description": "Fetches detailed information about a specific product using its unique identifier",
  "input_parameters": [
    {"name": "product_id", "type": "string", "required": true}
  ],
  "output_parameters": [
    {"name": "product_details", "type": "object", "required": true}
  ],
  "endpoint": "https://api.ecommerce.com/products/details",
  "tags": ["e-commerce", "product", "details"]
}
```

#### Update Intent

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: `PUT`
- **Description**: Updates the details of an existing intent.

#### Delete Intent

- **Endpoint**: `/api/intents/{intent_uid}`
- **Method**: `DELETE`
- **Description**: Deletes an existing intent.

## 6. General API Guidelines and Standards

### 6.1 Pagination

To handle large data sets, list endpoints support pagination.

#### Parameters

- **page**: Page number (default: 1).
- **page_size**: Items per page (default: 10).

**Example Request**:

```curl
GET /api/services/12345/intents?page=2&page_size=5
```

#### Response Headers

- **X-Total-Count**
- **X-Total-Pages**
- **X-Current-Page**
- **X-Page-Size**

### 6.2 Security and Compliance

- **Authentication**: Use OAuth 2.0 for secure authentication.
- **Encryption**: All communications MUST use HTTPS.
- **Compliance**: Adhere to regulations like GDPR and CCPA.
- **Data Protection**: Implement data encryption at rest and in transit.

### 6.3 Monitoring and Analytics

- **Real-time Monitoring**: Provide dashboards for API usage and performance.
- **Logging and Alerts**: Implement systems to track activity and respond to issues.
- **Audit Trails**: Maintain logs for compliance and troubleshooting.

### 6.4 Scalability

- **Caching**: Implement caching mechanisms for frequently accessed data.
- **Load Balancing**: Distribute traffic efficiently to handle high volumes.
- **Auto-scaling**: Utilize auto-scaling to adjust resources based on demand.

### 6.5 Error Management Strategy

#### Comprehensive Error Handling Approach

- **Layered Error Handling**:
  1. **Client-Side Errors (4xx)**: Issues with the client's request.
  2. **Server-Side Errors (5xx)**: Issues on the server side.
  3. **Protocol-Level Errors**: Specific to UIM protocol operations.

#### Standard Error Response Structure

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Descriptive error message.",
    "details": {
      "additional": "context-specific information"
    }
  }
}
```

**Detailed error codes and messages** are provided in [Appendix A](#a-standard-error-codes-and-messages).

#### Error Handling Guidelines

- **Consistent Structure**: Ensure all error responses follow the standard format.
- **Clear Messages**: Provide descriptive and actionable error messages.
- **Security Considerations**: Avoid exposing sensitive internal details.
- **Documentation**: Document all error codes and scenarios.

## 7. Practical Examples and Use Cases

### 7.1 E-commerce Platform Integration

**Scenario**: An AI shopping assistant helps users find products across multiple e-commerce platforms.

**Workflow**:

1. **Discovery**: The AI agent searches for the `SearchProducts` intent across registered e-commerce services.
2. **Policy Agreement**: The agent retrieves the ODRL policy and obtains a PAT from each service.
3. **Execution**: The agent executes the `SearchProducts` intent with user-provided criteria.
4. **Aggregation**: Results from multiple platforms are aggregated and presented to the user.
5. **Purchase**: The user selects a product, and the agent uses the `PlaceOrder` intent to complete the purchase.

![Ecommerce Example](images/ecommerce-example.png)

**Benefits**:

- **User Convenience**: One-stop shop across multiple platforms.
- **Service Monetization**: E-commerce platforms gain additional sales channels.

### 7.2 Real Estate Data Retrieval

**Scenario**: A real estate analytics tool aggregates property data for market analysis.

**Workflow**:

1. **Discovery**: The AI agent discovers real estate services offering the `SearchProperty` intent.
2. **Policy Agreement**: The agent agrees to policies and obtains PATs.
3. **Data Retrieval**: Executes `SearchProperty` intents to gather property listings.
4. **Analysis**: Aggregates and analyzes data to provide market insights.
5. **Compliance**: Ensures data usage complies with service policies.

![Real Estate Example](images/realestate-example.png)

**Benefits**:

- **Comprehensive Data**: Access to diverse property listings.
- **Enhanced Analytics**: Improved market analysis capabilities.

## 8. Security Considerations

- **Authentication and Authorization**: AI agents MUST authenticate using secure methods like OAuth 2.0. Web services MUST verify PATs and ensure that AI agents have the necessary permissions.
- **Data Integrity**: All tokens and sensitive data SHOULD be digitally signed to prevent tampering.
- **Confidentiality**: Sensitive information, including billing details, MUST be encrypted and securely stored.
- **Replay Attacks**: PATs SHOULD include nonce values or timestamps to prevent replay attacks.
- **Input Validation**: Web services MUST validate all inputs to prevent injection attacks.

## 9. Privacy Considerations

- **Data Minimization**: AI agents and web services SHOULD minimize the collection and storage of personal data.
- **Compliance**: Adherence to regulations like GDPR and CCPA is REQUIRED where applicable.
- **User Consent**: When personal data is involved, explicit user consent MUST be obtained.
- **Transparency**: Privacy policies SHOULD be clearly communicated through the `service_privacy_policy_url`.
- **Anonymization**: Where possible, data SHOULD be anonymized to protect user identities.

## 10. Appendix

### A. Standard Error Codes and Messages

#### Client-Side Errors (4xx)

| Error Code             | Message                                                    | Description                                |
|------------------------|------------------------------------------------------------|--------------------------------------------|
| INVALID_PARAMETER      | "The parameter '{param}' is required."                     | Missing or invalid parameter.              |
| UNAUTHORIZED           | "Unauthorized access. Authentication is required."         | Missing or invalid authentication token.   |
| FORBIDDEN              | "Access to this resource is forbidden."                    | Insufficient permissions.                  |
| NOT_FOUND              | "The requested resource '{resource}' was not found."       | Resource not found.                        |
| METHOD_NOT_ALLOWED     | "The HTTP method '{method}' is not allowed for this endpoint." | Unsupported HTTP method.                   |
| CONFLICT               | "The request could not be completed due to a conflict."    | Resource conflict.                         |
| UNSUPPORTED_MEDIA_TYPE | "The media type '{type}' is not supported."                | Unsupported content type.                  |

#### Server-Side Errors (5xx)

| Error Code              | Message                                                   | Description                      |
|-------------------------|-----------------------------------------------------------|----------------------------------|
| INTERNAL_SERVER_ERROR   | "An unexpected error occurred on the server."             | Generic server error.            |
| SERVICE_UNAVAILABLE     | "The service is temporarily unavailable."                 | Server down or overloaded.       |
| GATEWAY_TIMEOUT         | "The server did not receive a timely response."           | Upstream server timeout.         |
| NOT_IMPLEMENTED         | "The requested functionality is not implemented."         | Feature not supported.           |

#### Protocol-Level Errors

| Error Code              | Message                                                   | Description                                |
|-------------------------|-----------------------------------------------------------|--------------------------------------------|
| INTENT_EXECUTION_FAILED | "The intent '{intent}' could not be executed."            | Execution failure due to various reasons.  |
| INTENT_NOT_SUPPORTED    | "The intent '{intent}' is not supported by this service." | Intent not recognized or supported.        |
| VERSION_CONFLICT        | "The intent version '{version}' is not supported."        | Version mismatch.                          |
| INTENT_DEPRECATED       | "The intent '{intent}' has been deprecated."              | Intent no longer available.                |

### B. Complete `agents.json` File Example

```json
{
  "service-info": {
    "name": "fakerealestate.com",
    "description": "Provides property listings and real estate data.",
    "service_url": "https://fakerealestate.com",
    "service_logo_url": "https://fakerealestate.com/logo.png",
    "service_terms_of_service_url": "https://fakerealestate.com/terms",
    "service_privacy_policy_url": "https://fakerealestate.com/privacy"
  },
  "intents": [
    {
      "intent_uid": "fakerealestate.com:SearchProperty:v1",
      "intent_name": "SearchProperty",
      "description": "Search properties based on criteria",
      "input_parameters": [
        {"name": "location", "type": "string", "required": true, "description": "City or ZIP code"},
        {"name": "min_price", "type": "integer", "required": false, "description": "Minimum price"},
        {"name": "max_price", "type": "integer", "required": false, "description": "Maximum price"},
        {"name": "property_type", "type": "string", "required": false, "description": "Type of property"}
      ],
      "output_parameters": [
        {"name": "properties", "type": "array", "description": "List of matching properties"},
        {"name": "total_results", "type": "integer", "description": "Total number of results"}
      ],
      "endpoint": "https://fakerealestate.com/api/execute/SearchProperty",
      "tags": ["real estate", "search"],
      "rate_limit": "1000/hour",
      "price": "0.01 USD"
    }
    // Additional intents can be added here
  ],
  "uim-public-key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQE...",
  "uim-policy-file": "https://fakerealestate.com/uim-policy.json",
  "uim-api-discovery": "https://fakerealestate.com/uim/intents/search",
  "uim-compliance": {
    "standards": ["ISO27001", "GDPR"],
    "regional-compliance": {
      "EU": "GDPR",
      "US-CA": "CCPA"
    },
    "notes": "Data is encrypted in transit and at rest."
  },
  "uim-license": "https://uimprotocol.com/licenses/uim-by-nc-v1.0"
}
```

### C. Sample ODRL Policy

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "uid": "http://fakerealestate.com/policy/12345",
  "type": "Set",
  "permission": [
    {
      "target": "http://fakerealestate.com/api/intents",
      "action": "execute",
      "constraint": [
        {
          "leftOperand": "http://fakerealestate.com/vocab/rateLimit",
          "operator": "lte",
          "rightOperand": 1000,
          "unit": "http://fakerealestate.com/vocab/hour"
        }
      ],
      "duty": [
        {
          "action": "pay",
          "target": "http://fakerealestate.com/vocab/intentPrice",
          "amount": 0.01,
          "unit": "http://fakerealestate.com/vocab/USD"
        }
      ]
    }
  ],
  "prohibition": [
    {
      "target": "http://fakerealestate.com/api/intents",
      "action": "exceedRateLimit"
    }
  ],
  "obligation": [
    {
      "action": "signPayload",
      "assignee": "http://aiagent.com/agent/1",
      "target": "http://fakerealestate.com/vocab/payload",
      "constraint": [
        {
          "leftOperand": "http://fakerealestate.com/vocab/publicKey",
          "operator": "use",
          "rightOperand": "MIIBIjANBgkqh..."
        }
      ]
    }
  ],
  "party": [
    {
      "function": "assigner",
      "identifier": "http://fakerealestate.com"
    },
    {
      "function": "assignee",
      "identifier": "http://aiagent.com/agent/1"
    }
  ],
  "asset": "http://fakerealestate.com/api/intents"
}
```

### D. Sample PAT Structure

```json
{
  "pat": {
    "uid": "pat-12345",
    "issued_to": "ai-agent-1",
    "issued_by": "fakerealestate.com",
    "policy_reference": "http://fakerealestate.com/policy/12345",
    "permissions": ["execute:intent/SearchProperty"],
    "obligations": ["pay:0.01 USD per intent"],
    "billing_info": {
      "payment_method": "credit_card",
      "billing_address": "123 AI Street, Tech City",
      "currency": "USD"
    },
    "valid_from": "2024-01-01T00:00:00Z",
    "valid_to": "2024-12-31T23:59:59Z"
  },
  "signature": "Base64-encoded-digital-signature"
}
```

### E. Sample API Requests and Responses

#### Intent Discovery Request

```curl
GET /api/intents/search?intent_name=SearchProperty
```

#### Intent Discovery Response

```json
{
  "intents": [
    {
      "service_name": "Fake Real Estate",
      "intent_name": "SearchProperty",
      "intent_uid": "fakerealestate.com:SearchProperty:v1",
      "description": "Search properties based on criteria",
      "input_parameters": [
        {"name": "location", "type": "string", "required": true}
      ],
      "output_parameters": [
        {"name": "properties", "type": "array", "description": "List of properties"}
      ],
      "endpoint": "https://fakerealestate.com/api/execute/SearchProperty",
      "tags": ["real estate", "search"]
    }
  ]
}
```

#### Execute Intent Request

```json
POST /api/intents/execute
Authorization: Bearer PAT-12345
Content-Type: application/json

{
  "intent_uid": "fakerealestate.com:SearchProperty:v1",
  "parameters": {
    "location": "New York",
    "min_price": 500000,
    "max_price": 1000000
  }
}
```

#### Execute Intent Response

```json
{
  "properties": [
    {
      "property_id": "NYC123",
      "address": "123 Main St, New York, NY",
      "price": 750000,
      "property_type": "Apartment"
    },
    {
      "property_id": "NYC124",
      "address": "456 Broadway, New York, NY",
      "price": 850000,
      "property_type": "Condo"
    }
  ],
  "total_results": 2
}
```

### F. High Level System Architecture Diagram

1. **Centralized Architecture**:

   - **AI Agent** interacts with the **Central Repository** for discovery, policy agreement, and execution.
   - **Central Repository** communicates with **Web Services** to forward execution requests and receive responses.
  ![Centralized flow](images/central-arch-box.png)

2. **Decentralized Architecture**:

   - **AI Agent** discovers **Web Services** via DNS TXT records and `agents.json` files.
   - **AI Agent** communicates directly with **Web Services** for policy agreement and intent execution.
  ![Decentralized flow](images/decentral-arch-box.png)

3. **Hybrid Approach**:

   - **AI Agent** uses the **Central Repository** for intent discovery.
   - **AI Agent** interacts directly with **Web Services** for policy agreement and execution.
  ![Hybrid flow](images/hybrid-arch-box.png)

---

## Milestones for the UIM Protocol Development

The UIM Protocol is intended to be a community-driven and open standards project. The development of the protocol will be divided into five phases, each with specific milestones and goals. The following sections outline the milestones for each phase.

### **Phase 1: Draft Proposal and Initial Community Feedback**

- **Milestone 1.1**: Publish the Draft Proposal
  - Publish the initial draft of the UIM Protocol on GitHub, outlining the core components, specifications, and goals.
- **Milestone 1.2**: Community Engagement and Outreach
  - Launch the Discord server and start discussions on GitHub. Share the proposal on social media and tech communities.
- **Milestone 1.3**: Gather Feedback and Conduct Surveys
  - Encourage community feedback through GitHub issues, discussions, and feedback forms to identify key concerns and suggestions.

### **Phase 2: Refinement and Iterative Updates**

- **Milestone 2.1**: Analyze Feedback and Prioritize Changes
  - Review feedback, prioritize updates, and refine the protocol’s design and documentation based on community input.
- **Milestone 2.2**: Release Updated Drafts
  - Publish updated drafts addressing key feedback points and improvements. Highlight changes and continue discussions.
- **Milestone 2.3**: Host Webinars and Q&A Sessions
  - Organize sessions to discuss updates, answer questions, and engage directly with contributors.

### **Phase 3: Testing and Proof-of-Concept Implementations**

- **Milestone 3.1**: Develop Proof-of-Concept Implementations
  - Build example AI agents and web services using the protocol to validate functionality and identify gaps.
- **Milestone 3.2**: Community Testing and Bug Reporting
  - Encourage community members to test implementations, raise issues, and contribute code or documentation improvements.
- **Milestone 3.3**: Security and Compliance Review
  - Conduct a detailed review of security features and compliance mechanisms to ensure robustness.

### **Phase 4: Final Refinements and Preparation for v1.0 Release**

- **Milestone 4.1**: Finalize the Protocol Specification
  - Incorporate feedback from testing and finalize all sections of the specification.
- **Milestone 4.2**: Complete Documentation and Guides
  - Develop comprehensive documentation, including installation guides, API references, and best practice guides.
- **Milestone 4.3**: Pre-Release Candidate
  - Release a pre-v1.0 candidate version for final review by the community.

### **Phase 5: Version 1.0 Release and Promotion**

- **Milestone 5.1**: Official v1.0 Release
  - Publish the final version of the UIM Protocol, including all associated resources.
- **Milestone 5.2**: Launch Campaign and Public Announcements
  - Announce the v1.0 release across all channels, including social media, tech forums, newsletters, and webinars.
- **Milestone 5.3**: Post-Release Support and Community Engagement
  - Continue engaging with the community, support early adopters, and gather feedback for future updates.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
```

--------------------------------------------------------------------------------

### File: faq.md
```
Path: faq.md
Size: 3.15 KB
Last Modified: 2024-09-20 16:49:44
```

**Contents:**
```
# Unified Intent Mediator (UIM) Protocol: FAQ

### 1. What is the Unified Intent Mediator (UIM) Protocol?
The Unified Intent Mediator (UIM) Protocol is a standardized framework designed to streamline interactions between AI agents and web services. It defines a common language and set of rules for communication, allowing AI agents to discover, understand, and execute actions (called "intents") offered by various web services in a secure, compliant, and efficient manner.

### 2. How does the UIM Protocol work in a decentralized architecture?
In a decentralized architecture, web services publish their capabilities as "intents" through DNS TXT records and agents.json files. AI agents then crawl these resources to discover and interact directly with web services, eliminating the need for a central intermediary. This approach offers scalability, autonomy, and preserves data ownership for web services.

### 3. What are Policy Adherence Tokens (PATs) and why are they important?
PATs are digitally signed tokens issued by web services to AI agents, granting them permission to execute specific actions. These tokens encapsulate compliance requirements, usage limits, and billing agreements, ensuring secure and regulated interactions. PATs streamline policy enforcement and simplify billing processes within the UIM ecosystem.

### 4. How does the UIM Protocol handle billing and monetization?
The UIM Protocol supports various monetization strategies, including transaction fees, usage-based billing, subscription models, and revenue-sharing partnerships. Web services have the flexibility to choose the most suitable model for their offerings, while the protocol ensures secure and transparent billing processes.

### 5. What is the role of ODRL in the UIM Protocol?
The Open Digital Rights Language (ODRL) is integrated into the UIM Protocol to provide a standardized way to define and manage permissions, prohibitions, and obligations between AI agents and web services. This integration ensures clear, verifiable, and enforceable policies, enhancing security and compliance within the ecosystem.

### 6. What are the benefits of using a hybrid architecture for the UIM Protocol?
A hybrid architecture combines centralized discovery with decentralized execution and PAT issuance. This approach offers the benefits of both worlds: a unified discovery mechanism for AI agents while preserving the autonomy, scalability, and customized security of decentralized interactions.

### 7. How does the UIM Protocol ensure security and compliance?
Security and compliance are paramount in the UIM Protocol. It utilizes HTTPS for secure communication, OAuth 2.0 for authentication, and enforces compliance with regulations like GDPR and CCPA. Additionally, PATs and ODRL integration strengthen security by defining and enforcing access control and usage policies.

### 8. How can I get involved in the development of the UIM Protocol?
The UIM Protocol is an open-source project, and community involvement is highly encouraged. You can contribute by reviewing the draft specification, joining discussions on platforms like Discord and GitHub, raising issues, submitting pull requests, and sharing the project with your network.
```

--------------------------------------------------------------------------------

### File: intent_examples.md
```
Path: intent_examples.md
Size: 28.69 KB
Last Modified: 2024-09-03 16:20:31
```

**Contents:**
```
# AI Agent Intent Examples

## AI-Agent Driven E-Commerce Integration for Personalized Shopping Experiences

* **searchProducts**: "Find products based on user preferences, keywords, and categories”  
  * Parameters: query (string), category (string, optional), priceRange (string, optional), sortBy (string, optional)  
* **getProductDetails**: "Retrieve detailed information about a specific product.”  
  * Parameters: productId (string)  
* **addToCart**: "Add a selected product to the user's shopping cart.”  
  * Parameters: productId (string), quantity (integer)  
* **checkoutCart**: "Proceed to checkout with the current items in the user's cart.”  
  * Parameters: paymentMethod (string), shippingAddress (string)  
* **trackOrder**: "Monitor the status of an order and provide updates.”  
  * Parameters: orderId (string)

## Financial Service Automation Using AI-Agent Driven Interactions

* **checkAccountBalance**: "Retrieve the current balance of the user's accounts.”  
  * Parameters: accountId (string)  
* **monitorTransactions**: "Track recent transactions and notify users of any unusual activity.”  
  * Parameters: accountId (string), startDate (string, optional), endDate (string, optional)  
* **transferFunds**: "Facilitate secure money transfers between accounts or to other users.”  
  * Parameters: fromAccountId (string), toAccountId (string), amount (float)  
* **payBill**: "Schedule and automate recurring bill payments.”  
  * Parameters: billerId (string), amount (float), dueDate (string)  
* **financialPlanning**: "Provide personalized financial advice and budgeting tips based on user spending patterns.”  
  * Parameters: accountId (string), goals (string, optional)

## AI-Agent Powered Social Media Content Management

* **schedulePost**: "Automate the scheduling and posting of content across multiple social media platforms.”  
  * Parameters: content (string), platforms (array of strings), scheduledTime (string)  
* **curateContent**: "Suggest relevant content for sharing based on trending topics and user interests.”  
  * Parameters: interests (array of strings), platforms (array of strings, optional)  
* **respondToComments**: "Automatically respond to comments and messages with predefined templates.”  
  * Parameters: postId (string), responseTemplate (string)  
* **analyzePerformance**: "Provide analytics and insights on post performance and audience engagement.”  
  * Parameters: postId (string), metrics (array of strings, optional)  
* **manageAdCampaigns**: "Create, monitor, and optimize social media advertising campaigns.”  
  * Parameters: campaignDetails (object), budget (float)

## Healthcare Service Booking and Management Through AI Agents

* **bookAppointment**: "Schedule medical appointments with healthcare providers.”  
  * Parameters: providerId (string), date (string), time (string), reason (string, optional)  
* **managePrescriptions**: "Track prescription refills and notify users when it’s time to renew.”   
  * Parameters: prescriptionId (string), refillDate (string)  
* **accessMedicalRecords**: "Retrieve and display the user's medical history and records.”   
  * Parameters: userId (string)  
* **symptomChecker**: "Provide initial diagnosis and health advice based on reported symptoms.”  
  * Parameters: symptoms (array of strings)  
* **healthReminders**: "Send reminders for medication, appointments, and health check-ups.”  
  * Parameters: reminderType (string), date (string), time (string)

## AI-Agent Enabled News and Media Content Curation

* **personalizedNewsFeed**: "Curate a personalized news feed based on user interests and preferences.”  
  * Parameters: interests (array of strings), sources (array of strings, optional)  
* **breakingNewsAlerts**: "Notify users of important news events as they happen.”   
  * Parameters: categories (array of strings, optional)  
* **summarizeArticle**: "Provide concise summaries of long articles for quick reading.”  
  * Parameters: articleUrl (string)  
* **saveForLater**: "Allow users to save articles and videos to view later.”  
  * Parameters: contentUrl (string)  
* **exploreTopics**: "Suggest related topics and articles based on user reading history.”  
  * Parameters: currentTopic (string)

## Secure Fund Transfer Systems Utilizing AI-Agent Interfaces

* **initiateTransfer**: "Facilitate secure transfers between user accounts and other recipients.”  
  * Parameters: fromAccountId (string), toAccountId (string), amount (float)  
* **trackTransfer**: "Monitor the status of fund transfers and provide updates to users.”  
  * Parameters: transferId (string)  
* **setTransferLimits**: "Allow users to set daily or monthly transfer limits for added security.”  
  * Parameters: accountId (string), limit (float)  
* **verifyRecipient**: "Confirm recipient details before completing transfers to prevent errors.”  
  * Parameters: recipientId (string)  
* **transactionHistory**: "Provide a detailed history of all past transfers for user reference.”  
  * Parameters: accountId (string), startDate (string, optional), endDate (string, optional)

## AI-Agent Powered Travel and Booking Platforms

* **searchFlights**: "Find and compare flights based on user preferences.”  
  * Parameters: origin (string), destination (string), departureDate (string), returnDate (string, optional)  
* **bookAccommodation**: "Reserve hotels or vacation rentals according to user criteria.”  
  * Parameters: location (string), checkInDate (string), checkOutDate (string), roomType (string, optional)  
* **createItinerary**: "Generate travel itineraries including flights, accommodations, and activities.”  
  * Parameters: tripDetails (object)  
* **trackBookings**: "Monitor booking statuses and send reminders for upcoming trips.”  
  * Parameters: bookingId (string)  
* **travelRecommendations**: "Suggest destinations, activities, and dining options based on user interests.”  
  * Parameters: interests (array of strings), location (string, optional)

## Automated Customer Support Through AI-Agent Interactions

* **answerFAQ**: "Provide instant responses to frequently asked questions.”  
  * Parameters: question (string)  
* **createSupportTicket**: "Create and track support tickets for user inquiries.”  
  * Parameters: issueDescription (string), priority (string, optional)  
* **liveChatSupport**: "Offer real-time chat support with AI-driven responses.”  
  * Parameters: userMessage (string)  
* **resolveIssue**: "Guide users through troubleshooting steps to resolve common issues.”  
  * Parameters: issueType (string)  
* **collectFeedback**: "Collect and analyze user feedback to improve services.”  
  * Parameters: feedback (string), rating (integer)

## AI-Agent Driven Data Analytics for Business Insights

* **generateReport**: "Create detailed business reports based on collected data.”  
  * Parameters: reportType (string), timePeriod (string, optional)  
* **predictiveAnalytics**: "Provide forecasts and predictive insights based on historical data.”  
  * Parameters: dataSetId (string), predictionType (string)  
* **identifyTrends**: "Highlight emerging trends and patterns in business data.”  
  * Parameters: dataSetId (string), trendType (string)  
* **trackKPIs**: "Monitor key performance indicators and alert users of any significant changes.”  
  * Parameters: kpi (string), threshold (float)  
* **dataVisualization**: "Present data in visually appealing charts and graphs for easier interpretation.”  
  * Parameters: dataSetId (string), visualizationType (string)

## AI-Agent Integration for Home Automation Systems

* **controlDevice**: "Manage and control smart home devices such as lights, thermostats, and security cameras.”  
  * Parameters: deviceId (string), command (string)  
* **automateRoutine**: "Set up and automate daily routines for home devices.”  
  * Parameters: routineName (string), schedule (string), devices (array of objects)  
* **monitorSecurity**: "Track home security status and send alerts for any suspicious activities.”  
  * Parameters: securityDeviceId (string)  
* **manageEnergyUsage**: "Optimize energy usage and provide recommendations for savings.”  
  * Parameters: deviceId (string), usageData (object)  
* **voiceControl**: "Enable voice control for various home automation tasks.”  
  * Parameters: command (string)

## AI-Agent Based Appointment Scheduling for Various Services

* **scheduleAppointment**: "Book appointments for services such as salons, car repairs, and healthcare.”  
  * Parameters: serviceId (string), date (string), time (string)  
* **manageCalendar**: "Sync appointments with user calendars and send reminders.”  
  * Parameters: calendarId (string)  
* **rescheduleAppointment**: "Allow users to easily reschedule appointments.”  
  * Parameters: appointmentId (string), newDate (string), newTime (string)  
* **cancelAppointment**: "Cancel scheduled appointments.”  
  * Parameters: appointmentId (string)  
* **recommendServices**: "Suggest related services or follow-up appointments based on user history.”  
  * Parameters: userId (string), currentService (string)

## AI-Agent Powered Online Education Platforms

* **recommendCourses**: "Suggest courses and learning materials based on user interests and progress. Parameters: userId (string), interests (array of strings)"  
* **trackProgress**: "Monitor user progress and provide feedback on performance. Parameters: userId (string), courseId (string)"  
* **automateGrading**: "Grade assignments and quizzes automatically. Parameters: courseId (string), assignmentId (string)"  
* **scheduleLessons**: "Arrange and remind users of upcoming lessons and study sessions. Parameters: courseId (string), lessonDate (string), lessonTime (string)"  
* **peerInteraction**: "Facilitate interactions with peers and instructors through forums and chat. Parameters: courseId (string), message (string)"

## AI-Agent Enabled Legal Service Consultations

* **bookConsultation**: "Schedule appointments with legal professionals. Parameters: lawyerId (string), date (string), time (string)"  
* **reviewDocuments**: "Upload and review legal documents with AI assistance. Parameters: documentId (string)"  
* **provideLegalAdvice**: "Provide preliminary legal advice based on user queries. Parameters: query (string)"  
* **trackCaseStatus**: "Monitor the status of ongoing legal cases. Parameters: caseId (string)"  
* **estimateCosts**: "Offer cost estimates for legal services based on user needs. Parameters: serviceType (string), details (object)"

## Personalized AI-Agent Driven Fitness and Wellness Platforms

* **recommendWorkouts**: "Suggest personalized workout plans based on user goals and fitness level. Parameters: userId (string), fitnessGoals (string)"  
* **trackFitnessProgress**: "Monitor and record fitness activities and progress. Parameters: userId (string), activityData (object)"  
* **provideNutritionAdvice**: "Provide dietary recommendations and meal plans. Parameters: userId (string), dietaryPreferences (string)"  
* **monitorHealthMetrics**: "Track vital health metrics and send alerts for any anomalies. Parameters: userId (string), healthData (object)"  
* **sendMotivationalReminders**: "Send motivational messages and reminders to keep users engaged. Parameters: userId (string), message (string)"

## AI-Agent Driven Job Search and Recruitment Platforms

* **recommendJobs**: "Suggest job listings based on user profile and preferences. Parameters: userId (string), jobPreferences (array of strings)"  
* **trackApplications**: "Monitor the status of job applications and send updates. Parameters: applicationId (string)"  
* **assistResumeBuilding**: "Help in creating and optimizing resumes and cover letters. Parameters: userId (string), resumeData (object)"  
* **prepareForInterviews**: "Provide tips and mock interview sessions to prepare users. Parameters: userId (string), interviewType (string)"  
* **suggestNetworkingOpportunities**: "Recommend networking events and professional connections. Parameters: userId (string), industry (string)"

## Real Estate Services Enhanced by AI-Agent Interactions

* **searchProperties**: "Find and compare properties based on user criteria. Parameters: location (string), propertyType (string), priceRange (string)"  
* **scheduleViewings**: "Arrange property viewings and send reminders. Parameters: propertyId (string), date (string), time (string)"  
* **estimatePropertyPrices**: "Provide market value estimates for properties. Parameters: propertyId (string)"  
* **manageDocuments**: "Assist in managing and reviewing real estate documents. Parameters: documentId (string)"  
* **matchAgents**: "Recommend real estate agents based on user preferences. Parameters: userId (string), location (string)"

## AI-Agent Powered Personal Finance Management Tools

* **trackBudget**: "Monitor and categorize expenses to help users stay within budget. Parameters: userId (string), budgetData (object)"  
* **setSavingsGoals**: "Set and track progress towards savings goals. Parameters: userId (string), goalAmount (float)"  
* **provideInvestmentAdvice**: "Offer personalized investment recommendations. Parameters: userId (string), investmentPreferences (string)"  
* **sendBillReminders**: "Notify users of upcoming bills and due dates. Parameters: userId (string), billDetails (object)"  
* **analyzeExpenses**: "Analyze spending patterns and suggest ways to save money. Parameters: userId (string), expenseData (object)"

## AI-Agent Based Entertainment and Media Recommendations

* **recommendContent**: "Suggest movies, TV shows, music, and books based on user preferences. Parameters: userId (string), contentType (string)"  
* **highlightTrendingContent**: "Show trending and popular content in various categories. Parameters: contentType (string)"  
* **createPersonalizedPlaylists**: "Generate and manage personalized playlists for music and videos. Parameters: userId (string), contentType (string)"  
* **notifyNewReleases**: "Alert users of new releases and upcoming content. Parameters: userId (string), contentType (string)"  
* **provideContentReviews**: "Offer reviews and ratings for various entertainment options. Parameters: contentId (string)"

## AI-Agent Enabled Event Planning and Management Platforms

* **discoverEvents**: "Find and suggest events based on user interests. Parameters: userId (string), eventType (string)"  
* **bookTickets**: "Facilitate ticket booking and payment for events. Parameters: eventId (string), ticketType (string)"  
* **manageEventSchedule**: "Organize and manage event schedules. Parameters: userId (string), eventDetails (object)"  
* **sendInvitations**: "Send and track invitations to events. Parameters: eventId (string), invitees (array of strings)"  
* **remindEvent**: "Notify users of upcoming events and any changes. Parameters: userId (string), eventId (string)"

## AI-Agent Powered Marketplace for Freelance Services

* **searchFreelancers**: "Find and compare freelance services based on user needs. Parameters: serviceType (string), location (string, optional)"  
* **hireFreelancer**: "Facilitate hiring and contract management for freelancers. Parameters: freelancerId (string), projectDetails (object)"  
* **trackProjectProgress**: "Monitor project progress and deliverables. Parameters: projectId (string)"  
* **processPayments**: "Handle payments and invoicing for freelance services. Parameters: projectId (string), amount (float)"  
* **collectReviews**: "Gather and display reviews and ratings for freelancers. Parameters: freelancerId (string), review (string), rating (integer)"

## AI-Agent Driven Supply Chain and Logistics Management

* **trackShipment**: "Monitor the status and location of shipments in real-time. Parameters: shipmentId (string)"  
* **manageInventory**: "Oversee inventory levels and send alerts for restocking. Parameters: warehouseId (string), productId (string)"  
* **processOrders**: "Automate order processing and fulfillment. Parameters: orderId (string)"  
* **evaluateSuppliers**: "Track and evaluate supplier performance. Parameters: supplierId (string)"  
* **optimizeLogistics**: "Provide recommendations for optimizing logistics and reducing costs. Parameters: logisticsData (object)"

## AI-Agent Enabled Customer Feedback and Survey Systems

* **createSurvey**: "Design and distribute customer surveys. Parameters: surveyDetails (object)"  
* **collectFeedback**: "Gather and analyze feedback from customers. Parameters: surveyId (string), customerId (string)"  
* **analyzeSentiment**: "Analyze customer feedback for sentiment and trends. Parameters: feedbackData (object)"  
* **generateReport**: "Produce detailed reports on survey results. Parameters: surveyId (string)"  
* **recommendActions**: "Suggest follow-up actions based on survey findings. Parameters: surveyId (string), recommendations (array of strings)"

## AI-Agent Powered Product Recommendation Engines

* **personalizedSuggestions**: "Provide personalized product recommendations based on user behavior. Parameters: userId (string), preferences (array of strings)"  
* **relatedProducts**: "Suggest related products based on current user selections. Parameters: productId (string)"  
* **highlightBestSellers**: "Show best-selling products in various categories. Parameters: category (string)"  
* **displayUserReviews**: "Show user reviews and ratings for products. Parameters: productId (string)"  
* **compareProducts**: "Allow users to compare similar products side-by-side. Parameters: productIds (array of strings)"

## AI-Agent Based Security and Surveillance Systems

* **monitorPremises**: "Continuously monitor premises using connected cameras and sensors. Parameters: cameraId (string), schedule (string)"  
* **alertIntrusion**: "Send real-time alerts in case of any detected intrusion or suspicious activity. Parameters: sensorId (string), alertType (string)"  
* **controlAccess**: "Manage and control access to secured areas. Parameters: accessPointId (string), command (string)"  
* **reportIncidents**: "Generate reports on security incidents and actions taken. Parameters: incidentId (string), reportDetails (object)"  
* **remoteControlSecurity**: "Allow remote control of security systems via AI agents. Parameters: systemId (string), command (string)"

## AI-Agent Driven Marketing and Advertising Platforms

* **manageAdCampaigns**: "Create, manage, and optimize ad campaigns. Parameters: campaignDetails (object), budget (float)"  
* **targetAudience**: "Identify and target specific audience segments for marketing. Parameters: audienceCriteria (object)"  
* **analyzeAdPerformance**: "Provide detailed analytics on ad campaign performance. Parameters: campaignId (string)"  
* **createMarketingContent**: "Assist in creating marketing content and advertisements. Parameters: contentDetails (object)"  
* **manageMarketingBudget**: "Track and manage marketing budgets and expenditures. Parameters: budgetDetails (object)"

## AI-Agent Enabled Restaurant Reservation Systems

* **searchRestaurants**: "Find restaurants based on user preferences and location. Parameters: location (string), cuisineType (string, optional)"  
* **bookTable**: "Facilitate table bookings at chosen restaurants. Parameters: restaurantId (string), date (string), time (string), partySize (integer)"  
* **recommendMenuItems**: "Suggest menu items based on user tastes and dietary preferences. Parameters: restaurantId (string), dietaryPreferences (string)"  
* **handleSpecialRequests**: "Manage special requests like dietary restrictions or seating preferences. Parameters: bookingId (string), specialRequest (string)"  
* **sendReservationReminders**: "Notify users of upcoming reservations. Parameters: bookingId (string)"

## AI-Agent Powered Personal Shopping Assistants

* **manageShoppingList**: "Create and manage shopping lists for users. Parameters: userId (string), listItems (array of strings)"  
* **searchForProducts**: "Find products based on user preferences and needs. Parameters: query (string), category (string, optional)"  
* **notifyPriceDrops**: "Notify users of price drops or special deals on desired items. Parameters: productId (string)"  
* **placeOrder**: "Place orders on behalf of users with preferred retailers. Parameters: retailerId (string), orderDetails (object)"  
* **trackDeliveries**: "Monitor and provide updates on the delivery status of orders. Parameters: orderId (string)"

## AI-Agent Driven Transportation and Ride-Hailing Services

* **bookRide**: "Schedule rides with ride-hailing services. Parameters: pickupLocation (string), destination (string), rideType (string)"  
* **optimizeRoute**: "Provide optimized routes for travel. Parameters: currentLocation (string), destination (string)"  
* **estimateFare**: "Estimate fares for different ride options. Parameters: pickupLocation (string), destination (string)"  
* **trackVehicle**: "Monitor the real-time location of booked vehicles. Parameters: bookingId (string)"  
* **manageSharedRides**: "Suggest and manage shared ride options to reduce costs. Parameters: pickupLocation (string), destination (string)"

## AI-Agent Enabled Environmental Monitoring and Management Systems

* **monitorAirQuality**: "Track and report air quality levels in real-time. Parameters: location (string), pollutantType (string, optional)"  
* **analyzeWaterQuality**: "Monitor and analyze water quality data. Parameters: location (string), sampleData (object)"  
* **optimizeWasteManagement**: "Optimize waste collection and disposal processes. Parameters: location (string), wasteType (string)"  
* **trackEnergyConsumption**: "Track and analyze energy usage patterns. Parameters: location (string), energyData (object)"  
* **sendEnvironmentalAlerts**: "Notify users of any detected environmental hazards or changes. Parameters: alertType (string), location (string)"

## AI-Agent Powered Community Management Platforms

* **coordinateEvents**: "Organize and promote community events. Parameters: eventDetails (object)"  
* **maintainMemberDirectory**: "Manage a directory of community members. Parameters: communityId (string)"  
* **facilitateDiscussions**: "Facilitate community discussions and forums. Parameters: topic (string), message (string)"  
* **manageResources**: "Manage and share community resources. Parameters: resourceId (string), details (object)"  
* **sendCommunityUpdates**: "Send updates and announcements to community members. Parameters: communityId (string), message (string)"

## AI-Agent Driven Financial Market Analysis Tools

* **analyzeMarketTrends**: "Analyze and report on market trends and patterns. Parameters: marketType (string), timePeriod (string)"  
* **recommendStocks**: "Provide personalized stock recommendations based on user preferences. Parameters: userId (string), riskTolerance (string)"  
* **managePortfolio**: "Assist in managing and optimizing investment portfolios. Parameters: userId (string), portfolioDetails (object)"  
* **evaluateInvestmentRisks**: "Evaluate and report on investment risks. Parameters: investmentId (string), riskFactors (array of strings)"  
* **sendMarketNewsAlerts**: "Notify users of market news and events that could impact investments. Parameters: marketType (string)"

## AI-Agent Enabled Language Translation and Localization Services

* **translateText**: "Translate text between different languages. Parameters: text (string), sourceLanguage (string), targetLanguage (string)"  
* **provideVoiceTranslation**: "Offer real-time voice translation for conversations. Parameters: sourceLanguage (string), targetLanguage (string)"  
* **localizeDocuments**: "Adapt documents for different regions and cultures. Parameters: documentId (string), targetLocale (string)"  
* **adaptContent**: "Modify content to suit cultural nuances and preferences. Parameters: contentId (string), targetLocale (string)"  
* **assistLanguageLearning**: "Help users learn new languages with personalized lessons. Parameters: userId (string), language (string)"

## AI-Agent Powered Virtual Travel and Tourism Guides

* **provideVirtualTours**: "Offer virtual tours of tourist attractions. Parameters: location (string), tourType (string)"  
* **createTravelItineraries**: "Generate personalized travel itineraries. Parameters: userId (string), destinations (array of strings)"  
* **recommendLocalAttractions**: "Suggest local attractions, restaurants, and activities. Parameters: location (string), interests (array of strings)"  
* **offerLanguageAssistance**: "Provide translation and language assistance for travelers. Parameters: sourceLanguage (string), targetLanguage (string)"  
* **sendTravelAlerts**: "Notify users of travel advisories and updates. Parameters: location (string), alertType (string)"

## AI-Agent Driven Smart City Infrastructure Management

* **manageTrafficFlow**: "Monitor and optimize traffic flow in real-time. Parameters: location (string), trafficData (object)"  
* **overseePublicServices**: "Manage public services such as waste collection and water supply. Parameters: serviceType (string), location (string)"  
* **optimizeEnergyUsage**: "Track and optimize energy usage across the city. Parameters: location (string), energyData (object)"  
* **monitorCitySecurity**: "Provide city-wide security monitoring and incident reporting. Parameters: location (string), securityData (object)"  
* **facilitateCitizenEngagement**: "Enable communication between city officials and citizens. Parameters: topic (string), message (string)"

## AI-Agent Enabled Human Resource Management Systems

* **assistRecruitment**: "Help in screening and recruiting candidates. Parameters: jobId (string), candidateDetails (object)"  
* **manageOnboarding**: "Oversee the onboarding process for new employees. Parameters: employeeId (string), onboardingDetails (object)"  
* **trackPerformance**: "Monitor and evaluate employee performance. Parameters: employeeId (string), metrics (array of strings)"  
* **recommendTrainingPrograms**: "Suggest training programs for employees. Parameters: employeeId (string), trainingNeeds (array of strings)"  
* **handleLeaveRequests**: "Manage employee leave requests and approvals. Parameters: employeeId (string), leaveType (string), startDate (string), endDate (string)"

## AI-Agent Powered Energy Management and Optimization Platforms

* **monitorEnergyConsumption**: "Track and analyze energy consumption patterns. Parameters: location (string), energyData (object)"  
* **recommendCostReduction**: "Provide recommendations for reducing energy costs. Parameters: location (string), usagePatterns (object)"  
* **integrateRenewableEnergy**: "Manage the integration of renewable energy sources. Parameters: energySource (string), capacity (float)"  
* **sendRealTimeAlerts**: "Notify users of any anomalies in energy usage. Parameters: location (string), alertType (string)"  
* **generateEfficiencyReports**: "Produce reports on energy efficiency and usage trends. Parameters: location (string), reportType (string)"

## AI-Agent Driven Personalized Learning Assistants

* **createLearningPathways**: "Generate personalized learning pathways based on user goals. Parameters: userId (string), learningGoals (array of strings)"  
* **monitorLearningProgress**: "Track and report on learning progress. Parameters: userId (string), courseId (string)"  
* **recommendLearningResources**: "Suggest learning resources and materials. Parameters: userId (string), interests (array of strings)"  
* **provideInteractiveQuizzes**: "Offer interactive quizzes and assessments. Parameters: userId (string), courseId (string)"  
* **sendStudyReminders**: "Notify users of study sessions and upcoming assessments. Parameters: userId (string), reminderType (string)"

## AI-Agent Enabled Telemedicine and Remote Healthcare Services

* **scheduleVirtualConsultations**: "Book and manage virtual consultations with healthcare providers. Parameters: providerId (string), date (string), time (string)"  
* **monitorSymptoms**: "Track and report symptoms to healthcare providers. Parameters: userId (string), symptoms (array of strings)"  
* **managePrescriptionsRemotely**: "Handle prescription refills and renewals. Parameters: userId (string), prescriptionId (string)"  
* **accessHealthRecords**: "Provide access to personal health records. Parameters: userId (string)"  
* **offerWellnessTips**: "Send personalized wellness and preventive care tips. Parameters: userId (string), wellnessGoals (array of strings)"

## AI-Agent Powered Automated Legal Document Generation

* **draftContracts**: "Automatically draft contracts based on user input. Parameters: userId (string), contractDetails (object)"  
* **reviewLegalDocuments**: "Analyze and suggest improvements to legal documents. Parameters: documentId (string)"  
* **ensureCompliance**: "Check documents for compliance with relevant regulations. Parameters: documentId (string), regulations (array of strings)"  
* **manageDocumentTemplates**: "Customize and manage legal document templates. Parameters: templateId (string)"  
* **facilitateESignatures**: "Enable electronic signatures for legal documents. Parameters: documentId (string)"

```

--------------------------------------------------------------------------------

### File: uim-compliance-with-eu-tdm-regulation.md
```
Path: uim-compliance-with-eu-tdm-regulation.md
Size: 9.38 KB
Last Modified: 2024-09-30 21:04:55
```

**Contents:**
```
# How the UIM Protocol Safeguards Right Holders Under the EU Text and Data Mining Regulation

## Introduction

The **Unified Intent Mediator (UIM)** protocol establishes a standardized framework for AI agents to interact with web services through well-defined intents, metadata, and execution methods. A crucial aspect of this interaction is ensuring that the rights of content owners (right holders) are protected, especially in the context of **Text and Data Mining (TDM)** activities.

The **EU Directive on Copyright in the Digital Single Market** (Directive (EU) 2019/790), specifically **Articles 3 and 4**, addresses TDM and sets out provisions to balance the interests of right holders with the needs of entities engaging in TDM. Understanding how the UIM protocol aligns with these regulations is essential for both service providers and AI agents operating within the EU.

## Overview of the EU TDM Regulation (Articles 3 and 4)

### Article 3: TDM for Scientific Research

- **Scope**: Provides an exception allowing research organizations and cultural heritage institutions to perform TDM on works to which they have lawful access, **without requiring additional permission from right holders**.
- **Purpose**: Facilitates scientific research by reducing barriers to accessing and analyzing large datasets.

### Article 4: TDM for Any Purpose

- **Scope**: Allows any individual or entity to perform TDM on works they have lawful access to.
- **Right Holder's Opt-Out**: Right holders can **reserve their rights** to prevent TDM activities by expressing this in an appropriate manner, such as through **machine-readable metadata** or **terms of service**.
- **Obligation**: Entities performing TDM must respect these reservations and obtain necessary permissions when rights are reserved.

## Safeguarding Right Holders with the UIM Protocol

The UIM protocol incorporates several features that align with the EU TDM regulation, enabling right holders to safeguard their interests effectively.

### 1. Policy Definition and Management through ODRL Integration

- **Use of ODRL**: The UIM protocol leverages the **Open Digital Rights Language (ODRL)** to define and manage permissions, prohibitions, and obligations associated with intents and the data they provide.
- **Expressing Rights Reservations**: Right holders can specify detailed policies that include **prohibitions on TDM activities**, constraints on data usage, and conditions under which data can be accessed or processed.

**Corrected ODRL Policy Snippet Reserving TDM Rights**:

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "@type": "Policy",
  "@id": "http://example.com/policy/tdm-restriction",
  "profile": "http://uimprotocol.com/uim/odrl-profile",
  "prohibition": [
    {
      "assignee": [
        {
          "uid": "http://www.w3.org/ns/odrl/2/Party#Public",
          "role": "assignee"
        }
      ],
      "target": "http://example.com/api/intents",
      "action": [
        {
          "id": "http://uimprotocol.com/uim/odrl/action#analyze"
        }
      ]
    }
  ],
  "permission": [
    {
      "target": "http://example.com/api/intents",
      "action": [
        {
          "id": "use"
        }
      ],
      "constraint": [
        {
          "leftOperand": "purpose",
          "operator": "neq",
          "rightOperand": "http://uimprotocol.com/uim/odrl/purpose#textDataMining"
        }
      ]
    }
  ],
  "agreement": "TDM activities are prohibited unless explicit permission is granted."
}
```

### 2. Policy Adherence Tokens (PATs)

- **Enforcing Compliance**: AI agents must obtain a **Policy Adherence Token (PAT)** before executing intents.
- **Agreement to Policies**: During the PAT issuance process, agents agree to the ODRL policies defined by the right holder.
- **Verification**: Web services verify PATs with each request, ensuring that only compliant agents can access and use the data.

### 3. Explicit Consent and Permissions

- **Granular Control**: Right holders can specify conditions under which TDM may be allowed, such as for certain users or purposes, by defining permissions in ODRL policies.
- **Dynamic Policies**: Policies can be updated to reflect changes in rights reservations, and agents must obtain new PATs accordingly.

### 4. Machine-Readable Metadata

- **Accessibility**: Policies are provided in machine-readable formats (JSON-LD with ODRL context), satisfying the requirement for right holders to express rights reservations appropriately.
- **Discoverability**: AI agents can easily discover these policies via the `uim-policy-file` link provided in the `agents.json` file or DNS TXT records.

### 5. Compliance with Legal Obligations

- **Alignment with Article 4**: By requiring agents to adhere to policies that may include TDM prohibitions, the UIM protocol ensures that right holders' reservations are respected.
- **Enforcement Mechanisms**: If an agent violates the policy (e.g., performs TDM without permission), the service can revoke access, and legal actions can be pursued based on the agreed terms.

---

## Handling TDM Exceptions for Scientific Research (Article 3)

- **Special Permissions**: Right holders can include exceptions in their policies to allow TDM for scientific research by recognized organizations.
- **Verification of Eligibility**: The PAT issuance process can involve verifying the agent's eligibility (e.g., confirming that it represents a research institution).
- **Custom Policies**: Separate policies can be defined for different categories of users, granting permissions where legally required.

**Corrected ODRL Policy Allowing TDM for Research**:

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "@type": "Policy",
  "@id": "http://example.com/policy/tdm-research",
  "profile": "http://uimprotocol.com/uim/odrl-profile",
  "permission": [
    {
      "assignee": [
        {
          "uid": "http://example.org/party#ResearchInstitution",
          "role": "assignee"
        }
      ],
      "target": "http://example.com/api/intents",
      "action": [
        {
          "id": "http://uimprotocol.com/uim/odrl/action#analyze"
        }
      ],
      "constraint": [
        {
          "leftOperand": "purpose",
          "operator": "eq",
          "rightOperand": "http://uimprotocol.com/uim/odrl/purpose#scientificResearch"
        }
      ]
    }
  ],
  "duty": [
    {
      "assignee": [
        {
          "uid": "http://example.org/party#ResearchInstitution",
          "role": "assignee"
        }
      ],
      "action": [
        {
          "id": "attribution"
        }
      ]
    }
  ],
  "agreement": "TDM is permitted for scientific research by recognized institutions."
}
```

**Explanation of Corrections**:

- **Assignee**: Defined as an object with `"uid"` and `"role"`.
- **Action**: Custom action `analyze` is properly namespaced.
- **Constraint**: Specifies the purpose as `scientificResearch` using a custom term.
- **Duty**: Correctly structured to include the `attribution` action.
- **Policy Structure**: Ensured compliance with ODRL syntax and semantics.

## Summary of Safeguards Provided by the UIM Protocol

1. **Rights Reservation Expression**: Right holders can **explicitly reserve their rights** regarding TDM in a machine-readable format.

2. **Mandatory Policy Agreement**: AI agents are **required to agree** to the right holder's policies before accessing services, ensuring awareness and compliance.

3. **Access Control via PATs**: The use of PATs allows services to **control access** and ensure that only authorized agents can perform actions, in line with the policies.

4. **Dynamic Policy Enforcement**: Right holders can **update policies** as needed, and agents must obtain new PATs, allowing adaptability to changing legal or business requirements.

5. **Transparency and Accountability**: The protocol facilitates **auditing and tracking** of agent activities, providing mechanisms to address non-compliance.

6. **Support for Legal Exceptions**: The UIM protocol can accommodate exceptions (e.g., for scientific research), aligning with **Article 3** provisions.

## Conclusion

The UIM protocol provides a robust framework that empowers right holders to safeguard their rights in accordance with the EU TDM regulation. By leveraging ODRL for policy expression and enforcing compliance through PATs, the protocol ensures that:

- **Right holders can reserve their rights** concerning TDM activities.
- **AI agents are obligated to comply** with these reservations.
- **Legal exceptions** (such as for scientific research) are appropriately handled.

This alignment with the EU TDM regulation not only protects right holders but also provides clarity and legal certainty for AI agents engaging in text and data mining activities, fostering a responsible and compliant ecosystem.

**References**:

- **EU Directive on Copyright in the Digital Single Market**: [Directive (EU) 2019/790](https://eur-lex.europa.eu/eli/dir/2019/790/oj)
- **ODRL Information Model 2.2**: [W3C Recommendation](https://www.w3.org/TR/odrl-model/)
- **Kluwer Copyright Blog on TDM Articles 3 and 4**: [The New Copyright Directive: Text and Data Mining (Articles 3 and 4)](https://copyrightblog.kluweriplaw.com/2019/07/24/the-new-copyright-directive-text-and-data-mining-articles-3-and-4/)

---

**Disclaimer**: The corrected policies are provided as examples and may need further adaptation to meet specific legal and organizational requirements. It is advisable to consult legal experts when implementing policies with legal implications.
```

--------------------------------------------------------------------------------

### File: uim-concept.md
```
Path: uim-concept.md
Size: 35.91 KB
Last Modified: 2024-09-16 20:06:22
```

**Contents:**
```
# Concepts behind the Unified Intent Mediator (UIM) Protocol

## Introduction

As AI technology advances, the need for efficient AI agent-web service interactions has become critical. Traditional methods like web scraping and simulated browser actions are inefficient, leading to:

- Inconsistent data extraction
- High latency
- Frequent errors
- Poor user experience
- Increased operational costs

The UIM protocol addresses these challenges by introducing a standardized, secure method for direct AI agent-web service interaction. Instead of simulating user actions, UIM allows services to expose capabilities as well-defined intents, which AI agents can discover and execute seamlessly.

### Current Inefficiencies in AI-Agent Interactions with Web Services

Despite AI advancements, current interaction methods remain rudimentary and problematic:

1. Web Scraping Challenges
   - Inconsistent data extraction due to unpredictable HTML changes
   - Legal and ethical issues, including terms of service violations

2. Simulated Browser Interactions
   - High performance overhead, degrading user experience
   - Vulnerability to dynamic content, pop-ups, and CAPTCHAs

3. Lack of Standardization
   - Diverse API designs requiring custom integrations
   - Inconsistent data formats necessitating multiple parsers

4. Limited Access to Deep Functionality
   - Restricted to basic data retrieval and simple transactions
   - Difficulty accessing advanced features due to API limitations

5. Security and Compliance Challenges
   - Complex authentication mechanisms
   - Data privacy concerns and regulatory compliance issues

![Challenges in AI-Agent interactions with web services](images/challenges.png)

### Motivation for the Unified Intent Mediator (UIM)

UIM addresses these challenges through:

1. Structured Interaction
   - Standardization across services
   - Direct service communication, eliminating scraping and simulations

2. Enhanced Security
   - Robust authentication mechanisms
   - Encrypted communications

3. Standardization and Interoperability
   - Unified interface for AI agents
   - Simplified integration process

4. Advanced Automation and Integration
   - Access to a broad range of functionalities
   - Seamless integration of complex workflows

5. Improved User Experience
   - Faster, more accurate interactions
   - Enhanced functionality and task precision

6. Sustainable Monetization Model
   - New revenue opportunities for service providers
   - Flexible monetization strategies

The UIM protocol redefines AI agent-web service interactions, paving the way for more efficient, reliable, and scalable AI-driven applications. As intelligent automation demand grows, UIM is positioned to become the cornerstone of next-generation AI-web service integrations.

![Unified Intent Mediator: A catalyst for AI-Agent evolution](images/catalyst.png)

## Key Concepts

The UIM protocol is built on three fundamental concepts: Intents, Metadata and Parameters, and the Execute Method. Each plays a crucial role in facilitating efficient communication between AI agents and web services.

![Key concepts](images/concept.png)

### Intents

Intents are the core building blocks of the UIM protocol. They represent specific, predefined actions that an AI agent can perform on a web service. By standardizing these actions, UIM creates a common language for interaction, significantly reducing complexity and enhancing efficiency.

In practical terms, an intent is analogous to a function call in programming. It encapsulates a discrete task, complete with the necessary information to execute it. For example, an e-commerce platform might offer intents such as:

- SearchProducts: Enables product searches based on various criteria
- GetProductDetails: Retrieves detailed information about a specific product
- PlaceOrder: Initiates and processes a purchase transaction

Other intent examples can be found [here](intent_examples.md) for inspiration.

This standardization allows AI agents to interact uniformly across different services, streamlining development and improving reliability.

### Metadata and Parameters

Metadata and parameters provide the context and specifics needed to execute intents effectively. They serve as the blueprint for each intent, detailing its purpose and requirements.

Metadata typically includes:

- Name: A unique identifier for the intent
- Description: A concise explanation of the intent's function
- Category: The type of action (e.g., e-commerce, finance, healthcare)

Parameters specify the input required for the intent's execution. For a 'SearchProducts' intent, parameters might include:

- query (string): The search term
- category (string): The product category filter
- price_range (string): The price range filter
- sort_by (string): The sorting criteria

This structured approach ensures that AI agents can provide the necessary information in the correct format, facilitating accurate and efficient intent execution.

### The Execute Method

The execute method is the operational core of the UIM protocol. It manages the actual execution of intents, ensuring smooth interaction between AI agents and web services. The method operates in four key stages:

1. Input Validation: Verifies that all required parameters are present and correctly formatted
2. Execution: Interacts with the web service's API to perform the requested action
3. Response Formatting: Standardizes the web service's response for consistent interpretation by AI agents
4. Error Handling: Manages exceptions and provides meaningful feedback for error resolution

![The execute method overview](images/execute-method.png)

This systematic approach enhances reliability and simplifies troubleshooting, contributing to a more robust interaction framework.

## Seamless Integration and Discoverability in the UIM Protocol

The UIM protocol prioritizes seamless integration and efficient discoverability, offering significant improvements over traditional AI-agent interactions with web services.

### Seamless Integration

![Integration benefits](images/uim-protocol.png)

The UIM protocol facilitates seamless integration through:

1. **Direct Interaction**
   - Eliminates navigation through web pages or user action simulation
   - Reduces latency and enhances task execution speed and reliability
   - Example: AI agents can book hotel rooms across multiple services using a single SearchForRoom intent

2. **Improved User Experience**
   - Provides faster and more accurate responses
   - Enables AI agents to perform complex tasks efficiently
   - Example: An AI agent can find, purchase, and confirm a book order within seconds

3. **Scalability**
   - Allows easy addition of new intents as web service capabilities expand
   - AI agents can leverage new functionalities with minimal modifications
   - Example: Streaming services can add intents like GetRecommendations or CreatePlaylist, which AI agents can automatically discover and utilize

4. **Consistency Across Services**
   - Ensures uniform behavior and responses across different web services
   - Simplifies AI agent development and enhances reliability
   - Example: A social media management AI can use a consistent PostContent intent across multiple platforms

### Discoverability

![How to improve discoverability](images/discoverability.png)

The UIM protocol enhances intent discoverability through:

1. **Intent Catalog**
   - Centralized repository for all registered intents and metadata
   - Standardized format for intent registration
   - RESTful API endpoints for intent registration, updating, and discovery

2. **Advanced Search Functionality**
   - Robust search capabilities based on keywords, categories, and other parameters
   - Features include:
     - Search indexing of all intent metadata
     - Rich query language for complex searches
     - Relevance-based ranking of search results

3. **Intent Tagging System**
   - Categorizes intents into meaningful groups
   - Allows multiple tags per intent (e.g., shopping, product search, retail for e-commerce intents)
   - Supports both service-defined and community-driven tagging
   - Enables tag-based search refinement

4. **Comprehensive Documentation**
   - Automatically generated for each intent
   - Includes:
     - Intent name and description
     - Detailed parameter information
     - API endpoint details
     - Usage examples with sample requests and responses

#### Example of an Intent Documentation

``` json
{
  "intent_uid": "ecommercePlatform:searchProducts:v1",
  "intent_name": "SearchProducts",
  "description": "Search for products based on given criteria",
  "parameters": [
    {
      "name": "query", 
      "type": "string", 
      "required": true, 
      "description": "The search term"
    },
    {
      "name": "category", 
      "type": "string", 
      "required": false, 
      "description": "Product category"
    },
    {
      "name": "price_range", 
      "type": "string", 
      "required": false, 
      "description": "Price range in the format 'min-max'"
    },
    {
      "name": "sort_by", 
      "type": "string", 
      "required": false, 
      "description": "Sort criteria (e.g., popularity, price)"
    }
  ],
  "endpoint": "https://api.ecommerce.com/api/products/search",
  "examples": {
    "request": {
      "method": "GET",
      "url": "https://api.ecommerce.com/api/products/search",
      "params": {
        "query": "laptops",
        "category": "electronics",
        "price_range": "1000-2000",
        "sort_by": "popularity"
      }
    },
    "response": {
      "status": "success",
      "data": [
        {
          "product_id": "123",
          "name": "Gaming Laptop",
          "price": 1500,
          "category": "electronics"
        }
      ]
    }
  },
  "tags": ["shopping", "product search", "retail"]
}
```

### Natural Language Support for Intent Discovery in UIM

The UIM protocol enhances intent discoverability by incorporating natural language processing (NLP) capabilities. This feature allows AI agents to interpret and utilize natural language queries, simplifying the process of identifying and executing appropriate actions to fulfill user requests.

#### Natural Language Understanding for AI Agents

Integration of NLP into the UIM protocol's intent catalog enables AI agents to process user instructions expressed in everyday language. This capability is crucial for creating more intuitive and efficient interactions. Key features include:

1. **Flexible Query Structure**: AI agents can pass original user requests directly to a UIM discovery API.
2. **Dynamic Query Translation**: The system translates natural language queries into structured search requests for the intent catalog.

![Intent discovery process](images/intent-discovery.png)

This approach offers two primary benefits:

1. **Improved Discoverability**
   - AI agents quickly and accurately find relevant intents by interpreting natural language queries.
   - Reduces time and effort required to identify appropriate actions.
   - Enhances overall efficiency of the discovery process.

2. **Enhanced Accuracy**
   - NLP engine understands context and language nuances.
   - Enables AI agents to select the most relevant intents and parameters.
   - Results in more precise and effective actions.

#### Implementation Components

To support natural language queries effectively, the UIM protocol incorporates:

1. **Robust Intent Catalog**: A comprehensive repository of all registered intents and their metadata.
2. **Advanced Search Functionality**: Supports complex queries and relevance-based ranking.
3. **Comprehensive Tagging System**: Categorizes intents for easier discovery.
4. **Detailed Documentation**: Provides clear examples and usage guidelines for each intent.

By implementing these features, the UIM protocol significantly enhances the discoverability and usability of intents. This approach ensures that AI agents can easily find, understand, and utilize appropriate intents, leading to more efficient and accurate interactions with web services.

The integration of natural language support in the UIM protocol represents a significant advancement in AI-web service interactions. It bridges the gap between human language and machine-readable instructions, paving the way for more intuitive and powerful AI-driven applications.

## Monetization Strategies for the UIM Protocol

The Unified Intent Mediator (UIM) protocol presents various opportunities for monetizing interactions between AI agents and web services. Here are five key strategies, each offering a unique approach to generating revenue while promoting adoption of the UIM protocol:

1. **Mediator Platform with Transaction Fees**
   - Concept: A centralized platform managing all interactions
   - Operation:
     - AI agents pay subscription or per-transaction fees
     - Web services register intents within the platform
     - Platform tracks usage and allocates payments
   - Example: Similar to App Store models (Apple, Google Play)
   ![Mediator Platform](images/mediator-platform.png)

2. **Usage-Based Billing with API Monetization**
   - Concept: Charging based on API call volume
   - Operation:
     - AI agents billed per API call
     - Pricing varies with intent complexity
     - Web services paid based on API usage
   - Example: Cloud services like AWS, Azure
   ![Usage-Based Billing](images/usage-based.png)

3. **Subscription Model with Tiered Pricing**
   - Concept: Tiered subscription plans for AI agents
   - Operation:
     - Plans offer varying usage limits and features
     - Web services compensated based on intent usage
   - Example: SaaS platforms like Salesforce, Netflix
   ![Subscription Model](images/subscription.png)

4. **Blockchain-Based Smart Contracts**
   - Concept: Automated payments via blockchain technology
   - Operation:
     - Interactions recorded on blockchain
     - Smart contracts execute payments automatically
   - Example: Ethereum's smart contract capabilities
   ![Blockchain-Based Smart Contracts](images/blockchain.png)

5. **Revenue Sharing Partnerships**
   - Concept: Strategic partnerships between web services and AI agent providers
   - Operation:
     - Partners offer exclusive or premium intents
     - Revenue shared between platform and web services
   - Example: Affiliate marketing programs like Amazon Associates
   ![Revenue Sharing Partnerships](images/revenue-sharing.png)

### Comparison Table of Monetization Strategies

| Monetization Strategy | Pros | Cons |
| :---- | :---- | :---- |
| **Mediator Platform with Transaction Fees** |  |  |
| \- Centralized control and management of interactions | \- Provides a unified platform for discovery, authentication, and execution | \- Dependency on the platform for all interactions |
| \- Simplifies the process for AI agents and web services | \- Enables consistent tracking and billing | \- Potential for high transaction fees, deterring some users |
| \- Potential for high revenue through transaction fees | \- Established model with proven success (e.g., App Store) | \- Centralization could lead to single points of failure |
| **Usage-Based Billing with API Monetization** |  |  |
| \- Revenue is proportional to actual usage | \- Flexible and scalable model | \- Unpredictable costs for AI agents |
| \- Encourages efficient use of resources | \- Clear cost structure based on resource consumption | \- Complex billing and tracking mechanisms required |
| \- Provides incentives for web services to optimize their APIs | \- Proven success in cloud services (e.g., AWS, Azure) | \- Potentially high costs for high-frequency users |
| **Subscription Model with Tiered Pricing** |  |  |
| \- Predictable revenue streams for agentic platforms and web services | \- Attracts different user segments through varied pricing tiers | \- Requires continuous addition of value to higher tiers |
| \- Simplifies budgeting for AI agents | \- Encourages loyalty and long-term usage | \- Balancing pricing and feature availability can be challenging |
| \- Can offer exclusive features in higher tiers | \- Proven success in SaaS platforms (e.g., Salesforce, Netflix) | \- Potentially less flexible for users with variable usage patterns |
| **Blockchain-Based Smart Contracts** |  |  |
| \- Decentralized and transparent transactions | \- Reduces the need for intermediaries | \- High initial setup and implementation costs |
| \- Automated and secure payment processing | \- Ensures trust through immutable records | \- Complexity in integrating blockchain with existing systems |
| \- Enables micro-transactions efficiently | \- Potential for innovative and fair revenue distribution | \- Volatility of cryptocurrency values |
| **Revenue Sharing Partnerships** |  |  |
| \- Aligns incentives between the agentic platforms and web services | \- Encourages collaboration and innovation | \- Dependence on the success of partner services |
| \- Can provide exclusive or premium content to AI agents | \- Proven success in affiliate marketing (e.g., Amazon Associates) | \- Requires negotiation and management of partnerships |
| \- Potential for high revenue through commissions | \- Can attract high-quality web services through revenue sharing | \- Potential complexity in tracking and distributing shared revenue |

Each strategy offers unique benefits and challenges. The choice depends on factors such as target market, technological capabilities, and business model preferences. By aligning the UIM protocol with these flexible, sustainable revenue models, service providers can ensure viability while promoting wider adoption of standardized AI-driven interactions.

## Summary of UIM Protocol Benefits

The Unified Intent Mediator (UIM) protocol offers numerous advantages that collectively transform AI-web service interactions:

![Benefits overview](images/uim-benefits.png)

1. **Streamlined Interaction**
   - Eliminates need for simulated user actions
   - Enables direct, efficient task execution via registered intents
   - Reduces complexity and overhead of traditional methods

2. **Enhanced Functionality and Integration**
   - Exposes wide range of web service functionalities as intents
   - Facilitates creation of complex, integrated automated solutions
   - Expands AI agents' capabilities from simple data retrieval to intricate transactions

3. **New Revenue Streams**
   - Allows service providers to monetize intent access/usage
   - Offers flexible pricing models (tiered, subscription, pay-per-use)
   - Incentivizes broader participation in the UIM ecosystem

4. **Improved Efficiency and User Experience**
   - Streamlines interaction process, reducing task completion time
   - Enables quicker, more reliable AI agent responses
   - Enhances user satisfaction and trust in AI-driven services

5. **Robust Security and Compliance**
   - Incorporates encrypted communications and secure authentication (e.g., OAuth2.0)
   - Designed to comply with data protection regulations (GDPR, CCPA)
   - Builds trust through enhanced data privacy and security measures

6. **Scalability and Flexibility**
   - Modular design allows easy addition of new intents and functionalities
   - Enables AI agents to adapt to changes with minimal modifications
   - Supports growth in line with evolving AI-driven application demands

7. **Innovative and Future-Proof Solution**
   - Built to integrate emerging technologies (e.g., blockchain, machine learning)
   - Ensures relevance and adaptability to future technological advancements
   - Positions UIM as a cornerstone for future AI-web service interactions

## Final Thoughts

The UIM protocol represents a paradigm shift in AI-web service communication, addressing current inefficiencies and offering a robust, scalable, and secure solution. As AI continues to evolve and permeate various aspects of business and daily life, UIM will play a crucial role in ensuring efficient, secure, and capable interactions.

The success of UIM depends on collaborative efforts from developers, service providers, and industry leaders. By working together, they can leverage this strategic enabler to unlock new possibilities in AI-driven automation and web service integration, building a more connected and intelligent future.

In essence, the UIM protocol is not merely a technical solution, but a catalyst for innovation in the AI and web service ecosystem, promising to revolutionize digital interactions and pave the way for more sophisticated, efficient, and user-friendly AI applications.

## **System Architecture of the UIM Protocol: A Detailed Evaluation**

The UIM protocol is designed to facilitate seamless communication and interaction between AI agents and web services. In this section, we will delve into the system architecture of the UIM protocol, comparing and contrasting two proposed approaches: the Man-in-the-Middle Approach with a Centralized Repository and the Decentralized Approach with AI Agents Crawling Web Services. By evaluating the architectural differences, benefits, and potential challenges of each approach, we can gain insights into the strengths and weaknesses of each design, ultimately informing the selection of the most suitable architecture for implementors of the UIM protocol.

![Main architecture](images/main-architecture.png)

### **1. Man-in-the-Middle Approach: Centralized Repository**

**Overview:**
In the centralized approach, a central system acts as an intermediary (man-in-the-middle) between AI agents and web services. This central repository collects, manages, and provides access to intent information registered by web services. AI agents interact with this repository to discover available intents and execute actions on web services via standardized endpoints.

**Key Architectural Components:**

- **Central Repository**: The core of this architecture, where web services register their intents. This repository contains metadata, parameters, and execution details for each intent.
- **Service Management Endpoints**: Web services use these endpoints to register, update, and manage their intents in the repository.
- **Discovery Endpoints**: AI agents use these endpoints to search for available intents, fetch detailed information, and identify which actions they can execute.
- **Execution Endpoint**: Facilitates the actual execution of an action by forwarding requests from AI agents to the appropriate web service based on registered intents.
- **Policy Adherence and Security Layer**: Manages authentication, authorization, and rate limiting, often using the Policy Adherence Token (PAT) system. It ensures compliance and secure interaction between AI agents and web services.

![Centralized repository](images/centralized-repo.png)

**Architecture Flow:**

1. **Web Service Registration**: Web services register their intents with the central repository using service management endpoints. Alternatively, the system can automatically discover and register intents using a crawling mechanism.
2. **Intent Discovery**: AI agents query the discovery endpoints to identify relevant intents based on user requests.
3. **Intent Details Retrieval**: Once an intent is identified, the agent fetches detailed execution parameters from the repository.
4. **Execution**: The AI agent submits a request to the execution endpoint, which forwards it to the appropriate web service.
5. **Response Handling**: The results are returned to the AI agent, which then processes and presents the output to the user.

**Benefits:**

- **Centralized Management**: A single point of management for all intents simplifies oversight, updates, and maintenance.
- **Consistent Data Structure**: Standardized intent formats and metadata facilitate easier integration and use by AI agents.
- **Enhanced Security**: Centralized control over access, authentication, and rate limiting helps enforce security and compliance measures.
- **Reliable Monetization**: A clear, controlled pathway for monetization, allowing the central system to manage payments and enforce billing policies.

**Challenges:**

- **Scalability**: As the number of registered web services and AI agents grows, the central system must handle significant data volumes and high transaction loads.
- **Single Point of Failure**: Any issues with the central repository can disrupt the entire system, impacting both AI agents and web services.
- **Data Privacy Concerns**: Central storage of intent information may raise concerns about data ownership and privacy for web services.

#### **2. Decentralized Approach: AI Agents Crawling Web Services**

**Overview:**
In the decentralized approach, AI agents themselves are responsible for discovering and collecting intent information directly from web services. This is achieved through crawling mechanisms that utilize DNS TXT records and/or `agents.json` files hosted by web services. The intent information is stored locally by AI agents, allowing them to directly interact with web services without a centralized intermediary.

**Key Architectural Components:**

- **DNS TXT Records and `agents.json` Files**: These files are hosted by web services to provide intent metadata, execution details, policies, rate limits, and authentication methods. They act as a self-descriptive interface for AI agents.
- **Crawling Mechanism**: AI agents periodically or on-demand crawl these resources to collect and update intent information from various web services.
- **Local Intent Repository**: Each AI agent maintains its own repository of intent information, allowing it to execute actions based on the data collected from web services.
- **Execution Endpoint**: AI agents directly call execution endpoints on web services to perform actions, authenticated using data collected during crawling (e.g., PATs, OAuth tokens).
- **Policy Compliance and Security Layer**: Similar to the centralized model, but managed locally by each AI agent using the information gathered from `agents.json` and DNS records.

![AI-Agent architecture](images/ai-agent-architecture.png)

**Architecture Flow:**

1. **Crawling and Discovery**: AI agents crawl web services to gather available intents using DNS TXT records and `agents.json` files.
2. **Intent Data Storage**: The gathered data is stored locally within the AI agent’s repository, creating a personalized database of actions.
3. **Execution**: When a user request matches a stored intent, the AI agent directly interacts with the corresponding web service to execute the action.
4. **Compliance and Security**: The AI agent adheres to rate limits, billing requirements, and authentication methods as outlined in the collected intent data.
5. **Response Handling**: Results from the execution are processed and returned to the user.

**Benefits:**

- **Scalability**: Decentralization avoids the bottlenecks of a central system, allowing scalability across millions of AI agents and web services.
- **No Single Point of Failure**: Since intent information is distributed, the system remains robust even if some agents or services encounter issues.
- **Privacy and Ownership**: Web services maintain control over their intent data, reducing concerns about data privacy and centralization.
- **Flexible and Adaptable**: AI agents can quickly adapt to new services or changes in existing ones without waiting for updates in a central repository.

**Challenges:**

- **Inconsistent Data**: Without centralized control, there may be variations in how web services present their intent data, leading to potential inconsistencies. Adherence to the UIM protocol can help mitigate this issue.
- **Higher Complexity for AI Agents**: Each agent must handle crawling, data parsing, security, and compliance on its own, increasing the complexity of individual agents.
- **Maintenance Overhead**: AI agents need to frequently crawl and update intent information to stay current, which can be resource-intensive.

### **Comparative Evaluation of Both Approaches**

1. **Centralized Repository (Man-in-the-Middle)**
   - **Pros**: Streamlined management, consistent data structure, enhanced security, clear monetization strategy.
   - **Cons**: Scalability issues, single point of failure, potential data privacy concerns.

2. **Decentralized Crawling by AI Agents**
   - **Pros**: Scalability, robust against failures, privacy-friendly, adaptable to changes.
   - **Cons**: Potential inconsistencies, complex management for AI agents, resource-intensive maintenance.

### **Strategic Recommendations:**

- **Use Centralized Approach**: If the primary goal is to maintain strict oversight, enforce security protocols, and ensure a standardized user experience across all AI agents and web services.
- **Adopt Decentralized Approach**: If scalability, resilience, and data privacy are paramount, particularly in environments where rapid adaptation and autonomy are critical.

![Architecture comparison](images/solution-comparison.png)

By understanding these architectural nuances, stakeholders can better align the UIM protocol’s deployment strategy with their operational needs, ensuring efficient and effective integration between AI agents and web services.

## UIM Protocol Specification

Check out the proposed specification here: [Unified Intent Mediator Specification](unified-intent-mediator-api-specification.md). It goes into details about the suggested endpoints, data structures, security measures, billing, policy compliance, and more.

## Future Work and Expansion

The Unified Intent Mediator protocol represents a significant step forward in facilitating efficient and seamless interactions between AI agents and web services. However, there is substantial potential for further development and expansion. Future work could focus on several key areas to enhance the protocol's capabilities and drive wider adoption.

### Support for More Complex Interactions

As AI technology continues to advance, there will be a growing demand for the API to support more complex interactions. This could involve enabling multi-step processes, where AI agents can chain multiple intents together to complete sophisticated tasks (multi-tool and multi-step scenarios):

- **Multi-Step Intents:** Future iterations of the UIM protocol could include support for multi-step intents, where AI agents execute a sequence of actions as part of a single, cohesive operation. This would enable more complex workflows, such as initiating a transaction, verifying details, and completing the payment, all within one unified process.  
- **Context-Aware Interactions:** Enhancing the UIM protocol to support context-aware interactions would allow AI agents to adjust their behavior based on the current state or environment. For example, an AI agent could modify its requests based on user preferences, historical data, or real-time conditions.

![Future developments](images/future-development.png)

**Examples of Complex Interactions:**

- **E-commerce**: An AI agent could handle the entire purchase process, from searching for a product, comparing prices across multiple platforms, selecting the best deal, and completing the checkout process, all in one seamless interaction.  
- **Healthcare**: An AI agent could book an appointment, retrieve medical records, and even arrange for prescription deliveries by interacting with multiple intents across different healthcare services or providers.
- **Finance**: An AI agent could manage a user’s entire investment portfolio, from analyzing market trends, selecting suitable stocks, and executing trades, all within a single interaction.  
- **Travel Planning**: An AI agent could plan an entire trip by booking flights, hotels, and rental cars, while also arranging for local tours and activities through a series of coordinated intents.

### Integration of Advanced AI Capabilities

To further enhance the functionality of the Unified Intent Mediator protocol, integrating advanced AI capabilities such as natural language processing (NLP), machine learning (ML), and predictive analytics would be highly beneficial.

**Advanced AI Capabilities:**

- **Natural Language Processing (NLP)**: Integrating NLP can allow AI agents to understand and process user intents expressed in natural language, making interactions more intuitive and user-friendly.  
- **Machine Learning (ML)**: ML algorithms can be used to predict user preferences and optimize interactions. For instance, an AI agent could learn a user’s shopping habits and proactively suggest products or services.  
- **Predictive Analytics**: By analyzing historical data, AI agents can anticipate user needs and offer proactive solutions. For example, an AI agent could predict when a user might need to reorder a product based on past purchasing patterns.

![AI Capabilities](images/ai-capabilities.png)

### Exploring Partnerships with Major Web Services and AI Platforms

Partnerships with major web services and AI platforms can significantly accelerate the adoption and innovation of the Unified Intent Mediator protocol. Collaborating with industry leaders can provide access to a broader range of services and enhance the protocol's capabilities and reach.

**Potential Partnerships:**

- **Industry Collaborations:** Forming strategic partnerships with key industry players can accelerate the adoption and expansion of the UIM protocol. These collaborations could involve co-developing standards, integrating UIM with existing platforms, or launching joint initiatives to promote the protocol’s benefits.  
- **Open Source Community Engagement:** Engaging with the open-source community can drive innovation and improvement within the UIM protocol. By encouraging contributions from developers worldwide, the protocol can evolve more rapidly and address a broader range of use cases.

![Potential partnerships](images/adoption.png)

### Development of a Developer Ecosystem

Creating a vibrant developer ecosystem around the Unified Intent Mediator protocol can foster innovation and drive the creation of new intents and services. By providing comprehensive documentation, SDKs, and developer tools, the protocol can attract a community of developers eager to build on the concept.

**Developer Ecosystem Initiatives:**

- **Comprehensive Documentation**: Offering detailed guides, tutorials, and API references to help developers understand and utilize the protocol effectively.  
- **Software Development Kits (SDKs)**: Providing SDKs for popular programming languages to streamline the development process and make it easier for developers to integrate their services.  
- **Developer Tools**: Creating tools for testing, debugging, and monitoring interactions can help developers build and maintain high-quality services.

![Developer ecosystem](images/developer-ecosystem.png)

### Expansion into New Domains

While the initial focus may be on well-established industries like e-commerce, healthcare, and finance, there is significant potential for expanding the Unified Intent Mediator protocol into new domains. Emerging sectors such as smart cities, IoT, and autonomous vehicles can greatly benefit from the protocol capabilities, but might have additional requriements and challenges. By exploring these new domains, the UIM protocol can continue to drive innovation and create new opportunities for seamless, efficient, and intelligent service integration.

**New Domains for Expansion:**

- **Smart Cities**: Integrating with smart city infrastructure to provide AI-driven services like intelligent traffic management, waste collection, and public safety monitoring.  
- **Internet of Things (IoT)**: Enabling AI agents to interact with IoT devices for home automation, industrial monitoring, and environmental sensing.  
- **Autonomous Vehicles**: Facilitating interactions between AI agents and autonomous vehicle systems for tasks like route planning, maintenance scheduling, and real-time traffic updates.

### Summary

The future work and expansion of the Unified Intent Mediator API hold immense potential to revolutionize AI-agent interactions with web services. By supporting more complex interactions, integrating advanced AI capabilities, exploring strategic partnerships, fostering a developer ecosystem, and expanding into new domains, the protocol can continue to drive innovation and create new opportunities for seamless, efficient, and intelligent service integration. The success of these future efforts will depend on collaboration, innovation, and a commitment to maintaining the protocol’s foundational principles of standardization, security, and scalability.

![Future development timeline](images/future-timeline.png)
```

--------------------------------------------------------------------------------

### File: uim-licensing-scheme.md
```
Path: uim-licensing-scheme.md
Size: 49.90 KB
Last Modified: 2024-09-30 21:04:55
```

**Contents:**
```
# Licensing Scheme Specification for the Unified Intent Mediator (UIM) Protocol

## Introduction

The **Unified Intent Mediator (UIM) Protocol** standardizes interactions between AI agents and web services. A critical component of this protocol is the **UIM Licensing Scheme**, which defines permissions, conditions, and prohibitions for using content and services. This scheme is inspired by:

- **Creative Commons (CC) Licenses**: For their simplicity and modularity.
- **Responsible AI Licenses (RAIL)**: For incorporating AI-specific considerations and use restrictions.

*Credits: This licensing scheme is inspired by the Creative Commons licenses and the Responsible AI Licenses (RAIL), aiming to foster open, ethical, and collaborative AI ecosystems.*

---

## Key Features

### 1. **Modular License Elements**

- **Flexibility**: Combines basic permissions, conditions, and prohibitions to create a wide variety of license combinations.
- **Customization**: Allows licensors to tailor licenses to specific use cases and requirements.

### 2. **Artifact Type Specification**

- **DAMS Expansion to DAMPS**: Distinguishes between different artifact types, including data, applications, models, parameters, and source code.
- **Clarity**: Clearly indicates which artifacts the license applies to, preventing misuse.

### 3. **Comprehensive License Elements**

- **Standard and New Elements**: Includes standard license elements and newly introduced ones to cover specific scenarios.
- **Detailed Definitions**: Each element is clearly defined to ensure consistent understanding and application.

### 4. **License Naming Convention**

- **Structured Codes**: Uses a standardized naming convention that includes artifact types, license elements, and version numbers.
- **Ease of Identification**: Facilitates quick recognition of the license's key aspects.

### 5. **Three Formats**

- **Human-Readable**: Summarizes the license in plain language.
- **Lawyer-Readable**: Provides detailed legal terms and conditions.
- **Machine-Readable**: Uses standardized formats (e.g., JSON-LD) aligned with schema.org for interoperability.

### 6. **Integration with Existing Standards**

- **Compatibility**: Ensures alignment with schema.org vocabularies and other licensing frameworks.
- **Interoperability**: Enhances the ability of AI agents and services to understand and comply with licenses.

### 7. **Ethical AI Considerations**

- **Ethical AI Use (EAU)**: Includes provisions to promote responsible AI development and prevent harmful applications.
- **Use Restrictions**: Allows licensors to specify prohibited uses, such as harmful activities or violations of human rights.

## License Elements

The UIM Licensing Scheme comprises **Permissions**, **Conditions**, and **Prohibitions**. These elements can be combined to create licenses that meet specific needs.

### Permissions

- **Access**: Permission to access the content or service.
- **Reproduce**: Copy or replicate content.
- **Distribute**: Share content with others.
- **Modify**: Adapt, remix, transform, or build upon content.
- **Commercial Use**: Use content for commercial purposes.
- **NonCommercial Use**: Use content for non-commercial purposes.
- **Data Mining**: Use content for text and data mining.
- **Model Training**: Use content to train AI models.
- **Indexing**: Access and reproduce content solely for indexing and providing search results.

### Conditions

- **Attribution (BY)**: Must give appropriate credit.
- **ShareAlike (SA)**: Derivative works must be licensed under identical terms.
- **NonCommercial (NC)**: Commercial use is prohibited.
- **NoDerivatives (ND)**: No modifications or adaptations allowed.
- **Ethical AI Use (EAU)**: Must comply with ethical guidelines, prohibiting harmful applications.
- **Indexing Only (IO)**: Access and reproduction are permitted solely for indexing and search purposes.
- **AI Output Attribution (AIATTR)**: AI systems must attribute outputs derived from the content back to the source.

### Prohibitions

- **Harmful Use**: Prohibits use in applications causing harm (e.g., surveillance, discrimination).
- **Reidentification**: Prohibits attempts to re-identify anonymized data.
- **Redistribution**: Prohibits unauthorized redistribution.
- **No Data Mining (NoDM)**: Prohibits the use of content for data mining.
- **No Model Training (NoMT)**: Prohibits the use of content for training AI models.
- **No Long-Term Storage (NoLTS)**: Prohibits storing content for long-term use.
- **Bypass Access Controls Prohibited (BACP)**: Prohibits bypassing paywalls or access restrictions.

## Artifact Types (DAMPS Convention)

To specify the artifacts impacted by the license, the UIM scheme uses the expanded **DAMPS** convention:

- **D**: **Data**
- **A**: **Applications/Binaries/Services**
- **M**: **Model Architectures**
- **P**: **Parameters (Trained Weights)**
- **S**: **Source Code**

### Purpose of DAMS ➡️ DAMPS Expansion

- **Granular Control**: Differentiates between model architectures and parameters, allowing for tailored licensing.
- **Common Practice Alignment**: Reflects industry practices where model code and trained parameters are licensed differently.

## License Naming Convention

**License Code Structure**:

```txt
[Open-][Artifact Type(s)-]UIM-[License Elements]-v[Version Number]
```

### Components

1. **Open-**: Indicates that the license offers artifacts at no charge and allows re-licensing under the same terms.
2. **Artifact Type(s)**: Specified using the DAMPS letters (D, A, M, P, S).
3. **UIM**: Denotes that it is part of the UIM Licensing Scheme.
4. **License Elements**: Combination of license conditions and prohibitions (e.g., BY, NC, ND, SA, IO, AIATTR).
5. **v[Version Number]**: Indicates the version of the license.

### Examples of License Codes

1. **Search Engine Use**:

   - **License Code**: **A-UIM-BY-ND-IO-NoDM-NoMT-v1.0**
   - **Artifact Type**: Application (A)
   - **Conditions**: Attribution (BY), NoDerivatives (ND), Indexing Only (IO)
   - **Prohibitions**: No Data Mining (NoDM), No Model Training (NoMT)

2. **Attribution-Based AI**:

   - **License Code**: **D-UIM-BY-AIATTR-v1.0**
   - **Artifact Type**: Data (D)
   - **Conditions**: Attribution (BY), AI Output Attribution (AIATTR)

3. **Dynamic Content Restrictions**:

   - **License Code**: **D-UIM-BY-ND-NoMT-NoLTS-v1.0**
   - **Artifact Type**: Data (D)
   - **Conditions**: Attribution (BY), NoDerivatives (ND)
   - **Prohibitions**: No Model Training (NoMT), No Long-Term Storage (NoLTS)

4. **Parameters with Restrictions**:

   - **License Code**: **P-UIM-BY-NC-ND-v1.0**
   - **Artifact Type**: Parameters (P)
   - **Conditions**: Attribution (BY), NonCommercial (NC), NoDerivatives (ND)

## Integration with Existing Standards

- **Schema.org Alignment**: Machine-readable licenses use schema.org vocabularies to enhance interoperability.
- **JSON-LD Format**: Standardized format ensures consistency and compatibility with AI agents and services.
- **Version Control**: Including version numbers in license codes helps manage updates and maintain clarity.

## Three Formats of Licenses

### 1. **Human-Readable Summary**

- **Purpose**: Provides an easy-to-understand overview of the license terms.
- **Content**: Outlines permissions, conditions, and prohibitions in plain language.

### 2. **Lawyer-Readable Legal Code**

- **Purpose**: Offers a detailed legal document specifying the license terms.
- **Content**: Includes comprehensive definitions, rights granted, conditions imposed, prohibitions, and disclaimers.

### 3. **Machine-Readable Code**

- **Purpose**: Enables AI agents and services to automatically interpret and comply with the license terms.
- **Format**: Uses JSON-LD aligned with schema.org vocabularies.
- **Content**: Contains structured data representing the license elements.

#### JSON-LD Schema Definition

To ensure metadata consistency, the following schema is used for machine-readable licenses:

```json
{
  "@context": ["https://schema.org/", "https://uimprotocol.com/licenses/context"],
  "@type": "License",
  "name": "License Name",
  "url": "License URL",
  "version": "Version Number",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [/* Array of permissions */],
  "conditions": [/* Array of conditions */],
  "prohibitions": [/* Array of prohibitions */]
}
```

---

## UIM License Combinations

Below is a comprehensive list of non-contradictory license combinations within the UIM Licensing Scheme. Each license includes:

- **License Name and Code**
- **Applicable Artifact Type(s)**
- **Permissions**
- **Conditions**
- **Prohibitions**
- **Human-Readable Summary**
- **Lawyer-Readable Legal Code**
- **Machine-Readable Code (JSON-LD)**

## Table of Contents

1. [UIM Public Domain Dedication (UIM-PD-v1.0)](#1-uim-public-domain-dedication-uim-pd-v10)
2. [UIM CC0 Dedication (UIM-CC0-v1.0)](#2-uim-cc0-dedication-uim-cc0-v10)
3. [UIM Attribution License (UIM-BY-v1.0)](#3-uim-attribution-license-uim-by-v10)
4. [UIM Attribution-ShareAlike License (UIM-BY-SA-v1.0)](#4-uim-attribution-sharealike-license-uim-by-sa-v10)
5. [UIM Attribution-NoDerivatives License (UIM-BY-ND-v1.0)](#5-uim-attribution-noderivatives-license-uim-by-nd-v10)
6. [UIM Attribution-NonCommercial License (UIM-BY-NC-v1.0)](#6-uim-attribution-noncommercial-license-uim-by-nc-v10)
7. [UIM Attribution-NonCommercial-ShareAlike License (UIM-BY-NC-SA-v1.0)](#7-uim-attribution-noncommercial-sharealike-license-uim-by-nc-sa-v10)
8. [UIM Attribution-NonCommercial-NoDerivatives License (UIM-BY-NC-ND-v1.0)](#8-uim-attribution-noncommercial-noderivatives-license-uim-by-nc-nd-v10)
9. [UIM Attribution with AI Output Attribution License (UIM-BY-AIATTR-v1.0)](#9-uim-attribution-with-ai-output-attribution-license-uim-by-aiattr-v10)
10. [UIM Attribution-NoDerivatives Indexing License (UIM-BY-ND-IO-NoDM-NoMT-v1.0)](#10-uim-attribution-noderivatives-indexing-license-uim-by-nd-io-nodm-nomt-v10)
11. [UIM Attribution-NoDerivatives Dynamic Content License (UIM-BY-ND-NoMT-NoLTS-v1.0)](#11-uim-attribution-noderivatives-dynamic-content-license-uim-by-nd-nomt-nolts-v10)
12. [Open Data UIM Attribution License (Open-D-UIM-BY-v1.0)](12-open-data-uim-attribution-license-open-d-uim-by-v10)

## 1. UIM Public Domain Dedication (UIM-PD-v1.0)

### License Name and Code

- **License Name**: UIM Public Domain Dedication Version 1.0
- **License Code**: **UIM-PD-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: Data (D), Applications (A), Parameters (P), Models (M), Source Code (S)

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Modify**
- **Commercial Use**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **None**

### Prohibitions

- **None**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, modify, and use** the work for **any purpose**, without any restrictions.

**No conditions or prohibitions apply.**

### Lawyer-Readable Legal Code

**License Name**: UIM Public Domain Dedication Version 1.0 (UIM-PD-v1.0)

**Dedication:**

The Licensor, to the extent possible under law, hereby dedicates the Work to the public domain. The Work is provided "as-is" without warranties of any kind.

**Permissions:**

You may use the Work freely for any purpose, without any conditions or restrictions.

**Disclaimers:**

The Licensor makes no warranties about the Work and disclaims liability for all uses of the Work.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "CreativeWork",
  "name": "UIM-PD-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-pd-v1.0",
  "version": "1.0",
  "license": "https://creativecommons.org/publicdomain/zero/1.0/",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [],
  "prohibitions": []
}
```

## 2. UIM CC0 Dedication (UIM-CC0-v1.0)

### License Name and Code

- **License Name**: UIM CC0 Dedication Version 1.0
- **License Code**: **UIM-CC0-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: Data (D), Applications (A), Parameters (P), Models (M), Source Code (S)

### Permissions

- **Same as UIM-PD-v1.0**

### Conditions

- **None**

### Prohibitions

- **None**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, modify, and use** the work for **any purpose**, without any restrictions.

**No conditions or prohibitions apply.**

### Lawyer-Readable Legal Code

**License Name**: UIM CC0 Dedication Version 1.0 (UIM-CC0-v1.0)

**Dedication:**

The Licensor, to the extent possible under law, has dedicated the Work to the public domain under CC0. The Work is provided "as-is" without warranties of any kind.

**Permissions:**

You may use the Work freely for any purpose, without any conditions or restrictions.

**Disclaimers:**

The Licensor makes no warranties about the Work and disclaims liability for all uses of the Work.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "@type": "CreativeWork",
  "name": "UIM-CC0-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-cc0-v1.0",
  "version": "1.0",
  "license": "https://creativecommons.org/publicdomain/zero/1.0/",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [],
  "prohibitions": []
}
```

## 3. UIM Attribution License (UIM-BY-v1.0)

### License Name and Code

- **License Name**: UIM Attribution License Version 1.0
- **License Code**: **UIM-BY-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: D, A, P, M, S

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Modify**
- **Commercial Use**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, modify, and use** the work for **any purpose**, including **commercial** and **non-commercial** uses.

**Under the following conditions:**

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **Ethical AI Use**: You must not use the work for harmful purposes.

**Prohibitions:**

- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution License Version 1.0 (UIM-BY-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Modify, Use**: You are granted the rights to access, reproduce, distribute, modify, and use the Work for any purpose, including commercial uses.

**2. Conditions**

- **Attribution (BY)**: You must give appropriate credit to the Licensor, provide a link to the license, and indicate if changes were made.
- **Ethical AI Use (EAU)**: You must not use the Work for harmful purposes, including but not limited to violating human rights or privacy.

**3. Prohibitions**

- **Harmful Use**: You may not use the Work in any way that causes harm.

**4. Disclaimer**

- The Work is provided "as-is" without warranties of any kind.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-v1.0",
  "version": "1.0",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "HarmfulUse"
  ]
}
```

## 4. UIM Attribution-ShareAlike License (UIM-BY-SA-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-ShareAlike License Version 1.0
- **License Code**: **UIM-BY-SA-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: D, A, P, M, S

### Permissions

- **Same as UIM-BY-v1.0**

### Conditions

- **Attribution (BY)**
- **ShareAlike (SA)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, modify, and use** the work for **any purpose**, including **commercial** and **non-commercial** uses.

**Under the following conditions:**

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **ShareAlike**: If you remix, transform, or build upon the work, you must distribute your contributions under the same license.
- **Ethical AI Use**: You must not use the work for harmful purposes.

**Prohibitions:**

- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-ShareAlike License Version 1.0 (UIM-BY-SA-v1.0)

**1. Grant of Rights**

- **Same as UIM-BY-v1.0**

**2. Conditions**

- **Attribution (BY)**: As above.
- **ShareAlike (SA)**: Any derivative works must be licensed under identical terms.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-SA-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-sa-v1.0",
  "version": "1.0",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "ShareAlike",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "HarmfulUse"
  ]
}
```

## 5. UIM Attribution-NoDerivatives License (UIM-BY-ND-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-NoDerivatives License Version 1.0
- **License Code**: **UIM-BY-ND-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: D, A, P, M, S

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Commercial Use**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **NoDerivatives (ND)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Modify**
- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, and distribute** the work for **any purpose**, including **commercial** and **non-commercial** uses.

**Under the following conditions:**

- **Attribution**: You must give appropriate credit, provide a link to the license.
- **NoDerivatives**: If you remix, transform, or build upon the work, you may not distribute the modified material.
- **Ethical AI Use**: You must not use the work for harmful purposes.

**Prohibitions:**

- **Modify**: You may not distribute modified versions.
- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-NoDerivatives License Version 1.0 (UIM-BY-ND-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Use**: Granted for any purpose, including commercial uses.

**2. Conditions**

- **Attribution (BY)**: As above.
- **NoDerivatives (ND)**: You may not distribute modified versions of the Work.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Modify**: Distribution of modified works is prohibited.
- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-ND-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-nd-v1.0",
  "version": "1.0",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "NoDerivatives",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "Modify",
    "HarmfulUse"
  ]
}
```

## 6. UIM Attribution-NonCommercial License (UIM-BY-NC-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-NonCommercial License Version 1.0
- **License Code**: **UIM-BY-NC-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: D, A, P, M, S

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Modify**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **NonCommercial (NC)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Commercial Use**
- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, and modify** the work for **non-commercial purposes**.

**Under the following conditions:**

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial**: You may not use the work for commercial purposes.
- **Ethical AI Use**: You must not use the work for harmful purposes.

**Prohibitions:**

- **Commercial Use**: Prohibited.
- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-NonCommercial License Version 1.0 (UIM-BY-NC-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Modify, Use**: Granted for non-commercial purposes only.

**2. Conditions**

- **Attribution (BY)**: As above.
- **NonCommercial (NC)**: You may not use the Work for commercial purposes.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Commercial Use**: Any commercial use is prohibited.
- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-NC-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-nc-v1.0",
  "version": "1.0",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "NonCommercial",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "CommercialUse",
    "HarmfulUse"
  ]
}
```

## 7. UIM Attribution-NonCommercial-ShareAlike License (UIM-BY-NC-SA-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-NonCommercial-ShareAlike License Version 1.0
- **License Code**: **UIM-BY-NC-SA-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: D, A, P, M, S

### Permissions

- **Same as UIM-BY-NC-v1.0**

### Conditions

- **Attribution (BY)**
- **NonCommercial (NC)**
- **ShareAlike (SA)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Commercial Use**
- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, and modify** the work for **non-commercial purposes**.

**Under the following conditions:**

- **Attribution**: As above.
- **NonCommercial**: As above.
- **ShareAlike**: If you remix, transform, or build upon the work, you must distribute your contributions under the same license.
- **Ethical AI Use**: As above.

**Prohibitions:**

- **Commercial Use**: Prohibited.
- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-NonCommercial-ShareAlike License Version 1.0 (UIM-BY-NC-SA-v1.0)

**1. Grant of Rights**

- **Same as UIM-BY-NC-v1.0**

**2. Conditions**

- **Attribution (BY)**: As above.
- **NonCommercial (NC)**: As above.
- **ShareAlike (SA)**: As above.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Commercial Use**: As above.
- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-NC-SA-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-nc-sa-v1.0",
  "version": "1.0",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "NonCommercial",
    "ShareAlike",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "CommercialUse",
    "HarmfulUse"
  ]
}
```

## 8. UIM Attribution-NonCommercial-NoDerivatives License (UIM-BY-NC-ND-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-NonCommercial-NoDerivatives License Version 1.0
- **License Code**: **UIM-BY-NC-ND-v1.0**

### Applicable Artifact Type(s)

- **All Artifact Types**: D, A, P, M, S

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **NonCommercial (NC)**
- **NoDerivatives (ND)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Commercial Use**
- **Modify**
- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, and distribute** the work for **non-commercial purposes**.

**Under the following conditions:**

- **Attribution**: As above.
- **NonCommercial**: As above.
- **NoDerivatives**: As above.
- **Ethical AI Use**: As above.

**Prohibitions:**

- **Commercial Use**: Prohibited.
- **Modify**: Distribution of modified works is prohibited.
- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-NonCommercial-NoDerivatives License Version 1.0 (UIM-BY-NC-ND-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Use**: Granted for non-commercial purposes only.

**2. Conditions**

- **Attribution (BY)**: As above.
- **NonCommercial (NC)**: As above.
- **NoDerivatives (ND)**: As above.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Commercial Use**: As above.
- **Modify**: As above.
- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-NC-ND-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-nc-nd-v1.0",
  "version": "1.0",
  "artifactType": ["Data", "Application", "Model", "Parameters", "SourceCode"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "NonCommercial",
    "NoDerivatives",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "CommercialUse",
    "Modify",
    "HarmfulUse"
  ]
}
```

## 9. UIM Attribution with AI Output Attribution License (UIM-BY-AIATTR-v1.0)

### License Name and Code

- **License Name**: UIM Attribution with AI Output Attribution License Version 1.0
- **License Code**: **UIM-BY-AIATTR-v1.0**

### Applicable Artifact Type(s)

- **Data (D)**

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Modify**
- **Commercial Use**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **AI Output Attribution (AIATTR)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, modify, and use** the data for **any purpose**, including **commercial** and **non-commercial** uses.

**Under the following conditions:**

- **Attribution**: As above.
- **AI Output Attribution**: Any AI system using this data must attribute outputs derived from the data back to the source website.
- **Ethical AI Use**: As above.

**Prohibitions:**

- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution with AI Output Attribution License Version 1.0 (UIM-BY-AIATTR-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Modify, Use**: Granted for any purpose, including commercial uses.

**2. Conditions**

- **Attribution (BY)**: As above.
- **AI Output Attribution (AIATTR)**: Any AI system using this data must include attribution to the source website in its outputs derived from the data.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-AIATTR-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-aiattr-v1.0",
  "version": "1.0",
  "artifactType": ["Data"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "AIOutputAttribution",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "HarmfulUse"
  ]
}
```

## 10. UIM Attribution-NoDerivatives Indexing License (UIM-BY-ND-IO-NoDM-NoMT-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-NoDerivatives Indexing License Version 1.0
- **License Code**: **UIM-BY-ND-IO-NoDM-NoMT-v1.0**

### Applicable Artifact Type(s)

- **Application (A)**

### Permissions

- **Access**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **NoDerivatives (ND)**
- **Indexing Only (IO)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Modify**
- **Data Mining (NoDM)**
- **Model Training (NoMT)**
- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access** and **index** the content for providing search results.

**Under the following conditions:**

- **Attribution**: As above.
- **NoDerivatives**: As above.
- **Indexing Only**: Access and reproduction are permitted solely for indexing and providing search results.
- **Ethical AI Use**: As above.

**Prohibitions:**

- **Modify**: Beyond indexing requirements is prohibited.
- **Data Mining and Model Training**: Prohibited.
- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-NoDerivatives Indexing License Version 1.0 (UIM-BY-ND-IO-NoDM-NoMT-v1.0)

**1. Grant of Rights**

- **Access and Indexing**: You are granted the rights to access and index the content solely for providing search results.

**2. Conditions**

- **Attribution (BY)**: As above.
- **NoDerivatives (ND)**: As above.
- **Indexing Only (IO)**: Use is limited to indexing and providing search results.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Modify**: As above.
- **Data Mining (NoDM)**: As above.
- **Model Training (NoMT)**: As above.
- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-ND-IO-NoDM-NoMT-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-nd-io-nodm-nomt-v1.0",
  "version": "1.0",
  "artifactType": ["Application"],
  "permissions": [
    "Access",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "NoDerivatives",
    "IndexingOnly",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "Modify",
    "DataMining",
    "ModelTraining",
    "HarmfulUse"
  ]
}
```

## 11. UIM Attribution-NoDerivatives Dynamic Content License (UIM-BY-ND-NoMT-NoLTS-v1.0)

### License Name and Code

- **License Name**: UIM Attribution-NoDerivatives Dynamic Content License Version 1.0
- **License Code**: **UIM-BY-ND-NoMT-NoLTS-v1.0**

### Applicable Artifact Type(s)

- **Data (D)**

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Commercial Use**
- **NonCommercial Use**

### Conditions

- **Attribution (BY)**
- **NoDerivatives (ND)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Modify**
- **Model Training (NoMT)**
- **No Long-Term Storage (NoLTS)**
- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access**, **reproduce**, and **distribute** the content for immediate use.

**Under the following conditions:**

- **Attribution**: As above.
- **NoDerivatives**: As above.
- **Ethical AI Use**: As above.

**Prohibitions:**

- **Modify**: Prohibited.
- **Model Training (NoMT)**: Prohibited.
- **No Long-Term Storage (NoLTS)**: Storing content for future use is prohibited.
- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: UIM Attribution-NoDerivatives Dynamic Content License Version 1.0 (UIM-BY-ND-NoMT-NoLTS-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Use**: Granted for immediate use.

**2. Conditions**

- **Attribution (BY)**: As above.
- **NoDerivatives (ND)**: As above.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Modify**: As above.
- **Model Training (NoMT)**: As above.
- **No Long-Term Storage (NoLTS)**: As above.
- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "UIM-BY-ND-NoMT-NoLTS-v1.0",
  "url": "https://uimprotocol.com/licenses/uim-by-nd-nomt-nolts-v1.0",
  "version": "1.0",
  "artifactType": ["Data"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "CommercialUse",
    "NonCommercialUse"
  ],
  "conditions": [
    "Attribution",
    "NoDerivatives",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "Modify",
    "ModelTraining",
    "NoLongTermStorage",
    "HarmfulUse"
  ]
}
```

## 12. Open Data UIM Attribution License (Open-D-UIM-BY-v1.0)

### License Name and Code

- **License Name**: Open Data UIM Attribution License Version 1.0
- **License Code**: **Open-D-UIM-BY-v1.0**

### Applicable Artifact Type

- **Data (D)**

### Permissions

- **Access**
- **Reproduce**
- **Distribute**
- **Modify**
- **Commercial Use**
- **NonCommercial Use**
- **Data Mining**
- **Model Training**
- **Indexing**

### Conditions

- **Attribution (BY)**
- **Ethical AI Use (EAU)**

### Prohibitions

- **Harmful Use**

### Human-Readable Summary

**You are free to:**

- **Access, reproduce, distribute, modify, and use** the data for **any purpose**, including **commercial** and **non-commercial** uses.

**Under the following conditions:**

- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **Ethical AI Use**: You must not use the data for harmful purposes.

**Prohibitions:**

- **Harmful Use**: Prohibited.

### Lawyer-Readable Legal Code

**License Name**: Open Data UIM Attribution License Version 1.0 (Open-D-UIM-BY-v1.0)

**1. Grant of Rights**

- **Access, Reproduce, Distribute, Modify, Use**: Granted for any purpose, including commercial uses.

**2. Conditions**

- **Attribution (BY)**: As above.
- **Ethical AI Use (EAU)**: As above.

**3. Prohibitions**

- **Harmful Use**: As above.

**4. Disclaimer**

- As above.

#### Machine-Readable Code (JSON-LD)

```json
{
  "@context": [
    "https://schema.org/",
    "https://uimprotocol.com/licenses/context"
  ],
  "@type": "License",
  "name": "Open-D-UIM-BY-v1.0",
  "url": "https://uimprotocol.com/licenses/open-d-uim-by-v1.0",
  "version": "1.0",
  "artifactType": ["Data"],
  "permissions": [
    "Access",
    "Reproduction",
    "Distribution",
    "Modification",
    "CommercialUse",
    "NonCommercialUse",
    "DataMining",
    "ModelTraining",
    "Indexing"
  ],
  "conditions": [
    "Attribution",
    "EthicalAIUse"
  ],
  "prohibitions": [
    "HarmfulUse"
  ]
}
```

## Table of UIM Licenses

This table provides a side-by-side comparison of key UIM licenses, helping licensors and users make informed decisions that align with their goals and ethical considerations.

| License Name | License Code | Artifact Types | Permissions | Conditions | Prohibitions | Human-Readable Summary |
|--------------|--------------|----------------|-------------|------------|--------------|------------------------|
| **UIM Public Domain Dedication** | **UIM-PD-v1.0** | All | All permissions | None | None | You are free to use the work for any purpose without any restrictions. No conditions or prohibitions apply. |
| **UIM CC0 Dedication** | **UIM-CC0-v1.0** | All | All permissions | None | None | You are free to use the work for any purpose without any restrictions. No conditions or prohibitions apply. |
| **UIM Attribution License** | **UIM-BY-v1.0** | All | All permissions | Attribution (BY), Ethical AI Use (EAU) | Harmful Use | You are free to use the work for any purpose, provided you give appropriate credit and comply with ethical guidelines. |
| **UIM Attribution-ShareAlike License** | **UIM-BY-SA-v1.0** | All | All permissions | Attribution (BY), ShareAlike (SA), Ethical AI Use (EAU) | Harmful Use | You are free to use the work for any purpose, provided you give credit, share derivatives under the same terms, and comply with ethical guidelines. |
| **UIM Attribution-NoDerivatives License** | **UIM-BY-ND-v1.0** | All | All except Modify | Attribution (BY), NoDerivatives (ND), Ethical AI Use (EAU) | Modify, Harmful Use | You may use and distribute the work unmodified, provided you give credit and comply with ethical guidelines. |
| **UIM Attribution-NonCommercial License** | **UIM-BY-NC-v1.0** | All | All for NonCommercial Use | Attribution (BY), NonCommercial (NC), Ethical AI Use (EAU) | Commercial Use, Harmful Use | You may use and modify the work for non-commercial purposes, provided you give credit and comply with ethical guidelines. |
| **UIM Attribution-NonCommercial-ShareAlike License** | **UIM-BY-NC-SA-v1.0** | All | All for NonCommercial Use | Attribution (BY), NonCommercial (NC), ShareAlike (SA), Ethical AI Use (EAU) | Commercial Use, Harmful Use | You may use and modify the work for non-commercial purposes, share derivatives under the same terms, give credit, and comply with ethical guidelines. |
| **UIM Attribution-NonCommercial-NoDerivatives License** | **UIM-BY-NC-ND-v1.0** | All | All except Modify for NonCommercial Use | Attribution (BY), NonCommercial (NC), NoDerivatives (ND), Ethical AI Use (EAU) | Commercial Use, Modify, Harmful Use | You may use and distribute the work unmodified for non-commercial purposes, provided you give credit and comply with ethical guidelines. |
| **UIM Attribution with AI Output Attribution License** | **UIM-BY-AIATTR-v1.0** | Data | All permissions | Attribution (BY), AI Output Attribution (AIATTR), Ethical AI Use (EAU) | Harmful Use | You are free to use the data for any purpose, provided you give credit, ensure AI outputs attribute back to the source, and comply with ethical guidelines. |
| **UIM Attribution-NoDerivatives Indexing License** | **UIM-BY-ND-IO-NoDM-NoMT-v1.0** | Application | Access, Indexing | Attribution (BY), NoDerivatives (ND), Indexing Only (IO), Ethical AI Use (EAU) | Modify, Data Mining (NoDM), Model Training (NoMT), Harmful Use | You may access and index the content for search purposes, provided you give credit and comply with ethical guidelines. Other uses are prohibited. |
| **UIM Attribution-NoDerivatives Dynamic Content License** | **UIM-BY-ND-NoMT-NoLTS-v1.0** | Data | Access, Reproduce, Distribute | Attribution (BY), NoDerivatives (ND), Ethical AI Use (EAU) | Modify, Model Training (NoMT), No Long-Term Storage (NoLTS), Harmful Use | You may use and distribute the content unmodified, provided you give credit and comply with ethical guidelines. Long-term storage and model training are prohibited. |
| **Open Data UIM Attribution License** | **Open-D-UIM-BY-v1.0** | Data | All permissions | Attribution (BY), Ethical AI Use (EAU) | Harmful Use | You are free to use, modify, and distribute the data for any purpose, provided you give credit and comply with ethical guidelines. |

### Usage Guidance

- **Selecting a License**:
  - **For Maximum Freedom**: Choose **UIM-PD-v1.0** or **UIM-CC0-v1.0** to place your work in the public domain.
  - **For Open Use with Attribution**: Use an **"Open-"** license like **Open-D-UIM-BY-v1.0**.
  - **To Restrict Commercial Use**: Select a license with the **NonCommercial (NC)** condition.
  - **To Prevent Modifications**: Choose a license with the **NoDerivatives (ND)** condition.
  - **To Ensure Ethical Use**: Include the **Ethical AI Use (EAU)** condition.

- **Understanding Obligations**:
  - **Attribution (BY)**: You must give appropriate credit when using the work.
  - **ShareAlike (SA)**: Derivative works must be shared under the same license terms.
  - **Ethical AI Use (EAU)**: You must avoid using the work in harmful applications.

---

## Understanding "Open-" Prefixed Licenses

### Definition and Purpose of "Open-" Licenses

In the UIM Licensing Scheme, the **"Open-"** prefix indicates that:

- **The artifact is offered at no charge.**
- **The license allows for free use, including modification and redistribution.**
- **Some conditions and prohibitions may still apply.**

**Key Characteristics:**

- **Open but Not Unconditional:** While "Open-" licenses promote openness, they may still include certain **conditions** (e.g., Attribution) and **prohibitions** (e.g., prohibiting harmful use).
- **Encourage Collaboration:** They allow users to freely use, modify, and share the work, fostering an open and collaborative environment.
- **Require Compliance with Conditions:** Users must adhere to the specified conditions and prohibitions.

### Examples of "Open-" Licenses

- **Open-D-UIM-BY-v1.0:** An open data license requiring attribution and compliance with ethical AI use.
- **Open-S-UIM-BY-SA-v1.0:** An open source code license requiring attribution and share-alike conditions.

## Understanding UIM-PD-v1.0 and UIM-CC0-v1.0 Licenses

### UIM Public Domain Dedication (UIM-PD-v1.0)

- **Definition:** The work is dedicated to the public domain, relinquishing all rights to the fullest extent permitted by law.
- **Key Characteristics:**
  - **No Conditions or Prohibitions:** Users are free to use the work for any purpose without any restrictions.
  - **No Attribution Required:** Users are not required to provide attribution.
  - **Unconditional Freedom:** Maximizes the freedom of the work, placing it entirely in the public domain.

### UIM CC0 Dedication (UIM-CC0-v1.0)

- **Definition:** Similar to UIM-PD-v1.0, CC0 dedicates the work to the public domain using the Creative Commons Zero dedication.
- **Key Characteristics:**
  - **No Conditions or Prohibitions:** Complete waiver of rights, allowing unrestricted use.
  - **Legal Robustness:** Designed to be effective internationally, where public domain dedication may not be recognized.

## Differentiating "Open-" Licenses from UIM-PD-v1.0 and UIM-CC0-v1.0

### Key Differences

**1. Presence of Conditions and Prohibitions**

- **"Open-" Licenses:**
  - **Conditions May Apply:** Require users to comply with certain conditions, such as Attribution (BY) or ShareAlike (SA).
  - **Prohibitions May Apply:** May include prohibitions against harmful use (e.g., Ethical AI Use (EAU)).

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**
  - **No Conditions or Prohibitions:** Users are granted unconditional freedom to use the work in any way.

**2. Requirement for Attribution**

- **"Open-" Licenses:**
  - **Attribution Required:** Typically include the Attribution (BY) condition, requiring users to credit the original creator.

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**
  - **Attribution Not Required:** Users are not obligated to provide attribution.

**3. Legal Rights Reserved**

- **"Open-" Licenses:**
  - **Some Rights Reserved:** While promoting openness, certain rights are reserved to ensure compliance with conditions and prohibitions.

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**
  - **No Rights Reserved:** All rights are waived, and the work is placed entirely in the public domain.

### How They Are Differentiated in the UIM Licensing Scheme

**1. Naming Convention**

- **"Open-" Licenses:**
  - **Prefixed with "Open-"**: Indicates an open license with some conditions and/or prohibitions.
  - **Example:** **Open-D-UIM-BY-v1.0**

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**
  - **Specific License Codes without "Open-" Prefix:**
    - **UIM-PD-v1.0:** Public Domain Dedication.
    - **UIM-CC0-v1.0:** CC0 Dedication.

**2. License Elements**

- **"Open-" Licenses:**
  - **Include License Elements:** Combine permissions, conditions, and prohibitions.
  - **Example Elements:** BY (Attribution), SA (ShareAlike), EAU (Ethical AI Use).

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**
  - **No License Elements:** Do not include conditions or prohibitions.

**3. Legal Code Content**

- **"Open-" Licenses:**
  - **Contain Terms and Conditions:** Legal code specifies the rights granted and the obligations of the user.
  - **Includes Conditions:** Users must adhere to specified conditions.

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**
  - **Simple Dedication Statement:** Legal code focuses on dedicating the work to the public domain.
  - **No User Obligations:** No conditions or prohibitions are imposed on the user.

### Practical Implications

- **For Users:**

  - **"Open-" Licenses:**
    - **Must Comply with Conditions:** Users need to be aware of and comply with any conditions like providing attribution.
    - **Subject to Prohibitions:** Must avoid prohibited uses, such as harmful applications.

  - **UIM-PD-v1.0 and UIM-CC0-v1.0:**
    - **Unrestricted Use:** Users can use the work without any obligations or restrictions.

- **For Licensors:**

  - **"Open-" Licenses:**
    - **Maintain Some Control:** Can ensure attribution and prevent certain types of misuse.
    - **Promote Ethical Use:** Can include provisions to discourage harmful applications.

  - **UIM-PD-v1.0 and UIM-CC0-v1.0:**
    - **Relinquish All Rights:** Cannot impose any conditions or control over how the work is used.

### Summary Table of Differences

| Aspect                   | "Open-" Licenses                          | UIM-PD-v1.0 and UIM-CC0-v1.0              |
|--------------------------|-------------------------------------------|-------------------------------------------|
| **Naming Convention**    | Prefixed with "Open-"                     | Specific codes without "Open-" prefix     |
| **Conditions Present**   | Yes (e.g., Attribution, ShareAlike)       | No                                        |
| **Prohibitions Present** | Yes (e.g., Harmful Use prohibited)        | No                                        |
| **Attribution Required** | Yes                                       | No                                        |
| **Legal Rights Reserved**| Some rights reserved                      | No rights reserved                        |
| **User Obligations**     | Must comply with conditions and prohibitions| No obligations                            |
| **Use Freedom**          | Free use within conditions and prohibitions| Unrestricted free use                     |


### Differentiation in the UIM Licensing Scheme

- **"Open-" Licenses** are open licenses that promote free use and sharing **while still imposing certain conditions and prohibitions**, such as requiring attribution or prohibiting harmful use.

- **UIM-PD-v1.0 and UIM-CC0-v1.0** are **unconditional dedications to the public domain**, granting users unrestricted freedom to use the work without any conditions or prohibitions.

**Key Takeaways:**

- **"Open-" Prefixed Licenses:**
  - Provide openness **with some retained rights**.
  - Require users to **adhere to specific conditions**, such as giving attribution.
  - Allow licensors to **promote ethical use** and maintain some level of control.

- **UIM-PD-v1.0 and UIM-CC0-v1.0 Licenses:**
  - **Fully relinquish control**, placing the work in the public domain.
  - Do not require attribution or impose any conditions.
  - Offer **maximum freedom** to users.

**Implications for License Selection:**

- **Licensors who want to ensure certain conditions are met**, such as receiving attribution or preventing harmful uses, should choose an **"Open-" license** with the appropriate conditions and prohibitions.

- **Licensors willing to release their work without any restrictions** should choose the **UIM-PD-v1.0** or **UIM-CC0-v1.0** licenses.

### When to Use Each License Type:**

- **"Open-" Licenses:**

  - **Best For:** Licensors who want to promote open use but still require attribution or enforce ethical considerations.
  - **Examples:** Open-source software projects, open datasets where credit is important.

- **UIM-PD-v1.0 and UIM-CC0-v1.0:**

  - **Best For:** Licensors who wish to contribute to the public domain and have no interest in retaining any rights or imposing any conditions.
  - **Examples:** Government data releases, creators who want to maximize dissemination without any control.

**Legal Robustness:**

- **UIM-CC0-v1.0** may be preferred in jurisdictions where dedicating works to the public domain is not straightforward, as the CC0 dedication includes a fallback license granting broad permissions.

## Conclusion

The above license combinations provide comprehensive coverage of feasible and non-contradictory licenses within the UIM Licensing Scheme. Each license is carefully constructed to address specific permissions, conditions, and prohibitions, enabling licensors to protect their content while promoting responsible and ethical use.

*Note: This list includes key license combinations that cover a wide range of use cases. Additional combinations can be created by combining the license elements, ensuring they remain feasible and non-contradictory.*

## Additional Resources

- **Creative Commons Licenses**: [https://creativecommons.org/licenses/](https://creativecommons.org/licenses/)
- **Responsible AI Licenses (RAIL)**: [https://www.licenses.ai/](https://www.licenses.ai/)
- **Schema.org**: [https://schema.org/](https://schema.org/)
- **JSON-LD Specification**: [https://json-ld.org/](https://json-ld.org/)
```

--------------------------------------------------------------------------------

### File: uim-odrl-vocab.md
```
Path: uim-odrl-vocab.md
Size: 17.84 KB
Last Modified: 2024-09-23 19:05:54
```

**Contents:**
```
# ODRL Vocabulary Document for the Unified Intent Mediator (UIM) Protocol Namespace

**Date:** September 23, 2024

**Version:** 0.1

---

## **Table of Contents**

1. [Introduction](#introduction)
2. [Namespace Declarations](#namespace-declarations)
3. [Vocabulary Definitions](#vocabulary-definitions)
   - [Actions](#actions)
   - [Constraints](#constraints)
   - [Duties](#duties)
   - [Assignee Types](#assignee-types)
4. [JSON-LD Context](#json-ld-context)
5. [Policy Examples](#policy-examples)
   - [1. Search Engines](#1-search-engines)
   - [2. Non-Commercial AI](#2-non-commercial-ai)
   - [3. Attribution-Based AI](#3-attribution-based-ai)
   - [4. Protecting Data Freshness](#4-protecting-data-freshness)
   - [5. Preventing Unwanted Commercial Use](#5-preventing-unwanted-commercial-use)
6. [Recommendations for Implementers](#recommendations-for-implementers)
7. [References](#references)
8. [Disclaimer](#disclaimer)

---

## **Introduction**

This document defines the Open Digital Rights Language (ODRL) Vocabulary for the Unified Intent Mediator (UIM) Protocol Namespace. The vocabulary is designed to address the need for a standardized taxonomy for AI data use, enabling website owners to express permissions, prohibitions, and obligations regarding the use of their data by AI systems.

By leveraging ODRL and defining specific terms within the UIM namespace, this vocabulary provides a framework for communicating data usage policies effectively and machine-readably, promoting responsible and ethical AI development.

## **Namespace Declarations**

To ensure clarity and avoid naming conflicts, we declare the following namespaces:

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  }
}
```

## **Vocabulary Definitions**

This section defines the custom terms used in the UIM protocol namespace, including actions, constraints, duties, and assignee types. Each term is extensively documented to ensure clear understanding and interoperability.

### **Actions**

#### **uim:aiTraining**

- **Type:** `odrl:Action`
- **Label:** "AI Training"
- **Definition:** Use of data for training AI models.
- **Comment:** Represents the use of data to train AI models, including machine learning algorithms and neural networks.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:aiTraining",
  "@type": "odrl:Action",
  "rdfs:label": "AI Training",
  "rdfs:comment": "Use of data for training AI models."
}
```

#### **uim:aiResearch**

- **Type:** `odrl:Action`
- **Label:** "AI Research"
- **Definition:** Use of data for AI research purposes.
- **Comment:** Covers the use of data in AI research, typically within academic or non-commercial settings.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:aiResearch",
  "@type": "odrl:Action",
  "rdfs:label": "AI Research",
  "rdfs:comment": "Use of data for AI research purposes."
}
```

#### **uim:aiUse**

- **Type:** `odrl:Action`
- **Label:** "AI Use"
- **Definition:** General use of data in AI applications.
- **Comment:** Encompasses any use of data in AI applications, including training, inference, and model development.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:aiUse",
  "@type": "odrl:Action",
  "rdfs:label": "AI Use",
  "rdfs:comment": "General use of data in AI applications."
}
```

#### **uim:index**

- **Type:** `odrl:Action`
- **Label:** "Index"
- **Definition:** Crawling data for indexing and search purposes.
- **Equivalent to:** `odrl:reproduce`
- **Comment:** Used by search engines to crawl and index content for search purposes.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "uim:index",
  "@type": "odrl:Action",
  "rdfs:label": "Index",
  "rdfs:comment": "Crawling data for indexing and search purposes.",
  "skos:exactMatch": "odrl:reproduce"
}
```

#### **uim:search**

- **Type:** `odrl:Action`
- **Label:** "Search"
- **Definition:** Making indexed data available for search queries.
- **Equivalent to:** `odrl:distribute`
- **Comment:** Involves providing search capabilities over indexed content.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@id": "uim:search",
  "@type": "odrl:Action",
  "rdfs:label": "Search",
  "rdfs:comment": "Making indexed data available for search queries.",
  "skos:exactMatch": "odrl:distribute"
}
```

#### **odrl:derive**

We use the standard `odrl:derive` action to represent creating derivative works or AI models based on the data.

### **Constraints**

#### **odrl:purpose**

- **Type:** `odrl:Constraint`
- **Label:** "Purpose"
- **Definition:** Specifies the intended purpose of the action.
- **Comment:** Used to constrain actions based on the purpose, such as non-commercial use.

#### **uim:assigneeType**

- **Type:** `odrl:LeftOperand`
- **Label:** "Assignee Type"
- **Definition:** Specifies the type of assignee (e.g., non-profit, commercial).
- **Comment:** Limits the policy to specific types of assignees.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:assigneeType",
  "@type": "odrl:LeftOperand",
  "rdfs:label": "Assignee Type",
  "rdfs:comment": "Specifies the type of assignee (e.g., non-profit, commercial)."
}
```

#### **uim:dataFreshness**

- **Type:** `odrl:LeftOperand`
- **Label:** "Data Freshness"
- **Definition:** Specifies the allowed age of data for use.
- **Comment:** Limits the use of data based on its age to ensure currency.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:dataFreshness",
  "@type": "odrl:LeftOperand",
  "rdfs:label": "Data Freshness",
  "rdfs:comment": "Specifies the allowed age of data for use."
}
```

#### **uim:compensationRequired**

- **Type:** `odrl:LeftOperand`
- **Label:** "Compensation Required"
- **Definition:** Indicates that compensation is required for use.
- **Comment:** Specifies that a fee or compensation is needed before the action is permitted.

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:compensationRequired",
  "@type": "odrl:LeftOperand",
  "rdfs:label": "Compensation Required",
  "rdfs:comment": "Indicates that compensation is required for use."
}
```

### **Duties**

#### **odrl:attribution**

- **Type:** `odrl:Action`
- **Label:** "Attribution"
- **Definition:** Duty to attribute the source when using the data.
- **Comment:** Requires users to provide appropriate credit to the content owner.

### **Assignee Types**

#### **uim:NonProfitOrganization**

- **Type:** `skos:Concept`
- **Label:** "Non-Profit Organization"
- **Definition:** Legally recognized non-profit organizations.
- **Comment:** Organizations that operate for charitable, educational, or scientific purposes without profit.

```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:NonProfitOrganization",
  "@type": "skos:Concept",
  "rdfs:label": "Non-Profit Organization",
  "rdfs:comment": "Legally recognized non-profit organizations."
}
```

#### **uim:CommercialEntity**

- **Type:** `skos:Concept`
- **Label:** "Commercial Entity"
- **Definition:** Entities operating for profit.
- **Comment:** Businesses and organizations that engage in commercial activities.

```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
  },
  "@id": "uim:CommercialEntity",
  "@type": "skos:Concept",
  "rdfs:label": "Commercial Entity",
  "rdfs:comment": "Entities operating for profit."
}
```

## **JSON-LD Context**

For completeness, the JSON-LD context that incorporates all the namespaces and prefixes used in the vocabulary is provided below:

```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "uim": "http://uimprotocol.com/uim/odrl/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  }
}
```

## **Policy Examples**

Below are ODRL policy examples using JSON-LD serialization, demonstrating how the vocabulary can be applied to express various data usage policies.

### **1. Search Engines**

**Use Case:** Search Engines (Allow Crawling Only for Indexing and Search Purposes)

**Policy:** Allow crawling only for indexing and search purposes.

```json
{
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    {
      "uim": "http://uimprotocol.com/uim/odrl/"
    }
  ],
  "@type": "Set",
  "@id": "https://example.com/policy/search-engine",
  "permission": [
    {
      "target": "https://example.com/",
      "action": [
        {
          "id": "uim:index"
        },
        {
          "id": "uim:search"
        }
      ]
    }
  ],
  "prohibition": [
    {
      "target": "https://example.com/",
      "action": [
        {
          "id": "uim:aiTraining"
        },
        {
          "id": "uim:aiUse"
        }
      ]
    }
  ],
  "assigner": {
    "uid": "https://example.com/owner"
  }
}
```

**Explanation:**

- **Permission:** Allows actions `uim:index` and `uim:search` on the target website.
- **Prohibition:** Prohibits actions `uim:aiTraining` and `uim:aiUse` on the target.
- **Assigner:** The policy is assigned by the website owner.

### **2. Non-Commercial AI**

**Use Case:** Non-Commercial AI (Permit Data Use for AI Research or Development by Non-Profit Organizations or for Non-Commercial Applications)

**Policy:** Permit data use for AI research or development by non-profit organizations or for non-commercial applications.

```json
{
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    {
      "uim": "http://uimprotocol.com/uim/odrl/"
    }
  ],
  "@type": "Set",
  "@id": "https://example.com/policy/non-commercial-ai",
  "permission": [
    {
      "target": "https://example.com/dataset",
      "action": {
        "id": "uim:aiResearch"
      },
      "constraint": [
        {
          "leftOperand": "purpose",
          "operator": "eq",
          "rightOperand": "http://www.w3.org/ns/odrl/2/non-commercial"
        }
      ],
      "assignee": {
        "uid": "*",
        "constraint": [
          {
            "leftOperand": "uim:assigneeType",
            "operator": "eq",
            "rightOperand": "uim:NonProfitOrganization"
          }
        ]
      }
    }
  ],
  "prohibition": [
    {
      "target": "https://example.com/dataset",
      "action": [
        {
          "id": "uim:aiTraining"
        },
        {
          "id": "commercialize"
        }
      ]
    }
  ],
  "assigner": {
    "uid": "https://example.com/owner"
  }
}
```

**Explanation:**

- **Permission:** Allows `uim:aiResearch` action with constraints:
  - **Purpose Constraint:** The purpose must be `non-commercial`.
  - **Assignee Constraint:** Assignee must be of type `uim:NonProfitOrganization`.
- **Prohibition:** Prohibits `uim:aiTraining` and `commercialize` actions.
- **Assigner:** The policy is assigned by the dataset owner.

### **3. Attribution-Based AI**

**Use Case:** Attribution-Based AI (Allow Data Use Only If the Resulting AI System Attributes Its Output Back to the Source Website)

**Policy:** Allow data use only if the resulting AI system attributes its output back to the source website.

```json
{
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    {
      "uim": "http://uimprotocol.com/uim/odrl/"
    }
  ],
  "@type": "Set",
  "@id": "https://example.com/policy/attribution-ai",
  "permission": [
    {
      "target": "https://example.com/content",
      "action": {
        "id": "uim:aiUse"
      },
      "duty": [
        {
          "action": {
            "id": "attribute"
          },
          "target": "https://example.com/original-source"
        }
      ]
    }
  ],
  "assigner": {
    "uid": "https://example.com/owner"
  }
}
```

**Explanation:**

- **Permission:** Allows `uim:aiUse` action with a duty to perform `attribute` action.
- **Duty:** Requires attribution to `https://example.com/original-source`.
- **Assigner:** The policy is assigned by the content owner.

### **4. Protecting Data Freshness**

**Use Case:** Dynamic websites, such as news sites, limit the use of their content to prevent AI models from being trained on outdated information.

**Policy:** Limit the use of content to prevent AI models from being trained on outdated information.

```json
{
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    {
      "uim": "http://uimprotocol.com/uim/odrl/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": "Set",
  "@id": "https://example.com/policy/data-freshness",
  "permission": [
    {
      "target": "https://example.com/news",
      "action": {
        "id": "uim:aiUse"
      },
      "constraint": [
        {
          "leftOperand": "uim:dataFreshness",
          "operator": "lt",
          "rightOperand": "P7D",
          "dataType": "xsd:duration"
        }
      ]
    }
  ],
  "assigner": {
    "uid": "https://example.com/owner"
  }
}
```

**Explanation:**

- **Permission:** Allows `uim:aiUse` action with a constraint that data must be less than 7 days old (`P7D`).
- **Data Type:** Specifies `xsd:duration` for the duration format.
- **Assigner:** The policy is assigned by the news website owner.

### **5. Preventing Unwanted Commercial Use**

**Use Case:** Websites behind paywalls or dependent on advertising revenue restrict the use of their data for commercial AI applications.

**Policy:** Restrict the use of data for commercial AI applications.

```json
{
  "@context": [
    "http://www.w3.org/ns/odrl.jsonld",
    {
      "uim": "http://uimprotocol.com/uim/odrl/"
    }
  ],
  "@type": "Set",
  "@id": "https://example.com/policy/no-commercial-ai",
  "permission": [
    {
      "target": "https://example.com/premium-content",
      "action": {
        "id": "uim:aiUse"
      },
      "constraint": [
        {
          "leftOperand": "purpose",
          "operator": "eq",
          "rightOperand": "http://www.w3.org/ns/odrl/2/non-commercial"
        }
      ]
    }
  ],
  "prohibition": [
    {
      "target": "https://example.com/premium-content",
      "action": [
        {
          "id": "uim:aiTraining"
        },
        {
          "id": "commercialize"
        }
      ]
    }
  ],
  "assigner": {
    "uid": "https://example.com/owner"
  }
}
```

**Explanation:**

- **Permission:** Allows `uim:aiUse` action for non-commercial purposes.
- **Prohibition:** Prohibits `uim:aiTraining` and `commercialize` actions.
- **Assigner:** The policy is assigned by the premium content provider.

## **Recommendations for implementers**

- **Use Standard Terms Where Possible:** To enhance interoperability, prefer standard ODRL terms when suitable. For example, use `odrl:derive` instead of defining a custom `uim:derive` action.

- **Define Custom Terms Carefully:** When custom terms are necessary, ensure they are thoroughly documented and properly namespaced to avoid conflicts.

- **Ensure Policy Clarity:** Policies should be unambiguous. Clearly specify permissions, prohibitions, and obligations to prevent misinterpretation.

- **Compliance with Legal Frameworks:** Ensure that the policies and terms comply with relevant laws and regulations, such as GDPR for personal data protection.

## **References**

1. **ODRL Information Model:** [https://www.w3.org/TR/odrl-model/](https://www.w3.org/TR/odrl-model/)
2. **ODRL Vocabulary & Expression:** [https://www.w3.org/TR/odrl-vocab/](https://www.w3.org/TR/odrl-vocab/)
3. **ODRL JSON-LD Context:** [https://www.w3.org/ns/odrl.jsonld](https://www.w3.org/ns/odrl.jsonld)
4. **SKOS (Simple Knowledge Organization System):** [https://www.w3.org/TR/skos-reference/](https://www.w3.org/TR/skos-reference/)
5. **ISO 8601 Duration Format:** [https://en.wikipedia.org/wiki/ISO_8601#Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)
6. **W3C RDF Schema (RDFS):** [https://www.w3.org/TR/rdf-schema/](https://www.w3.org/TR/rdf-schema/)

## **Disclaimer**

This document is provided as a template and requires adaptation to the specific needs and legal considerations of the implementing organization. It is recommended to consult legal experts when defining policies that have legal implications.

The UIM protocol authors and contributors are not responsible for any legal implications arising from the use of this document. However, we welcome feedback and contributions to improve the document and the UIM protocol. 

We will strive to:

- **Maintain Updated Vocabulary:** Regularly review and update the vocabulary to accommodate new use cases and changes in AI technology and data usage practices.

- **Promote Adoption:** Encourage stakeholders to adopt this vocabulary to establish a common language for expressing AI data usage policies.

- **Provide Tooling Support:** Develop tools and libraries to assist in creating, parsing, and enforcing ODRL policies using this vocabulary.```

--------------------------------------------------------------------------------

### File: uim-prototypes-intro.md
```
Path: uim-prototypes-intro.md
Size: 5.23 KB
Last Modified: 2024-09-16 20:08:32
```

**Contents:**
```
# Implementation Guide based on UIM Mock Agent and Mock Web Service

This guide will walk you through the setup and usage of the UIM Mock Agent and Mock Web Service. The UIM Mock Agent simulates an AI agent interacting with a mock web service according to the Unified Intent Mediator (UIM) specification. It demonstrates the discovery and execution of intents, issuance of Policy Adherence Tokens (PATs), policy retrieval and signing, and secure key management for multiple web services. 

By following the steps outlined, you can simulate the discovery and execution of intents, manage keys, retrieve and sign policies, and handle PAT issuance. This setup demonstrates the core functionalities of the Unified Intent Mediator (UIM) specification in a mock environment.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/synaptiai/uim-protocol.git
cd uim-mock-webservice
```

### 2. Install Dependencies

Install the required dependencies for both the mock agent and the mock web service:

```bash
pip install -r requirements.txt
```

### 3. Running the Mock Web Service

The mock web service is implemented using FastAPI and provides endpoints for discovering intents, retrieving policies, issuing PATs, and executing intents.

#### Start the Web Service

Run the web service using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 4000
```

This will start the web service on [http://localhost:4000](http://localhost:4000).
Keep this running in a separate terminal window.

#### Web Service Endpoints

The FastAPI framework provides automatic interactive documentation for the web service endpoints. You can access it by navigating to [http://localhost:4000/docs](http://localhost:4000/docs). This will open a Swagger UI page with the available endpoints and their documentation. The following endpoints are available:

- GET /agents.json: Returns the available intents and service information.
- GET /uim-policy.json: Returns the ODRL policy for the service.
- POST /pat/issue: Issues a PAT after verifying the signed policy.
- POST /uim/execute: Executes an intent using the provided parameters and PAT.

### 4. Running the Mock Agent

The mock agent is a command-line interface (CLI) application that interacts with the mock web service. It allows you to manage keys, discover intents, view policies, sign policies, get PATs, and execute intents.

#### Start the Mock Agent CLI

Navigate to the uim-mock-agent directory and run the CLI interface:

```bash
cd uim-mock-agent
python src/cli_interface.py
```

#### CLI Menu Options

The CLI provides the following options:

- Manage Keys: Generate new key pairs or view existing key pairs for a service.
- Discover Intents: Fetch and display available intents from the web service.
- View Policy: Retrieve and display the ODRL policy from the web service.
- Sign Policy and Get PAT: Sign the policy and request a PAT from the web service.
- Execute Intent: Execute an intent using the provided parameters and PAT.
- Exit: Exit the CLI.

## Detailed Usage

### 1. Manage Keys

This option allows you to generate new RSA key pairs or view existing key pairs for a service URL.

- Generate new key pair: Creates a new RSA key pair and saves it under the keys/ directory.
- View existing key pair: Displays the private and public keys for the specified service URL.
- Set current service URL: Sets the service URL for subsequent operations.

### 2. Discover Intents

Fetches the agents.json from the web service and displays the available intents along with their descriptions and input parameters.

### 3. View Policy

Fetches the uim-policy.json from the web service and displays the ODRL policy, including permissions, prohibitions, parties, and assets.

### 4. Sign Policy and Get PAT

- Fetch Policy: Retrieves the ODRL policy from the web service.
- Sign Policy: Signs the policy using the agent's private key.
- Get PAT: Submits the signed policy to the web service and requests a PAT. The PAT is used for authenticating subsequent intent executions.

### 5. Execute Intent

- Enter Intent UID: Specify the UID of the intent to execute.
- Enter Parameters: Provide the required parameters for the intent.
- Execute: Sends a request to the web service to execute the intent using the provided parameters and PAT.

### Example Workflow

- Start the Web Service:

```bash
cd uim-mock-webservice
uvicorn main:app --host 0.0.0.0 --port 4000
```

- Start the Mock Agent CLI:

```bash
cd uim-mock-agent
python src/cli_interface.py
```

- Set Current Service URL:
  - Select "Manage Keys" (Option 1)
  - Select "Set current service URL" (Option 3)
  - Enter [http://localhost:4000](http://localhost:4000)
- Generate Key Pair:
  - Select "Manage Keys" (Option 1)
  - Select "Generate new key pair" (Option 1)
- Discover Intents:
  - Select "Discover Intents" (Option 2)
- View Policy:
  - Select "View Policy" (Option 3)
- Sign Policy and Get PAT:
  - Select "Sign Policy and Get PAT" (Option 4)
  - Enter your agent ID when prompted
- Execute Intent:
  - Select "Execute Intent" (Option 5)
  - Enter the intent UID (e.g., fakerealestate.com:searchProperty:v1)
  - Enter the required parameters (e.g., location, min_price, max_price, property_type)
```

--------------------------------------------------------------------------------

### File: uim-tdmrep-relation.md
```
Path: uim-tdmrep-relation.md
Size: 10.45 KB
Last Modified: 2024-09-24 21:50:16
```

**Contents:**
```
# How the UIM Protocol Relates to the TDMrep Specification

## Introduction

The **Unified Intent Mediator (UIM) Protocol** and the **Text and Data Mining Reservation Protocol (TDMrep)** both address the challenges of managing rights and permissions in the context of automated data access and processing. They aim to facilitate lawful and ethical use of digital content, particularly in relation to text and data mining (TDM) activities.

This is an exploration of how the UIM Protocol relates to the TDMrep specification, highlighting their similarities, differences, and potential areas of integration or synergy.

## Overview of the TDMrep Specification

### Purpose and Context

The **TDMrep** (Text and Data Mining Reservation Protocol) is a specification developed by the W3C's TDM Reservation Protocol Community Group. It provides a standardized, machine-readable method for rights holders to express their reservations concerning the use of their content for text and data mining purposes, in compliance with the EU's Directive on Copyright in the Digital Single Market (Directive (EU) 2019/790), particularly Article 4(3).

### Key Features

- **Machine-Readable Rights Reservations**: Allows rights holders to declare their reservation of rights for TDM activities in a way that can be automatically detected and respected by data miners.
- **Multiple Implementation Methods**:
  - **HTTP Headers**: Rights reservations can be declared in HTTP response headers.
  - **HTML Meta Tags**: Embedding rights reservations within HTML content using meta tags.
  - **Robots.txt Extensions**: Utilizing the `robots.txt` file to include TDM-specific directives.
- **Policy Specification**: Provides a way to reference or include a TDM policy, which may offer information about licensing options or terms under which TDM is permitted.
- **Granular Control**: Rights holders can specify reservations at various levels, including entire domains, specific directories, or individual resources.

### Compliance with EU Regulations

The TDMrep specification is designed to meet the requirements of Article 4(3) of the EU Copyright Directive, which allows rights holders to opt out of the TDM exception for commercial purposes by expressing their reservations in an appropriate manner, such as machine-readable metadata.

## Overview of the UIM Protocol

### Purpose and Context

The **Unified Intent Mediator (UIM) Protocol** provides a standardized framework for AI agents to interact with web services through well-defined intents, metadata, and execution methods. It focuses on:

- **Standardization**: Offering consistent interfaces for AI agents and web services.
- **Security and Compliance**: Enforcing policies and permissions using machine-readable formats.
- **Policy Enforcement**: Using the Open Digital Rights Language (ODRL) to define permissions, prohibitions, and obligations associated with intents and the data provided by web services.
- **Authentication and Authorization**: Employing Policy Adherence Tokens (PATs) to ensure that only authorized agents can access services and that they agree to comply with the defined policies.

### Key Features

- **Intent Definitions**: Describes actions that AI agents can perform, including input/output parameters and execution endpoints.
- **Service Metadata**: Provides detailed information about the web service, including policies and compliance standards.
- **Policy Integration**: Uses ODRL policies to express rights, permissions, and obligations in a machine-readable format.
- **Secure Interactions**: Requires AI agents to authenticate and agree to policies before accessing resources.

## Relationship Between UIM Protocol and TDMrep Specification

### Common Goals

Both the UIM Protocol and the TDMrep specification aim to:

- **Facilitate Legal Compliance**: Ensure that automated systems respect the rights and reservations of content owners.
- **Use Machine-Readable Formats**: Employ standardized, machine-readable methods to express rights and permissions, enabling automated detection and compliance.
- **Protect Rights Holders**: Provide mechanisms for rights holders to control how their content is accessed and used by automated agents.

### Differences in Scope and Approach

- **Layer of Operation**:
  - **TDMrep**: Focuses on expressing rights reservations at the content level, primarily concerning the use of content for TDM activities.
  - **UIM Protocol**: Operates at the interaction layer between AI agents and web services, defining how agents should interact with services and enforce policies during these interactions.

- **Policy Expression**:
  - **TDMrep**: Uses methods like HTTP headers, HTML meta tags, and robots.txt to declare TDM reservations.
  - **UIM Protocol**: Uses ODRL policies embedded in service metadata to define a wide range of permissions, prohibitions, and obligations.

- **Enforcement Mechanisms**:
  - **TDMrep**: Relies on data miners to detect and respect rights reservations expressed in standard locations.
  - **UIM Protocol**: Enforces policies through PATs, requiring agents to agree to policies before accessing services.

### Potential Integration and Synergy

1. **Complementary Use of Machine-Readable Policies**

   - **Integration of TDMrep Declarations in UIM Policies**:
     - The UIM Protocol's ODRL policies could reference or incorporate TDMrep declarations, ensuring that AI agents interacting via the UIM Protocol are aware of and comply with TDM reservations expressed through TDMrep.
     - For example, an ODRL policy in the UIM Protocol could include a prohibition on TDM activities if a TDMrep reservation is detected.

2. **Unified Policy Enforcement**

   - **Enhancing Compliance**:
     - By integrating TDMrep rights reservations into the UIM Protocol's policy framework, AI agents using the UIM Protocol would be required to respect TDM reservations as part of their policy adherence.
     - This ensures a more robust enforcement mechanism compared to relying solely on agents voluntarily checking for TDMrep declarations.

3. **Standardization Efforts**

   - **Alignment of Standards**:
     - Both initiatives could collaborate to align their standards, promoting broader adoption and simplifying compliance for AI agents and web services.
     - For instance, the UIM Protocol could adopt or reference TDMrep methods for expressing TDM reservations, providing a consistent approach across different layers.

4. **Granular Control over Content Usage**

   - **Fine-Grained Permissions**:
     - The UIM Protocol's use of ODRL allows for detailed policies, including constraints and conditions under which content may be used.
     - Incorporating TDMrep's granularity in rights reservations can enhance the UIM Protocol's ability to respect rights at a more detailed level.

5. **Legal Compliance and Risk Mitigation**

   - **Compliance with EU Regulations**:
     - By integrating TDMrep specifications, the UIM Protocol can help AI agents and web services comply with the EU's legal requirements concerning TDM activities.
     - This reduces legal risks for both service providers and AI agents operating within the EU.

## Practical Scenarios

### Scenario 1: AI Agent Accessing Web Content via UIM Protocol

- **Context**: An AI agent wishes to access data from a web service using the UIM Protocol.
- **Action**:
  - The agent requests a PAT and agrees to the service's ODRL policies.
  - The service's policy includes a clause referencing TDMrep reservations.
- **Outcome**:
  - The agent is required to check for any TDMrep declarations before proceeding.
  - If a TDM reservation is detected, the agent must comply by refraining from TDM activities or obtaining appropriate permissions.

### Scenario 2: Web Service Expressing TDM Reservations

- **Context**: A web service wants to prevent unauthorized TDM activities on its content.
- **Action**:
  - Implements TDMrep declarations via HTTP headers and meta tags.
  - Updates its UIM Protocol policies to include prohibitions on TDM activities, referencing the TDMrep declarations.
- **Outcome**:
  - AI agents using the UIM Protocol are bound by the service's policies, which now explicitly prohibit TDM activities in accordance with the TDMrep reservations.
  - Ensures consistent enforcement of rights reservations across both content-level and interaction-level policies.

## Challenges and Considerations

### Ensuring Compliance by AI Agents

- **Challenge**:
  - Agents may not be designed to detect or respect TDMrep declarations outside the UIM Protocol.
- **Solution**:
  - The UIM Protocol can mandate that agents must check for TDMrep reservations as part of policy compliance.
  - Provide guidelines or tools for agents to detect and interpret TDMrep declarations.

### Complexity of Implementation

- **Challenge**:
  - Integrating multiple standards and specifications can increase the complexity for developers.
- **Solution**:
  - Develop libraries or SDKs that abstract the complexity, providing seamless integration between UIM Protocol policies and TDMrep declarations.
  - Adopting or referencing TDMrep methods in the UIM Protocol can simplify implementation.

### Adoption and Awareness

- **Challenge**:
  - Widespread adoption of both the UIM Protocol and TDMrep is necessary for maximum effectiveness.
- **Solution**:
  - Collaborative efforts to promote both standards, highlighting the benefits of integrated compliance and rights management.

## Conclusion

The **UIM Protocol** and the **TDMrep specification** address complementary aspects of rights management in the context of AI and automated data processing:

- **UIM Protocol**: Focuses on standardizing AI agent interactions with web services and enforcing policies at the interaction layer.
- **TDMrep**: Provides a method for rights holders to express TDM reservations at the content level.

**Relationship and Integration**:

- Integrating TDMrep declarations into UIM Protocol policies can enhance compliance and enforcement of rights reservations.
- AI agents using the UIM Protocol can be designed to respect both service-level policies and content-level TDM reservations.
- Collaborative standardization efforts can simplify implementation and promote broader adoption.

By aligning the UIM Protocol with the TDMrep specification, stakeholders can achieve a more robust and comprehensive approach to rights management, ensuring that both service-level and content-level rights are respected in automated interactions and data processing activities.

**References**:

- [TDM Reservation Protocol (TDMrep)](https://www.w3.org/community/reports/tdmrep/CG-FINAL-tdmrep-20240202/#abstract)
```

--------------------------------------------------------------------------------

### File: uim-technical-exploration.md
```
Path: uim-technical-exploration.md
Size: 84.97 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# Unified Intent Mediator (UIM) Technical Exploration

The Unified Intent Mediator (UIM) specification provides a standardized protocol for seamless and secure interactions between AI agents and web services. By following this specification, developers can create interoperable solutions that enhance functionality, efficiency, and user experience. Through community collaboration and continuous improvement, the UIM aims to become the industry standard for AI-driven web service interactions.

![UIM vocabulary](images/vocabulary.png)

**Core Vocabulary**:

* **Intent**: An action that can be performed by a web service, including metadata and parameters required for execution.  
* **Parameters**: Inputs required by an intent to perform its action, including name, type, and whether they are required.  
* **Service**: A web service that publishes its capabilities (intents) using the UIM protocol.  
* **Endpoint**: The API endpoint where an intent can be executed.  
* **Metadata**: Descriptive information about an intent, including its name, description, and category.
* **Policy Adherence Token (PAT)**: A token issued by a web service to an AI agent, encapsulating permissions, usage limits, and billing agreements.
* **AI Agent**: An application or service that uses intents to interact with web services.
* **Discovery Endpoint**: The API endpoint where AI agents can query for available intents.
* **Execution Endpoint**: The API endpoint where AI agents can execute intents.
* **Policy Endpoint**: The API endpoint where AI agents can request PATs from web services.

In the concept section of the [README](README.md), we dove into the Unified Intent Mediator (UIM) architecture based on these two proposed approaches:

1. **Man-in-the-Middle Approach (Centralized Repository)**
2. **Decentralized Approach (AI Agents Crawling Web Services)**

In this section, we will explore the API endpoints and components that enable these approaches and the underlying data structures that support them.

## 1. Introduction and Overview of Each Approach

### **1.1 Centralized Architecture (Man-in-the-Middle Approach)**

#### **1.1.1 Overview of Centralized Architecture**

The Centralized Architecture, also known as the Man-in-the-Middle Approach, serves as an intermediary system that manages all interactions between AI agents and web services. This model centralizes the registration, discovery, execution, and policy management of intents, offering a streamlined and unified platform that simplifies integrations and ensures consistency across all interactions. By acting as a central hub, this architecture provides a controlled environment where security, compliance, and scalability can be closely managed.

#### **1.1.2 Key Features of Centralized Architecture**

* **Unified Management**: A single repository controls the discovery and execution of intents, providing a consistent interface for AI agents and web services.
* **Streamlined Compliance**: Centralized management of Policy Adherence Tokens (PATs) ensures uniform application of security and billing rules, simplifying compliance for all parties involved.
* **Simplified Integration**: Web services register their intents once with the central system, making them easily discoverable by AI agents without the need for multiple, separate integrations.

#### **1.1.3 Workflow of Centralized Approach**

The centralized approach involves a structured workflow where web services and AI agents interact through a controlled, managed platform. Below is the typical process:

1. **Service Registration**:
   * **Intent Submission**: Web services submit their available intents, including descriptions, parameters, and execution details, to the central repository through the Service Management APIs.
   * **Intent Management**: Web services can update, modify, or remove their intents via the same management APIs, ensuring that the central repository always contains the latest, most accurate information.

2. **Intent Discovery**:
   * **Discovery APIs**: AI agents query the central repository’s Discovery APIs to search for available intents based on their needs. The central system handles all requests and responses, reducing the need for AI agents to interact directly with each individual web service.
   * **Standardized Output**: The discovery results are presented in a standardized format, making it easy for AI agents to understand and act on the available intents.

3. **Policy Adherence and Security**:
   * **Centralized PAT Management**: The central system issues PATs to AI agents after verifying compliance with the service’s policies. These tokens encapsulate permissions, usage limits, and billing agreements, ensuring that only authorized interactions occur.
   * **Unified Compliance Framework**: This centralized PAT management simplifies compliance by applying consistent security protocols across all interactions, reducing the burden on individual web services.

4. **Execution of Intents**:
   * **Execution APIs**: Once an intent is discovered, the AI agent uses the Execution APIs provided by the central repository to perform the desired actions. The central system coordinates the request, forwards it to the appropriate web service, and manages the execution flow.
   * **Monitoring and Logging**: The central system monitors all executed intents, maintaining logs for auditing, performance analysis, and troubleshooting.

5. **Error Handling and Adaptation**:
   * **Centralized Error Management**: The central system provides standardized error codes and recovery protocols, ensuring that AI agents can handle failures consistently and efficiently.
   * **Fallback and Retries**: If an intent fails to execute, the central system can offer alternative intents or suggest retries, enhancing the overall resilience of the interaction.

#### **1.1.4 Integration of Core Components in Centralized Architecture**

1. **Central Repository**:
   * **Purpose**: Acts as the main hub for all intent data, storing information from multiple web services in a single, accessible location. This repository ensures that AI agents have a streamlined path to discovering and executing intents.
   * **Implementation**: Web services register their intents through APIs, which automatically update the central repository. The repository maintains a comprehensive index of all available actions, categorized and searchable for ease of use.

2. **Service Management APIs**:
   * **Purpose**: These APIs facilitate the registration, updating, and removal of intents by web services. They ensure that the central repository always contains current data, providing a reliable resource for AI agents.
   * **Implementation**: Web services interact with these APIs to manage their intents, including setting parameters, defining execution rules, and specifying compliance requirements.

3. **Discovery and Execution APIs**:
   * **Purpose**: These APIs enable AI agents to find available intents and perform actions based on the information in the central repository. They standardize the interaction process, making it easy for AI agents to access a wide range of services through a single interface.
   * **Implementation**: AI agents query the Discovery API to search for intents and use the Execution API to initiate actions. The central system manages these interactions, ensuring they adhere to service-specific rules and security protocols.

4. **Centralized PAT Management**:
   * **Purpose**: The centralized PAT system manages the issuance, validation, and enforcement of Policy Adherence Tokens, ensuring secure and compliant interactions between AI agents and web services.
   * **Implementation**: The central repository generates PATs based on predefined service agreements, automatically enforcing policies during intent execution. This approach simplifies security management and provides a uniform framework for all transactions.

#### **1.1.5 Use Cases, Trade-offs, and Best Practices**

**Use Cases**:

* **Financial Services**: Ideal for industries requiring strict compliance and security, such as banking, where a unified approach simplifies oversight and reduces risks.
* **E-commerce Platforms**: Provides a standardized method for product searches, inventory management, and automated transactions, enhancing the efficiency of AI-driven interactions.
* **Customer Service Automation**: Streamlines the integration of multiple support services, allowing AI agents to access a broad range of helpdesk intents from a single point of contact.

**Trade-offs**:

* **Single Point of Failure**: If the central repository encounters issues, all interactions are affected, posing a risk to system reliability.
* **Scalability Concerns**: As the number of web services and AI agents grows, the central system may struggle to manage high volumes of requests efficiently.
* **Limited Autonomy**: Web services must adhere to the central repository’s rules and policies, limiting their autonomy and control over interactions.
* **Higher Onboarding Complexity for Web Services**: Web services must integrate with the central repository, which may require additional development and maintenance resources.
* **Data Privacy**: Centralized storage of intent data can raise concerns about data ownership, security, and privacy, especially in industries dealing with sensitive information.

**Best Practices**:

* **Implement Redundancy and Load Balancing**: To mitigate the risk of downtime, incorporate failover mechanisms and distribute workloads across multiple nodes.
* **Regular Security Audits**: Conduct periodic security reviews of the PAT management system to ensure that compliance and access controls remain robust.
* **Optimize API Performance**: Continuously monitor and optimize the performance of Discovery and Execution APIs to handle high traffic and ensure smooth interactions.

### **1.2 Decentralized Architecture (Direct Crawling by AI Agents)**

#### **1.2.1 Overview of Decentralized Architecture**

The Decentralized Architecture empowers AI agents to autonomously discover, interact with, and execute actions on web services without relying on a centralized intermediary. Each web service independently manages its own intents, publishing relevant information through DNS TXT records and `agents.json` files. This model allows web services to maintain full control over their data, compliance policies, and access protocols, while AI agents dynamically gather and utilize these intents in real time.

#### **1.2.2 Key Features of Decentralized Architecture**

* **Direct Interaction**: AI agents interact directly with web services, discovering and executing intents without the need for a central repository.
* **Scalability and Resilience**: By distributing the workload across individual web services, the architecture naturally scales to accommodate large numbers of interactions, reducing the risk of a single point of failure.
* **Privacy and Autonomy**: Web services retain control over their data and interaction policies, enhancing privacy and allowing for more customized interactions.
  
#### **1.2.3 Workflow of Decentralized Approach**

The decentralized approach follows a distinct workflow where AI agents independently discover and execute intents. Below is the typical process:

1. **Crawling and Discovery**:
   * **DNS TXT Records and `agents.json`**: Each web service publishes information about its available intents, discovery endpoints, and policy adherence requirements using DNS TXT records and `agents.json` files.
   * **AI Agent Crawling**: AI agents autonomously crawl these records to identify discovery endpoints and other relevant details. This crawling process is ongoing and dynamic, enabling agents to always have up-to-date information about available intents.

2. **Intent Retrieval**:
   * **Querying Discovery APIs**: Once the AI agent has identified a discovery endpoint from the `agents.json` file, it queries the endpoint to retrieve the list of available intents. This query can specify filters or keywords to refine the search based on the user’s needs.
   * **Parameter Collection**: The AI agent collects information about each intent, including required parameters, expected responses, rate limits, and any associated costs.

3. **Policy Adherence and Security**:
   * **Decentralized PAT Management**: Each web service manages its own Policy Adherence Tokens (PATs), which are issued to AI agents based on their compliance with specified policies. This step ensures that only authorized agents can execute intents, maintaining a secure interaction environment.
   * **Token Request**: AI agents must request a PAT from the web service’s policy endpoint, specifying the intents they intend to use and adhering to the service’s access rules.

4. **Execution of Intents**:
   * **Direct Execution**: With the required PAT and intent information, AI agents send execution requests directly to the web service’s endpoint. The requests include all necessary parameters and security tokens.
   * **Response Handling**: The web service processes the request, validates the PAT, and returns the desired results or actions. AI agents then parse and present the results to the end-user.

5. **Error Handling and Adaptation**:
   * **Dynamic Adaptation**: If an intent is unavailable or a service denies a request, AI agents can dynamically adapt by querying other available services or adjusting their parameters. This flexibility enhances the resilience and effectiveness of AI agents operating in decentralized environments.

#### **1.2.4 Integration of Core Components in Decentralized Architecture**

1. **DNS TXT Records and `agents.json` Files**:
   * **Purpose**: These files serve as self-publishing mechanisms for web services to expose information about their intents, discovery endpoints, security protocols, and rate limits.
   * **Implementation**: Web services include specific DNS TXT records that link to the `agents.json` file. This file contains structured details on available intents and the rules for interacting with the service.

2. **Intent Discovery APIs**:
   * **Purpose**: These APIs are hosted by individual web services and provide AI agents with a way to query and retrieve intent data. Each service can customize its discovery API, offering intents tailored to its capabilities and user needs.
   * **Implementation**: AI agents access these APIs by reading URLs specified in the `agents.json` file, allowing them to perform searches for specific intents or actions.

3. **Decentralized PAT Management**:
   * **Purpose**: Decentralized PATs ensure secure, compliant access to web service intents. Each service issues its own tokens based on predefined policies, giving them control over who can execute their intents.
   * **Implementation**: AI agents must request PATs by contacting the policy endpoint outlined in the `agents.json` file, providing details about their intended actions and complying with the service’s specific requirements.

#### **1.2.5 Use Cases, Trade-offs, and Best Practices**

**Use Cases**:

* **Privacy and Security**: Use cases where maintaining control over data and interactions is critical, such as healthcare, finance, and personal assistants.
* **IoT and Smart Environments**: Ideal for managing numerous devices and services in a distributed network where autonomy and direct communication are essential.
* **Decentralized Finance (DeFi)**: Facilitates secure, direct interaction with financial services, maintaining privacy and compliance without relying on centralized intermediaries.

**Trade-offs**:

* **Consistency Challenges**: Each service manages its own rules and data, which can lead to inconsistencies in how intents are defined and executed.
* **Higher Onboarding Complexity for AI Agents**: Requires agents to handle diverse sets of discovery and policy adherence rules, increasing the complexity of initial setup and maintenance.

**Best Practices**:

* **Standardize `agents.json` Formats**: Encouraging uniformity in how web services define their intents and policies can reduce onboarding friction for AI agents.
* **Regular Crawling and Updating**: AI agents should frequently crawl services to maintain up-to-date knowledge of available intents and changes to policies or endpoints.
* **Automated Error Recovery**: Implement robust error-handling mechanisms to allow AI agents to adapt dynamically when encountering unavailable or restricted intents.

### **1.3 Hybrid Approach: Centralized Discovery with Decentralized Execution and PAT Issuance**

This hybrid approach combines centralized discovery with decentralized execution and decentralized Policy Adherence Token (PAT) issuance, drawing parallels with how search engines like Google operate. In this model, the centralized discovery system provides AI agents with a standardized and comprehensive way to discover available intents across multiple web services, similar to how search engines crawl and index web content using `robots.txt`. However, the actual execution of intents is handled directly between the AI agents and web services, maintaining the autonomy and scalability benefits of decentralized interactions.

#### **1.3.1 Concept Overview**

* **Centralized Discovery**: A central system aggregates intent information from multiple web services. Web services publish their intents using `agents.json` files or register through service management endpoints, making these intents discoverable to AI agents through a unified discovery interface.
* **Decentralized Execution**: After discovering intents, AI agents execute actions directly by interacting with the specific web service’s execution endpoints. This decentralized execution maintains the service’s control over how intents are performed, allowing for customized security and performance management.
* **Decentralized PAT Issuance**: Each web service independently manages its own PAT issuance, ensuring that security, compliance, and billing policies are locally enforced. This allows web services to define and enforce their own rules, even as they participate in a broader, centrally-discovered ecosystem.

#### **1.3.2 Similarities to Search Engines (e.g., Google)**

* **Crawling and Indexing**: Similar to how search engines like Google use `robots.txt` to discover and index web content, AI agents rely on `agents.json` files or centralized service management endpoints to find and index available intents. The centralized discovery system acts like Google’s search index, providing a comprehensive and up-to-date view of available actions across multiple services.
  
* **Relevant Responses**: When users perform a search, search engines query their index to provide the most relevant results. In this hybrid approach, AI agents use the centralized discovery to find relevant intents that align with user requests. The centralized system does not execute these intents but instead acts as a guide to direct AI agents toward the appropriate service endpoints.

* **Direct Interaction for Execution**: While search engines direct users to relevant web pages, AI agents in this hybrid model directly interact with the web service’s execution endpoint, bypassing the centralized discovery system. This decentralized execution maintains the autonomy and control of each web service, allowing them to handle execution specifics such as rate limits, data processing, and compliance directly.

#### **1.3.3 Detailed Workflow**

1. **Centralized Discovery**:
   * **Intent Publishing**: Web services publish their available intents via `agents.json` files hosted on their domains or register them through centralized service management APIs. This data is aggregated into a centralized discovery index that AI agents can query.
   * **Crawling and Indexing**: The central discovery system periodically crawls web services, reading `agents.json` files and indexing the intents available. This process is similar to how search engines continually crawl and update their indexes based on new or updated content.
   * **Querying Discovery**: AI agents query the central discovery system to find intents relevant to the user’s request. This interaction is streamlined, with the centralized system providing a consolidated view of available actions.

2. **Decentralized Execution**:
   * **Direct Service Interaction**: Once an AI agent identifies an appropriate intent, it bypasses the central system and sends execution requests directly to the web service’s execution endpoint. This preserves the direct relationship between the AI agent and the service, allowing for real-time interaction and minimizing centralized bottlenecks.
   * **Localized Execution Rules**: Each web service independently manages its execution rules, including parameter validation, rate limits, and error handling. This autonomy allows web services to optimize their operations based on specific needs without needing to conform to a centralized execution standard.

3. **Decentralized PAT Issuance**:
   * **Independent PAT Management**: Web services independently issue and validate PATs, which are required for AI agents to execute intents. The PAT encapsulates permissions, usage constraints, and billing terms tailored to each service’s policies.
   * **Compliance and Security**: The decentralized PAT management system ensures that only authorized AI agents can execute intents. Each web service defines its security standards, ensuring that compliance and data privacy are enforced locally.

#### **1.3.4 Advantages of This Hybrid Approach**

* **Enhanced Discovery with Local Execution Control**: Centralized discovery simplifies the search process for AI agents, making it easier to find relevant intents across multiple services. At the same time, decentralized execution preserves the autonomy of web services, allowing them to manage how their intents are used.
  
* **Scalable and Resilient**: By decoupling discovery from execution, this approach reduces the processing load on the central system and distributes it across web services, enhancing overall scalability and resilience.

* **Flexible Compliance**: Decentralized PAT issuance allows each web service to enforce its own compliance and security protocols, adapting to specific regulatory requirements and minimizing centralized security risks.

* **Reduced Latency**: Direct execution between AI agents and web services minimizes latency compared to a fully centralized execution model, improving response times and user experience.

#### **1.3.5 Disadvantages and Challenges**

* **Coordination Complexity**: Maintaining consistency between the centralized discovery index and the decentralized execution points can be challenging. Frequent updates and synchronization mechanisms are needed to ensure that the discovery system reflects the latest available intents.

* **Diverse Compliance Requirements**: AI agents must navigate varying compliance rules across different services due to decentralized PAT issuance, which can complicate implementation and require sophisticated token management strategies.

* **Potential Data Silos**: Since each service manages its own execution and PAT system, data generated from interactions can become siloed, making it harder to gather comprehensive analytics across the ecosystem.
* **Increased Onboarding Complexity for Web Services**: Web services must manage both centralized discovery and decentralized execution, which can increase the complexity of onboarding and maintenance compared to a fully centralized model.

This hybrid approach leverages the best of both worlds, using centralized discovery to simplify intent identification while maintaining decentralized execution and compliance to empower web services. It mirrors the efficiency of search engine models while providing the flexibility needed for secure and scalable AI-agent interactions.

Based on the previous feedback regarding the structure and logical flow of the document, the **Appendix: Core Component Descriptions** section needs to be reordered to reflect the real-world sequence of how AI agents interact with web services. Here’s the revised approach that aligns with the natural usage flow: starting with discovery and execution, followed by service management, and finally detailing intent management. This reordering provides a clear narrative from the AI agent’s perspective, improving coherence and usability.

## 2. Core Components of the UIM Protocol

This section provides a comprehensive description of the core components of the UIM protocol, explaining their purpose, implementation, variations between approaches, relevant API endpoints, and the underlying data structures that support them. The components are presented in a sequence that mirrors the typical interaction flow of AI agents with web services: discovery and execution, followed by service management, and intent management.

### 2.1 Discovery and Execution Endpoints

#### 2.1.1 Purpose

Discovery and execution endpoints form the first point of interaction for AI agents, enabling them to identify and perform actions (intents) offered by web services. These endpoints streamline the process of discovering what services are available and executing those services in a secure and compliant manner.

#### 2.1.2 Implementation  

* **Centralized Context**: The discovery endpoint is centrally managed, offering a unified interface where AI agents can search for intents across multiple services. Execution is handled by forwarding requests to the appropriate web service.
* **Decentralized Context**: Each web service independently hosts its own discovery and execution endpoints. AI agents query these endpoints directly based on data found in `agents.json` files or DNS TXT records.
* **Hybrid Context**: The discovery endpoint is centrally managed, but execution is handled by AI-agents directly interacting with web services. This approach combines the benefits of both centralized and decentralized contexts.

#### 2.1.3 Unique Intent Identifier (UID) Format

In order to ensure that AI agents can effectively call intents from different service providers, even if the intents are similar, it is important to establish a robust and standardized method for identifying each intent across various service providers. The UIM protocol defines a Unique Intent Format for this purpose. The UID is a string that uniquely identifies an intent, consisting of the following components:

* **namespace**: Use namespaces to distinguish between different service providers. The namespace is typically the domain or a unique identifier for the service provider.
* **intent name**: Use intent names to distinguish between different intents offered by the same service provider. The intent name should be descriptive and unique within the namespace.
* **version number**: To accommodate changes and updates to intents, the UID format includes a version number. The version number is appended to the UID, separated by a colon. This allows for backward compatibility and efficient management of updates.

The UID format is as follows: `namespace:intentName:version`

**Examples**:

* `ecommercePlatform:searchProducts:v1`
* `weather.com:getForecast:v2`

#### 2.1.4 Intent Metadata

Intent metadata provides additional information about the intent, such as its purpose, input parameters and their types, output parameters and their types, and the execution endpoint. This metadata is used by AI agents to understand how to interact with the intent and make informed decisions about its suitability for a given task. The UIM protocol defines a standard format for intent metadata, which is used by both centralized and decentralized discovery endpoints. The metadata is typically provided in JSON format.

The following fields are included in the metadata:

* **intent_uid**: The unique identifier for the intent, following the UID format.
* **description**: A brief description of the intent's purpose and functionality.
* **input_parameters**: A list of input parameters required by the intent, including their names, types, and descriptions. These parameters are used by AI agents to construct the execution request.
* **output_parameters**: A list of output parameters returned by the intent, including their names, types, and descriptions. These parameters are used by AI agents to interpret the execution response.
* **endpoint**: The URL of the execution endpoint for the intent. This endpoint is used by AI agents to send execution requests.
* **tags**: A list of tags that describe the intent, making it easier to search and categorize. These tags are used by AI agents to filter and identify relevant intents.
* **service_name**: The name of the service that provides the intent.
* **service_description**: A brief description of the service that provides the intent. This field is optional.
* **service_url**: The URL of the service that provides the intent. This field is optional.
* **service_logo_url**: The URL of the service's logo. This field is optional.
* **service_terms_of_service_url**: The URL of the service's terms of service. This field is optional.
* **service_privacy_policy_url**: The URL of the service's privacy policy. This field is optional.

#### 2.1.5 Intent Discovery

* **Endpoint**: /api/intents/search  
* **Method**: GET  
* **Description**: Searches for available intents based on given criteria.  
* **Parameters**:  
  * query (string, optional): The natural language query or search term.  
  * service_name (string, optional): The name of a service.  
  * intent_name (string, optional): The name of an intent.  
  * uid (string, optional): The unique identifier of an intent.  
  * namespace (string, optional): The namespace of a service.  
  * description (string, optional): The description of an intent.  
  * tags (string, optional): A comma separated list of tags.

**Example Request:**

```http
GET /api/intents/search?intent_name=SearchProducts
```

**Example Response:**

```json
{
  "intents": [
    {
      "service_name": "E-commerce Platform",
      "intent_name": "SearchProducts",
      "intent_uid": "ecommerce.com:searchProducts:v1",
      "description": "Search for products based on given criteria",
      "input_parameters": [
        {"name": "query", "type": "string", "required": true},
        {"name": "category", "type": "string", "required": false},
        {"name": "price_range", "type": "string", "required": false},
        {"name": "sort_by", "type": "string", "required": false}
      ],
      "output_parameters": [
        {"name": "products", "type": "array", "required": true},
        {"name": "total_results", "type": "integer", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/products/search",
      "tags": ["e-commerce", "search", "products"]
    }
  ]
}
```

The discovery mechanisms allow AI agents to search for and retrieve intent details based on the UID, namespace, or other metadata.

**Examples**:  
**Search by UID**: /api/intents/search?uid=ecommercePlatform:searchProducts:v1  
**Search by Namespace**: /api/intents/search?namespace=ecommercePlatform  
**Search by Description**: /api/intents/search?description=search products

#### 2.1.6 Execute Intent

* **Endpoint**: /api/intents/execute  
* **Method**: POST  
* **Description**: Executes an intent based on the provided input parameters.
* **Parameters**:  
  * intent_uid (string, required): The identifier for the intent  
  * parameters (object, required): The parameters required to execute the intent.

**Example Request:**

```json
POST /api/intents/execute
{
  "intent_uid": "ecommercePlatform:searchProducts:v1",
  "parameters": {
    "query": "laptops",
    "category": "electronics",
    "price_range": "1000-2000",
    "sort_by": "popularity"
  }
}
```

**Example Response:**

```json
{
  "total_results": 1,
  "products": [
    {
      "product_id": "123",
      "name": "Gaming Laptop",
      "price": 1500,
      "category": "electronics"
    }
  ]
}
```

### 2.3 Discovery Through DNS TXT Records and agents.json Files

1. **DNS TXT Records**:
   * **Purpose**: DNS TXT records act as a preliminary layer of discovery, allowing AI agents to quickly identify which services are available and where to find detailed service descriptions or discovery endpoints.
   * **Functionality**: These records provide a lightweight mechanism to point AI agents to `agents.json` files or directly to discovery APIs. They integrate seamlessly with existing DNS infrastructure, making them an efficient and scalable way to manage high-level discovery information.
   * **Benefits**:
     * **Quick Service Identification**: Enables fast, infrastructure-level recognition of available services without requiring direct crawling of each domain.
     * **Scalability**: Scales well across large numbers of services, leveraging the robust DNS architecture already in place.

2. **`agents.json` Files**:
   * **Purpose**: These files provide a structured and detailed format for web services to publish their capabilities, discovery endpoints, compliance requirements, and execution rules.
   * **Functionality**: `agents.json` files are directly accessible by AI agents and contain comprehensive service information, such as available intents, rate limits, and specific API details.
   * **Benefits**:
     * **Rich Data Presentation**: Offers detailed descriptions of intents and operational rules that go beyond the capabilities of DNS TXT records.
     * **Flexibility and Control**: Allows services to independently update their discovery information without altering DNS configurations.

#### 2.3.1 Using Both Methods for Comprehensive Discovery

By combining both DNS TXT records and `agents.json` files, the UIM protocol can provide a comprehensive and efficient discovery process:

* **Efficient Layered Discovery**: DNS TXT records provide the initial point of contact, guiding AI agents to the right services without heavy overhead. Once identified, agents can then retrieve detailed service information from `agents.json` files.
* **Enhanced Redundancy and Flexibility**: This dual approach ensures that even if one layer is temporarily inaccessible (e.g., due to DNS issues), the other can still facilitate discovery.

#### 2.3.2 Implications of Omitting DNS TXT Records

**1. Simplification of Implementation**:  
Omitting DNS TXT records can simplify implementation, especially for smaller services or those that prefer to avoid the complexities of DNS management. By relying solely on `agents.json` files, services can directly control their discovery process without needing to configure or maintain DNS records.

**2. Potential Losses**:

* **Slower Discovery Process**: Without DNS TXT records, AI agents must directly crawl domains to locate `agents.json` files, which can be slower and less efficient, especially if services are not consistently structured or if file locations are non-standard.
* **Scalability Limitations**: DNS TXT records allow for a scalable, distributed approach to service discovery. Without them, the protocol relies entirely on HTTP crawling, which may not scale as efficiently for large ecosystems.
* **Increased Crawl Load**: Directly accessing `agents.json` files without the initial filtering step provided by DNS TXT records can increase the number of requests made by AI agents, potentially leading to higher server loads and slower performance.

**3. Impact on Reliability and Fault Tolerance**:

* **Reduced Fault Tolerance**: DNS TXT records provide an additional layer of fault tolerance by decentralizing the initial discovery step. If this layer is removed, the protocol’s reliance on web server availability increases, potentially reducing overall reliability during network or service disruptions.

**4. Compromised Usability for AI Agents**:

* **Higher Latency**: Direct crawling may lead to increased latency as agents must independently discover `agents.json` files without the initial guidance that DNS provides. This can slow down the overall process of intent discovery and execution.

For a comprehensive and efficient discovery process, using both DNS TXT records and `agents.json` files is recommended. This layered approach optimizes initial service identification and provides rich, detailed service descriptions in `agents.json` files. Omitting DNS TXT records can simplify implementations but at the cost of slower, less scalable discovery with increased load on service endpoints and reduced fault tolerance.

#### 2.3.3 Purpose

DNS TXT records provide fast, infrastructure-level discovery, guiding AI agents to the key URLs they need to begin more detailed exploration, while `agents.json` files provide a standardized, human-readable format for web services to publish intent information, discovery endpoints, execution rules, and compliance protocols. These mechanisms are critical components in the decentralized architecture, offering a flexible and scalable way for services to expose their capabilities.

#### 2.3.4 Implementation

* **Decentralized Context**: Web services create and maintain DNS TXT records that specify the location of their `agents.json` files. This enables AI agents to discover the service’s available intents dynamically, without a central intermediary. Each web service hosts an `agents.json` file at a known location (typically the root of their domain), detailing all available intents and necessary compliance information. AI agents crawl these files to gather relevant data about how to interact with the service.
* **Centralized Context**: Typically not used in a centralized setup, as the discovery is managed by the central repository directly.
* **Hybrid Context**: While discovery is centralized, DNS TXT records and `agents.json` files still play a role in helping AI agents quickly identify services that publish their intents, which is then crawled and indexed by a centralized discovery system. This approach maintains the dynamic nature of decentralized discovery while integrating the streamlined search capabilities of centralized models.

#### 2.3.5 DNS TXT Record Fields

1. **Location of `agents.json` File**
   * **Field Name**: `uim-agents-file`
   * **Description**: Specifies the URL of the `agents.json` file, which contains detailed information about the web service’s capabilities, compliance requirements, and endpoints.
   * **Rationale**: Directs AI agents to the `agents.json` file, which holds the structured and detailed data needed for in-depth interaction with the service.
   * **Example**:  
     `uim-agents-file=https://example.com/agents.json`

2. **API Discovery Endpoint**
   * **Field Name**: `uim-api-discovery`
   * **Description**: Provides a direct URL to the API discovery endpoint, where AI agents can access the web service’s intents catalog.
   * **Rationale**: Essential for immediate discovery of service intents and their associated details, this endpoint serves as the gateway for interaction initiation.
   * **Example**:  
     `uim-api-discovery=https://api.example.com/intents/search`

3. **ODRL Policy File**
   * **Field Name**: `uim-policy-file`
   * **Description**: URL pointing to the service’s policy or compliance endpoint where ODRL policies or other compliance information can be accessed.
   * **Rationale**: Helps AI agents quickly locate compliance requirements, enabling early validation of operational rules.
   * **Example**:  
     `uim-policy-file=https://example.com/uim-policy.json`

#### 2.3.6 `agents.json` File Specification

Here's a detailed description and documentation of each field in the `agents.json` JSON structure, outlining the purpose and intended use within the UIM protocol.

**`service-info`**:
This section provides basic metadata about the service, including its name, status, and links to relevant resources.

* **`name`**:
  * **Description**: The name of the service providing the intents.
  * **Example**: `"fakerealestate.com"`
  
* **`description`**:
  * **Description**: A brief description of the service and what it offers.
  * **Example**: `"A fictional service providing property listings and real estate data."`

* **`service_url`**:
  * **Description**: The main URL of the service, providing a direct link to the homepage or central access point.
  * **Example**: `"https://fakerealestate.com"`

* **`service_logo_url`**:
  * **Description**: URL of the service's logo, which can be used for display purposes by AI agents or third-party applications.
  * **Example**: `"https://fakerealestate.com/logo.png"`

* **`service_terms_of_service_url`**:
  * **Description**: Link to the terms of service page, outlining the legal use and conditions of the service.
  * **Example**: `"https://fakerealestate.com/terms"`

* **`service_privacy_policy_url`**:
  * **Description**: URL of the service’s privacy policy, detailing how user data is collected, used, and protected.
  * **Example**: `"https://fakerealestate.com/privacy"`

**`intents`**:
This array contains detailed descriptions of each intent provided by the service, including execution parameters and endpoint information.

* **`intent_uid`**:
  * **Description**: A unique identifier for the intent, formatted as `service:intent_name:version`, ensuring each intent can be uniquely referenced.
  * **Example**: `"fakerealestate.com:searchProperty:v1"`

* **`intent_name`**:
  * **Description**: The name of the intent, representing its core function.
  * **Example**: `"SearchProperty"`

* **`description`**:
  * **Description**: A brief explanation of what the intent does and its purpose.
  * **Example**: `"Searches properties based on location, price range, and property type."`

* **`input_parameters`**:
  * **Description**: A list of parameters required for the intent to execute, detailing each parameter's name, type, whether it is required, and a description.
  * **Example**:

    ```json
    [
      {"name": "location", "type": "string", "required": true, "description": "Location to search properties in."}
    ]
    ```

* **`output_parameters`**:
  * **Description**: A list of output parameters returned by the intent, including their names, types, and descriptions to help AI agents interpret the response.
  * **Example**:

    ```json
    [
      {"name": "properties", "type": "array", "description": "List of properties matching the search criteria."}
    ]
    ```

* **`endpoint`**:
  * **Description**: The URL of the execution endpoint for the intent, where AI agents send requests to execute the intent.
  * **Example**: `"https://fakerealestate.com/api/execute/SearchProperty"`

* **`tags`**:
  * **Description**: A list of tags that describe the intent, aiding in search and categorization.
  * **Example**: `["real estate", "search", "property"]`

* **`rate_limit`**:
  * **Description**: The maximum number of requests allowed per time unit, which helps AI agents manage their interactions with the service.
  * **Example**: `"1000/hour"`

* **`price`**:
  * **Description**: The cost associated with executing the intent, providing transparency on usage fees.
  * **Example**: `"0.01 USD"`

**`uim-public-key`**:

* **Description**: The public key used by the service for signing and verifying payloads, ensuring secure interactions.
* **Example**: `"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA..."`

**`uim-policy-file`**:

* **Description**: URL to a file containing the service's policy rules or ODRL-compliant policies, providing detailed compliance information.
* **Example**: `"https://fakerealestate.com/uim-policy.json"`

**`uim-api-discovery`**:

* **Description**: The URL for the discovery API, allowing AI agents to query and retrieve available intents.
* **Example**: `"https://fakerealestate.com/uim/intents/search"`

**`uim-compliance`**:
This section outlines the compliance standards and regional regulations the service adheres to.

* **`standards`**:
  * **Description**: A list of recognized standards the service complies with, such as data security or privacy standards.
  * **Example**: `["ISO27001", "GDPR"]`

* **`regional-compliance`**:
  * **Description**: Specific compliance standards applicable to certain regions, allowing AI agents to assess regional regulatory requirements.
  * **Example**:

    ```json
    {
      "EU": "GDPR",
      "US-CA": "CCPA"
    }
    ```

* **`notes`**:
  * **Description**: Additional notes on compliance practices, such as data encryption methods or security protocols.
  * **Example**: `"Data is encrypted in transit and at rest."`

**`uim-license`**

* **Description**: The license under which the service operates, providing information on the terms of use and permissions. Inspired by Creative Commons. *NOTE: May be obsolete if a policy endpoint exists and covers the license.*
* **Example**: `"CC-BY-NC-SA-4.0"`

#### 2.3.7 Example `agents.json` File

```json
{
  "service-info": {
    "name": "fakerealestate.com",
    "description": "A fictional service providing property listings and real estate data.",
    "service_url": "https://fakerealestate.com",
    "service_logo_url": "https://fakerealestate.com/logo.png",
    "service_terms_of_service_url": "https://fakerealestate.com/terms",
    "service_privacy_policy_url": "https://fakerealestate.com/privacy"
  },
  "intents": [
    {
      "intent_uid": "fakerealestate.com:searchProperty:v1",
      "intent_name": "SearchProperty",
      "description": "Searches properties based on location, price range, and property type.",
      "input_parameters": [
        {"name": "location", "type": "string", "required": true, "description": "Location to search properties in."},
        {"name": "min_price", "type": "integer", "required": false, "description": "Minimum price range."},
        {"name": "max_price", "type": "integer", "required": false, "description": "Maximum price range."},
        {"name": "property_type", "type": "string", "required": false, "description": "Type of property (e.g., apartment, house)."}
      ],
      "output_parameters": [
        {"name": "properties", "type": "array", "description": "List of properties matching the search criteria."},
        {"name": "total_results", "type": "integer", "description": "Total number of results found."}
      ],
      "endpoint": "https://fakerealestate.com/api/execute/SearchProperty",
      "tags": ["real estate", "search", "property"],
      "rate_limit": "1000/hour",
      "price": "0.01 USD"
    },
    {
      "intent_uid": "fakerealestate.com:getPropertyDetails:v1",
      "intent_name": "GetPropertyDetails",
      "description": "Fetches detailed information for a specific property based on property ID.",
      "input_parameters": [
        {"name": "property_id", "type": "string", "required": true, "description": "Unique identifier of the property."}
      ],
      "output_parameters": [
        {"name": "property_details", "type": "object", "description": "Detailed information about the property."}
      ],
      "endpoint": "https://fakerealestate.com/api/execute/GetPropertyDetails",
      "tags": ["real estate", "details", "property"],
      "rate_limit": "1000/hour",
      "price": "0.01 USD"
    }
  ],
  "uim-public-key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...",
  "uim-policy-file": "https://fakerealestate.com/uim-policy.json",
  "uim-api-discovery": "https://fakerealestate.com/uim/intents/search",
  "uim-compliance": {
    "standards": ["ISO27001", "GDPR"],
    "regional-compliance": {
      "EU": "GDPR",
      "US-CA": "CCPA"
    },
    "notes": "Data is encrypted in transit and at rest."
  },
  "uim-license": "CC-BY-NC-SA-4.0"
}
```

### 2.4 Benefits of Using ODRL and DNS for Efficient AI-Agent Interactions

By combining the robust policy framework provided by ODRL with the streamlined discovery mechanisms of DNS TXT records and agents.json files, the UIM protocol offers a powerful solution for managing AI-agent interactions with web services. This approach ensures clear, verifiable, and enforceable policies, enhances security and compliance, simplifies discovery and integration, and supports scalability and ease of implementation.

![benefits of ODRL](images/odrl-benefits.png)

#### 2.4.1 Benefits of Using the Open Digital Rights Language (ODRL) Information Model 2.2

**1. Standardization of Policies:**  
ODRL provides a standardized way to define permissions, prohibitions, and obligations. This standardization ensures that all policies are expressed in a consistent format, making it easier for AI agents to interpret and comply with them. This uniformity reduces the likelihood of misunderstandings or misconfigurations that could lead to non-compliance.

**2. Flexibility and Interoperability:**  
ODRL’s flexible framework allows it to be adapted to various use cases and requirements. It supports a wide range of policy expressions, from simple permissions to complex conditions and constraints. This flexibility ensures that the UIM protocol can accommodate diverse web services and AI agent interactions. Additionally, ODRL’s adherence to open standards promotes interoperability between different systems and platforms.

**3. Clear and Verifiable Terms:**  
By defining policies in ODRL, web services can provide clear, precise, and verifiable terms of service. This transparency helps build trust between AI agents and web services, as both parties have a clear understanding of their rights and obligations. Verifiable policies also facilitate auditing and compliance checks, ensuring that all interactions adhere to agreed-upon terms.

**4. Enhanced Security and Compliance:**  
ODRL allows the definition of detailed security and compliance requirements, such as rate limits, payment obligations, and data handling practices. By enforcing these requirements programmatically, web services can ensure that AI agents adhere to their policies, reducing the risk of abuse or non-compliance.

**5. Automated Enforcement:**  
ODRL policies can be enforced automatically by the UIM protocol. This automation reduces the administrative burden on web services, as they do not need to manually monitor and enforce compliance. Automated enforcement also ensures that policies are applied consistently and promptly.

![DNS TXT records and agents.json](images/dns-txt-and-agents-txt.png)

#### 2.4.2 Leveraging DNS TXT Records and agents.json for AI-Agent Interactions

**1. Simplified Discovery:**  
DNS TXT records and the agents.json file provide a straightforward method for AI agents to discover web service endpoints and retrieve necessary information. By querying these records, AI agents can easily find policy endpoints, API discovery endpoints, and authentication methods. This simplicity streamlines the initial setup process for AI agents.

**2. Centralized Information:**  
Using DNS TXT records and agents.json, web services can centralize all necessary information for AI agents. This centralized approach ensures that AI agents can quickly access all relevant details, such as rate limits, pricing, and public keys, in one place. Centralized information reduces the need for multiple queries and simplifies the interaction process.

**3. Enhanced Security:**  
DNS TXT records can include information about authentication protocols and public keys, enabling secure communication between AI agents and web services. By providing this information upfront, web services can ensure that AI agents use the correct authentication methods and encrypt sensitive data appropriately.

**4. Scalability:**  
The use of DNS TXT records and agents.json files scales well with the number of web services and AI agents. As more web services adopt this method, AI agents can easily discover and interact with new services without requiring significant changes to their implementation. This scalability supports the growth of the UIM protocol and the broader ecosystem of AI-agent interactions.

**5. Ease of Implementation:**  
Implementing DNS TXT records and agents.json files is straightforward and leverages existing internet infrastructure. Web services can easily publish these records, and AI agents can use standard DNS queries to retrieve them. This ease of implementation lowers the barrier to entry for web services and encourages widespread adoption.

### 2.5 Policy Adherence Token (PAT) Management

#### 2.5.1 Purpose

PATs are crucial for maintaining secure, compliant, and regulated interactions between AI agents and web services. They encapsulate permissions, usage constraints, compliance terms, and billing agreements, ensuring that every execution of an intent adheres to the service’s policies.

![key fields](images/policy-fields.png)

#### 2.5.2 Implementation

* **Centralized Context**: PAT issuance, validation, and management are centrally controlled by the repository. This centralized system verifies agent compliance before issuing tokens, streamlining policy enforcement across multiple services.
* **Decentralized Context**: Each web service independently handles its own PAT issuance and validation processes, allowing for tailored compliance and security measures specific to the service’s operational needs.
* **Hybrid Context**: PAT issuance is decentralized, with each service handling its own security and compliance checks. This approach ensures that each interaction adheres to service-specific rules, even though discovery remains centralized, offering both control and efficiency.

#### 2.5.3 Leveraging ODRL for Managing Policies

The [Open Digital Rights Language (ODRL) Information Model 2.2](https://www.w3.org/TR/odrl-model/) provides a robust framework for defining and managing permissions, prohibitions, and obligations. Integrating ODRL with the UIM protocol allows for a standardized and transparent approach to negotiating and enforcing agreements between AI agents and web services. This integration enhances the security, compliance, and efficiency of interactions. Additionally, leveraging DNS TXT records and an agents.json file provides a streamlined method for AI agents to discover API endpoints, authenticate, adhere to rate limits, understand pricing, and verify agreements.

![ODRL policy flow](images/policy-flow.png)

##### 2.5.3.1 Key Concepts

* **Policy**: Represents the agreement between AI agents and web services, detailing permissions, prohibitions, and obligations.  
* **Permission**: Specifies allowed actions for AI agents.  
* **Prohibition**: Specifies actions that AI agents are not allowed to perform.  
* **Obligation**: Specifies actions that AI agents must perform under certain conditions.  
* **Asset**: The resource or service the policy applies to.  
* **Party**: The entities involved in the policy (e.g., AI agents and web services).

##### 2.5.3.2 Example ODRL Policy for UIM Integration

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "uid": "http://example.com/policy/12345",
  "type": "Set",
  "profile": "http://example.com/profile/odrl-uim",
  "permission": [
    {
      "target": "http://example.com/api/intents",
      "action": "execute",
      "constraint": [
        {
          "leftOperand": "http://example.com/vocab/rateLimit",
          "operator": "lte",
          "rightOperand": 1000,
          "unit": "http://example.com/vocab/hour"
        }
      ],
      "duty": [
        {
          "action": "pay",
          "target": "http://example.com/vocab/intentPrice",
          "amount": 0.01,
          "unit": "http://example.com/vocab/USD"
        }
      ]
    }
  ],
  "prohibition": [
    {
      "target": "http://example.com/api/intents",
      "action": "exceedRateLimit"
    }
  ],
  "obligation": [
    {
      "action": "signPayload",
      "assignee": "http://example.com/ai-agent/1",
      "target": "http://example.com/vocab/payload",
      "constraint": [
        {
          "leftOperand": "http://example.com/vocab/publicKey",
          "operator": "use",
          "rightOperand": "MIIBIjANBgkqh..."
        }
      ]
    }
  ],
  "party": [
    {
      "function": "assigner",
      "identifier": "http://example.com/web-service/1"
    },
    {
      "function": "assignee",
      "identifier": "http://example.com/ai-agent/1"
    }
  ],
  "asset": "http://example.com/api/intents"
}
```

##### 2.5.3.3 Policy Fields and Definitions

* **uid**: Unique identifier for the policy.  
* **type**: Type of policy (Set).  
* **profile**: Profile defining the context of the policy (specific to UIM integration).  
* **permission**: Allowed actions for AI agents, such as executing intents within specified constraints (rate limits, payment).  
* **prohibition**: Actions AI agents are not allowed to perform, such as exceeding rate limits.  
* **obligation**: Actions AI agents must perform, such as signing payloads using the specified public key.  
* **party**: Entities involved in the policy (assigner and assignee).  
* **asset**: The resource or service the policy applies to (intents API).

##### 2.5.4 Policy Adherence Token (PAT) System

To streamline the process of AI-Agent policy adherence while maintaining security and flexibility, we introduce a **Policy Adherence Token (PAT)** system. This system offers a balanced approach to ensuring AI-Agent compliance with web service policies. By encapsulating the agreed policies and permissions in a digitally signed token, it simplifies the verification process while maintaining strong security and flexibility.

##### 2.5.4.1 Steps to Implement PAT

* Web services issue a Policy Adherence Token (PAT) to AI-Agents upon successful agreement to policies.  
* The PAT encapsulates the agreed policies, permissions, and obligations in a digitally signed token.  
* AI-Agents include the PAT in their payloads, simplifying verification and enforcement.

![PAT implementation](images/pat-implementation.png)

1. **Policy Retrieval and Agreement**:  
   1. AI-Agent retrieves the ODRL policy from the specified endpoint.  
   2. AI-Agent digitally signs the policy using its private key and sends it to the web service alongside it's public key to request a PAT.
2. **PAT Issuance**:  
   1. Web service verifies the AI-Agent’s signature and agreement.  
   2. Web service issues a PAT, which includes the agreed policy details, permissions, and a validity period.  
   3. PAT is digitally signed by the web service to ensure integrity and authenticity.  
3. **Using PAT in Requests**:  
   1. AI-Agent includes the PAT in the header of each request.  
   2. Web service verifies the PAT’s signature and validity before processing the request.

##### 2.5.4.2 Example PAT Structure

```json
{
  "pat": {
    "uid": "pat-12345",
    "issued_to": "ai-agent-1",
    "issued_by": "web-service-1",
    "policy_reference": "http://example.com/policy/12345",
    "permissions": [
      "execute:intent/searchProducts",
      "rate_limit:1000/hour"
    ],
    "obligations": [
      "pay:0.01 USD per intent"
    ],
    "valid_from": "2024-01-01T00:00:00Z",
    "valid_to": "2024-12-31T23:59:59Z"
  },
  "signature": "Base64-encoded-digital-signature"
}
```

##### 2.5.4.3 Example Request with PAT

```http
POST /api/intents/execute HTTP/1.1
Host: api.ecommerce.com
Authorization: Bearer PAT-12345
Content-Type: application/json
```

##### 2.5.4.4 Verification Process

1. Web service extracts the PAT from the request header.  
2. Web service verifies the PAT’s signature and validity.  
3. Web service checks if the PAT permissions match the requested action.  
4. If valid, the web service processes the request; otherwise, it rejects it.

#### 2.5.5 Pros and Cons of PAT System

**Pros**:

* Simplifies the verification process with a single token.  
* Reduces the need for frequent policy retrieval and agreement.  
* Maintains strong security with digital signatures.  
* Flexibility in managing permissions and obligations through the PAT.

**Cons**:

* Initial complexity in setting up the PAT issuance and verification process.  
* Requires secure storage and management of PATs.  
* Tokens need to be periodically renewed, adding some operational overhead.

### 2.5.6 Enhanced PAT System with Billing Information

Incorporating billing information into the PAT during the agreement and issuance phase is a powerful enhancement to the UIM protocol. It simplifies the transaction process, enables automated billing, and ensures that all necessary information is securely handled and readily available when needed. This approach not only improves the efficiency of interactions between AI Agents and web services but also enhances the overall trust and security of the UIM ecosystem. Let’s dive a bit deeper…

#### 2.5.6.1 Incorporating Billing Information During PAT Issuance

When AI Agents agree to a web service's policy and request a PAT, they can include their billing information as part of the agreement process. This information can be securely transmitted and stored as part of the PAT, ensuring that the web service has all necessary details for billing purposes.

**Steps to Implement**:

1. **Policy Retrieval:** The AI Agent retrieves the ODRL policy from the web service.  
2. **Billing Information Submission:** Along with agreeing to the policy, the AI Agent submits billing information (e.g., payment method, billing address, preferred currency).  
3. **PAT Issuance:** The web service issues a PAT that includes the AI Agent's billing information, along with the agreed-upon permissions, rate limits, and obligations.  
4. **Secure Storage:** The billing information is securely stored within the PAT or associated with the PAT in the web service’s system.

##### 2.5.6.1.1 Example Request

```json
{
  "agent_id": "ai-agent-1",
  "policy_reference": "http://example.com/policy/12345",
  "billing_info": {
    "payment_method": "credit_card",
    "billing_address": "123 AI Street, Tech City",
    "currency": "USD"
  },
  "signature": "Base64-encoded-signature"
}
```

##### 2.5.6.1.2 Example PAT Structure

```json
{
  "pat": {
    "uid": "pat-12345",
    "issued_to": "ai-agent-1",
    "issued_by": "web-service-1",
    "policy_reference": "http://example.com/policy/12345",
    "permissions": [
      "execute:intent/searchProducts",
      "rate_limit:1000/hour"
    ],
    "obligations": [
      "pay:0.01 USD per intent"
    ],
    "billing_info": {
      "payment_method": "credit_card",
      "billing_address": "123 AI Street, Tech City",
      "currency": "USD"
    },
    "valid_from": "2024-01-01T00:00:00Z",
    "valid_to": "2024-12-31T23:59:59Z"
  },
  "signature": "Base64-encoded-digital-signature"
}
```

#### 2.5.6.2 Automatic Billing Based on PAT

With billing information included in the PAT, the web service can automatically process payments as intents are executed. The web service’s transaction system can use the billing information to charge the AI Agent for each transaction without additional input.

##### 2.5.6.2.1 How It Works

* **Transaction Execution:** When the AI Agent executes an intent, the web service processes the request and records the transaction.  
* **Billing Automation:** The web service automatically charges the AI Agent using the payment method specified in the PAT, based on the transaction details (e.g., number of API calls, rate per call).  
* **Invoice Generation:** An invoice or receipt is generated and sent to the AI Agent for record-keeping.

![transaction flow](images/transaction-flow.png)

##### 2.5.6.2.2 Example Transaction Flow

1. **Intent Execution:** AI Agent sends a request to execute an intent.  
2. **Billing Trigger:** The web service processes the request and triggers the billing process using the PAT’s billing information.  
3. **Payment Processing:** The web service charges the AI Agent’s payment method.  
4. **Receipt Issuance:** The web service issues a receipt to the AI Agent.

#### 2.5.6.3 Security and Privacy Considerations

To ensure the security and privacy of billing information, the following measures should be implemented:

* **Encryption:** All billing information should be encrypted both at rest and in transit to protect against unauthorized access.  
* **Tokenization:** Payment methods (e.g., credit card details) can be tokenized, reducing the risk of exposure.  
* **Access Control:** Only authorized systems and personnel should have access to the billing information, and this access should be logged and monitored.  
* **Compliance:** Ensure compliance with relevant regulations (e.g., GDPR, PCI-DSS) to protect the privacy and security of billing information.

#### 2.5.6.4 Benefits of Including Billing Information in PATs

1. **Streamlined Process:** By including billing information in the PAT, the transaction process is streamlined, reducing the need for repeated information submission and minimizing friction.  
2. **Automated Billing:** Automating the billing process ensures timely and accurate payments, improving cash flow for web services and reducing administrative overhead for AI Agents.  
3. **Improved User Experience:** AI Agents can execute intents seamlessly without needing to repeatedly provide billing details, leading to a smoother user experience.  
4. **Enhanced Compliance:** Including billing information within the PAT structure ensures that all transactions are compliant with agreed-upon policies and obligations, reducing the risk of disputes.

![benefits of billing](images/billing-benefits.png)

### 2.6 Service Management APIs

#### 2.6.1 Purpose

Service management APIs facilitate the registration, maintenance, and overall management of web services within the UIM protocol ecosystem. These APIs allow web services to declare their capabilities, compliance policies, and availability, ensuring they are correctly integrated into the discovery and execution process.

#### 2.6.2 Implementation

* **Centralized Context**: Web services register directly with a central repository, providing standardized data about their capabilities. This ensures that the central discovery endpoint has the most accurate information.
* **Decentralized Context**: Services manage their registration independently, updating information in `agents.json` files hosted on their domains.
* **Hybrid Context**: Services can choose to register with the central repository or publish their information in `agents.json` files, providing flexibility and accommodating different use cases.

#### 2.6.3 Register Service

* **Endpoint**: /api/services  
* **Method**: POST  
* **Description**: Registers a new servicen with the central repository.
* **Parameters**:  
  * service_name (string, required): The name of the service.  
  * service_url (string, required): The URL of the service.  
  * description (string, required): A brief description of the service.
  * policy_url (string, optional): The polices URL of the service.
  * service_logo_url (string, optional): The URL of the service's logo.
  * service_terms_of_service_url (string, optional): The URL of the service's terms of service.
  * service_privacy_policy_url (string, optional): The URL of the service's privacy policy.

**Example Request:**

```json
{
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities",
}
```

#### 2.6.4 Update Service

* **Endpoint**: /api/services/{service_id}  
* **Method**: PUT  
* **Description**: Updates the details of an existing service.  
* **Parameters**: Same as Register Service.

#### 2.6.5 Delete Service

* **Endpoint**: /api/services/{service_id}  
* **Method**: DELETE  
* **Description**: Deletes a registered service.  
* **Parameters**:  
* **Parameters**: None

**Example Request:**

```http
DELETE /api/services/12345
```

#### 2.6.6 Retrieve Service

* **Endpoint**: /api/services/{service_id}  
* **Method**: GET  
* **Description**: Retrieves the details of a registered service.  
* **Parameters**: None

**Example Request:**

```http
GET /api/services/12345
```

**Example Response:**

```json
{
  "service_id": "12345",
  "service_name": "E-commerce Platform",
  "service_url": "https://api.ecommerce.com",
  "description": "Provides e-commerce functionalities"
}
```

### 2.7 Intent Management APIs

#### 2.7.1 Purpose

Intent management focuses on the creation, updating, and deletion of intents by web services. These processes ensure that the set of available actions remains accurate, relevant, and compliant with the latest service capabilities and regulatory standards.

#### 2.7.2 Implementation

* **Centralized Context**: Intent management is handled via APIs connected to the central repository, where intents are stored, updated, or removed as needed.
* **Decentralized Context**: Intents are managed locally by the web service, with updates reflected in the service’s published data structures, such as `agents.json` files.
* **Hybrid Context**: Web services can choose to manage intents centrally or locally, providing flexibility and accommodating different use cases. In the hybrid context, the central repository acts as a backup for the local intent management process.

#### 2.7.3 List All Intents for a Service

* **Endpoint**: /api/services/{service_id}/intents  
* **Method**: GET  
* **Description**: Lists all intents for a specific service.  
* **Parameters**: None.

**Example Request:**

```http
GET /api/services/12345/intents
```

**Example Response:**

```json
{
  "intents": [
    {
      "service_name": "E-commerce Platform",
      "intent_name": "SearchProducts",
      "intent_uid": "ecommerce.com:searchProducts:v1",
      "description": "Search for products based on given criteria",
      "input_parameters": [
        {"name": "query", "type": "string", "required": true},
        {"name": "category", "type": "string", "required": false},
        {"name": "price_range", "type": "string", "required": false},
        {"name": "sort_by", "type": "string", "required": false}
      ],
      "output_parameters": [
        {"name": "products", "type": "array", "required": true},
        {"name": "total_results", "type": "integer", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/products/search",
      "tags": ["e-commerce", "search", "products"]
    },
      // ... more intents
  ]
}
```

#### 2.7.4 Retrieve Intent Details

* **Endpoint**: /api/intents/{intent_uid}  
* **Method**: GET  
* **Description**: Retrieves the details of a specific intent.  
* **Parameters**: None.

**Example Request:**

```http
GET /api/intents/ecommerce.com:searchProducts:v1
```

**Example Response:**

```json
{
  "intent_uid": "ecommerce.com:searchProducts:v1",
  "service_name": "E-commerce Platform",
  "intent_name": "SearchProducts",
  "description": "Search for products based on given criteria",
  "input_parameters": [
    {"name": "query", "type": "string", "required": true},
    {"name": "category", "type": "string", "required": false},
    {"name": "price_range", "type": "string", "required": false},
    {"name": "sort_by", "type": "string", "required": false}
  ],
  "output_parameters": [
    {"name": "products", "type": "array", "required": true},
    {"name": "total_results", "type": "integer", "required": true}
  ],
  "endpoint": "https://api.ecommerce.com/products/search",
  "tags": ["e-commerce", "search", "products"]
}
```

#### 2.7.5 Create Intent

* **Endpoint**: /api/services/{service_id}/intents  
* **Method**: POST  
* **Description**: Creates a new intent for a specific service.  
* **Parameters**:
  * intent_uid (string, required): The unique identifier for the intent.
  * intent_name (string, required): The name of the intent.
  * description (string, required): A brief description of what the intent does.
  * input_parameters (array of objects, required): An array of input parameters required by the intent. Each parameter object includes:
    * name (string, required): The name of the parameter.
    * type (string, required): The data type of the parameter.
    * required (boolean, required): Indicates whether the parameter is required.
  * output_parameters (array of objects, required): An array of output parameters returned by the intent. Each parameter object includes:
    * name (string, required): The name of the parameter.
    * type (string, required): The data type of the parameter.
    * required (boolean, required): Indicates whether the parameter is required.
  * endpoint (string, required): The URL endpoint for the intent.
  * tags (array of strings, optional): An array of tags associated with the intent.

**Example Request:**

```json
POST /api/services/12345/intents
{
  "intent_uid": "ecommerce.com:GetProductDetails:v1",
  "intent_name": "GetProductDetails",
  "description": "Fetches detailed information about a specific product using its unique identifier",
  "parameters": [
    {"name": "product_id", "type": "string", "required": true}
    // ... more parameters
  ],
  "output_parameters": [
    {"name": "product_details", "type": "object", "required": true}
    // ... more output parameters
  ],
  "endpoint": "https://api.ecommerce.com/products/details",
  "tags": ["e-commerce", "product", "details"]
}
```

#### 2.7.6 Update Intent

* **Endpoint**: /api/intents/{intent_id}  
* **Method**: PUT  
* **Description**: Updates the details of an existing intent.  
* **Parameters**: Same as Create Intent.

#### 2.7.7 Delete Intent

* **Endpoint**: /api/intents/{intent_id}  
* **Method**: DELETE  
* **Description**: Deletes an existing intent.  
* **Parameters**: None

**Example Request:**

```http
DELETE /api/intents/67890
```

## 3. General API Guidelines and Standards

### 3.1 Pagination for List Endpoints

To handle large sets of data efficiently and improve performance, it's essential to implement pagination for list endpoints. Pagination allows clients to request specific subsets of data, making it easier to manage and process responses. Here, we'll define the pagination parameters, explain how they are used, and provide examples.

#### 3.1.1 Pagination Parameters

1. **page**: The page number to retrieve (integer, optional, default: 1).  
2. **page_size**: The number of items to include on each page (integer, optional, default: 10).

#### 3.1.2 Pagination Headers

In addition to the pagination parameters, the API will include pagination-related headers in the response to provide clients with information about the total number of items and pages available.

1. **X-Total-Count**: The total number of items available.  
2. **X-Total-Pages**: The total number of pages available.  
3. **X-Current-Page**: The current page number.  
4. **X-Page-Size**: The number of items per page.

#### 3.1.3 Example Pagination Request

Let's illustrate how pagination works with the "List All Intents for a Service" endpoint.

* **Endpoint**: /api/services/{service_id}/intents  
* **Method**: GET  
* **Description**: Lists all intents for a specific service with pagination support.

**Request Parameters**:

* page (integer, optional): The page number to retrieve (default: 1).  
* page_size (integer, optional): The number of items per page (default: 10).

**Example Request**:

```http
GET /api/services/12345/intents?page=2\&page_size=5
```

**Example Response Headers**:

```http
X-Total-Count: 20 
X-Total-Pages: 4 
X-Current-Page: 2 
X-Page-Size: 5
```

**Example Response Body**:

```json
{
  "intents": [
    {
      "intent_id": "67891",
      "intent_name": "GetProductDetails",
      "description": "Fetches detailed information about a specific product using its unique identifier",
      "tags": ["shopping", "product details", "retail"],
      "parameters": [
        {"name": "product_id", "type": "string", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/products/details"
    },
    {
      "intent_id": "67892",
      "intent_name": "AddToCart",
      "description": "Adds a specified product to the user's shopping cart",
      "tags": ["shopping", "cart", "retail"],
      "parameters": [
        {"name": "product_id", "type": "string", "required": true},
        {"name": "quantity", "type": "integer", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/cart/add"
    },
    {
      "intent_id": "67893",
      "intent_name": "Checkout",
      "description": "Processes the checkout for the current shopping cart",
      "tags": ["shopping", "checkout", "retail"],
      "parameters": [
        {"name": "payment_method", "type": "string", "required": true},
        {"name": "shipping_address", "type": "string", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/cart/checkout"
    },
    {
      "intent_id": "67894",
      "intent_name": "SearchOrders",
      "description": "Searches for orders based on specified criteria",
      "tags": ["orders", "search", "retail"],
      "parameters": [
        {"name": "order_id", "type": "string", "required": false},
        {"name": "date_range", "type": "string", "required": false},
        {"name": "status", "type": "string", "required": false}
      ],
      "endpoint": "https://api.ecommerce.com/orders/search"
    },
    {
      "intent_id": "67895",
      "intent_name": "GetOrderDetails",
      "description": "Fetches detailed information about a specific order",
      "tags": ["orders", "details", "retail"],
      "parameters": [
        {"name": "order_id", "type": "string", "required": true}
      ],
      "endpoint": "https://api.ecommerce.com/orders/details"
    }
  ]
}
```

### 3.2 Security and Compliance

#### 3.2.1 Authentication

Use OAuth2.0 for secure API authentication, ensuring that only authorized AI agents can access and execute intents.

#### 3.2.2 Encryption

Ensure all communications are encrypted using HTTPS, protecting data from interception and tampering.

#### 3.2.3 Compliance

Adhere to data protection regulations, such as GDPR, ensuring that all data handling practices are compliant with legal requirements.

### 3.3 Monitoring and Analytics

#### 3.3.1 Real-time Monitoring

Provide a dashboard for monitoring API usage and performance, offering insights into how the Unified Intent Mediator API is being used.

#### 3.3.2 Logging and Alerts

Implement logging and alerting systems to track unusual activity and ensure quick response to potential issues.

### 3.4 Scalability

#### 3.4.1 Caching Mechanisms

Implement caching mechanisms to handle frequently accessed data, improving response times and reducing load on servers.

#### 3.4.2 Load Balancing

Use load balancers to distribute traffic efficiently, ensuring that the Unified Intent Mediator API can handle high volumes of requests without performance degradation.

### 3.5 Error Management Strategy for the UIM Protocol

Error management is crucial for ensuring the robustness and reliability of the UIM protocol. By standardizing error codes, messages, and response handling across different layers, we can make it easier for developers to diagnose issues and build resilient systems. Below is a comprehensive approach to error management, followed by a detailed appendix of standard error codes and their meanings.

#### 3.5.1 Layer 1: Client-Side Errors (4xx Codes)

* **Description**: Errors that occur due to issues with the request made by the client (e.g., AI agents).  
* **Typical Issues**:  
  * Invalid input parameters.  
  * Unauthorized access.  
  * Resource not found.  
  * Method not allowed.  
* **Handling Strategy**:  
  * Validate all inputs before processing the request.  
  * Provide clear, actionable error messages to the client.  
  * Ensure that error responses are consistent across all endpoints.

**Example Response:**

```json
 {
   "error": {
     "code": "INVALID_PARAMETER",
     "message": "The parameter 'query' is required.",
     "details": null
   }
 }
```

#### 3.5.2 Layer 2: Server-Side Errors (5xx Codes)

* **Description**: Errors that occur due to issues on the server side, which may be due to system failures, unavailable services, or unhandled exceptions.  
* **Typical Issues**:  
  * Internal server errors.  
  * Service unavailable.  
  * Timeout.  
* **Handling Strategy**:  
  * Implement robust error logging and monitoring on the server side to quickly identify and address issues.  
  * Return meaningful error messages that do not expose internal details but provide enough information for troubleshooting.  
  * Implement retry logic where applicable, especially for temporary issues like timeouts.

**Example Response**:

```json
{
   "error": {
     "code": "INTERNAL_SERVER_ERROR",
     "message": "An unexpected error occurred on the server. Please try again later.",
     "details": null
   }
 }
```

#### 3.5.3 Layer 3: Protocol-Level Errors

* **Description**: Errors related to the operation of the UIM protocol itself, such as issues with intent execution, discovery, or API misuse.  
* **Typical Issues**:  
  * Invalid intent execution.  
  * Conflicts in intent versions.  
  * Unsupported operations.  
* **Handling Strategy**:  
  * Standardize responses for protocol-level errors, ensuring that all services using the UIM protocol handle these errors uniformly.  
  * Provide detailed documentation on these errors, including how to avoid or resolve them.

**Example Response**:

```json
{
   "error": {
     "code": "INTENT_EXECUTION_FAILED",
     "message": "The intent 'GetProductDetails' could not be executed due to missing required parameters.",
     "details": {
       "intent": "GetProductDetails",
       "missing_parameters": ["product_id"]
     }
   }
 }
```

#### 3.5.4 Standard Error Codes and Messages

Below is an appendix dedicated to standard error codes, their meanings, and recommended response structures.

##### 3.5.4.1 Client-Side Errors (4xx)

| Error Code | Message | Description | Example Scenario |
| :---- | :---- | :---- | :---- |
| INVALID_PARAMETER | "The parameter '{param}' is required." | The request is missing a required parameter or contains an invalid parameter. | A required field such as query in a search intent is not provided. |
| UNAUTHORIZED | "Unauthorized access. Authentication is required." | The request is not authenticated or the authentication token is invalid or expired. | The AI agent attempts to access a service without providing a valid OAuth2.0 token. |
| FORBIDDEN | "Access to this resource is forbidden." | The client is authenticated but does not have the necessary permissions to access the resource. | An AI agent tries to execute an intent that it does not have permission to use. |
| NOT_FOUND | "The requested resource '{resource}' was not found." | The specified resource or endpoint could not be found on the server. | The AI agent requests an intent or service that does not exist. |
| METHOD_NOT_ALLOWED | "The HTTP method '{method}' is not allowed for this endpoint." | The client attempted to use an HTTP method that is not supported by the endpoint. | Sending a POST request to an endpoint that only supports GET. |
| CONFLICT | "The request could not be completed due to a conflict." | The request could not be processed because of a conflict in the current state of the resource. | Attempting to register an intent that already exists under a different version. |
| UNSUPPORTED_MEDIA_TYPE | "The media type '{type}' is not supported." | The server does not support the media type of the request payload. | The client sends a request with an unsupported content type, such as text/xml instead of application/json. |

##### 3.5.4.2 Server-Side Errors (5xx)

| Error Code | Message | Description | Example Scenario |
| :---- | :---- | :---- | :---- |
| INTERNAL_SERVER_ERROR | "An unexpected error occurred on the server. Please try again later." | A generic error message when the server encounters an unexpected condition. | The server encounters a null pointer exception or other unhandled error. |
| SERVICE_UNAVAILABLE | "The service is temporarily unavailable. Please try again later." | The server is currently unable to handle the request due to maintenance or overload. | The server is down for maintenance, or a service dependency is unavailable. |
| GATEWAY_TIMEOUT | "The server did not receive a timely response from the upstream server." | The server, while acting as a gateway, did not receive a response from an upstream server in time. | A request to an external API exceeds the timeout limit. |
| NOT_IMPLEMENTED | "The requested functionality is not implemented." | The server does not support the functionality required to fulfill the request. | The AI agent attempts to use an intent that is not yet supported by the service. |

##### 3.5.4.3 Protocol-Level Errors

| Error Code | Message | Description | Example Scenario |
| :---- | :---- | :---- | :---- |
| INTENT_EXECUTION_FAILED | "The intent '{intent}' could not be executed due to {reason}." | The execution of an intent fails due to invalid input, missing parameters, or other issues. | An AI agent tries to execute GetProductDetails but fails because the required product_id is missing. |
| INTENT_NOT_SUPPORTED | "The intent '{intent}' is not supported by this service." | The requested intent is not recognized or supported by the target service. | An AI agent requests an intent that has been deprecated or is not implemented by the service. |
| VERSION_CONFLICT | "The intent version '{version}' is not supported." | There is a conflict between the requested version of the intent and the version supported by the service. | An AI agent attempts to execute version v1 of an intent when only v2 is supported. |
| INTENT_DEPRECATED | "The intent '{intent}' has been deprecated and is no longer supported." | The intent has been deprecated and is no longer available for use. | The AI agent calls a deprecated intent that has been removed in the latest version of the protocol. |

#### 3.5.5 Guidelines for Handling Errors

**Consistent Response Structure**: All error responses should follow a consistent JSON structure to make parsing and error handling easier for AI agents.

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Descriptive error message.",
    "details": {
      "additional": "context-specific information"
    }
  }
}
```

* **Detailed Messages**: Error messages should be descriptive enough to guide developers in resolving the issue, but not so detailed as to expose sensitive information.  
* **Error Logging and Monitoring**: Services implementing the UIM protocol should log all errors with sufficient detail (e.g., timestamps, request details, stack traces for server-side errors) to facilitate troubleshooting.  
* **User-Friendly Messages**: When errors are related to user actions, ensure that messages are clear and actionable, helping users correct their input or understand the issue.  
* **Deprecation Warnings**: When deprecating an intent or feature, provide warnings in the response to guide users towards alternatives before the feature is removed in a future release.
```

--------------------------------------------------------------------------------

### File: uim-mock-webservice/__init__.py
```
Path: uim-mock-webservice/__init__.py
Size: 0.00 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
```

--------------------------------------------------------------------------------

### File: uim-mock-webservice/main.py
```
Path: uim-mock-webservice/main.py
Size: 13.75 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import os
from pydantic import BaseModel, Field
from typing import Dict, Any
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
import jwt
from datetime import datetime, timedelta, timezone
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from fastapi.security import HTTPBearer
import base64
import uuid

# Load environment variables
load_dotenv()

class SearchRequest(BaseModel):
    location: str
    min_price: int = None
    max_price: int = None
    property_type: str = None

class SearchResponse(BaseModel):
    properties: list
    total_results: int

class DetailsRequest(BaseModel):
    property_id: str

class DetailsResponse(BaseModel):
    property_details: dict

class PolicyAgreementRequest(BaseModel):
    agent_id: str = Field(..., description="The unique identifier of the agent")
    signed_policy: str = Field(..., min_length=1, description="The signed policy document")
    agent_public_key: str = Field(..., min_length=1, description="The public key of the agent")

class ExecuteRequest(BaseModel):
    intent_uid: str = Field(..., description="The unique identifier of the intent")
    parameters: Dict[str, Any] = Field(..., description="The parameters for the intent")


app = FastAPI()

def get_key_pair(as_string: bool = False):
    """
    Get the key pair for the service.

    """
    try:
        private_key_path = os.path.join('keys', 'private_key.pem')
        public_key_path = os.path.join('keys', 'public_key.pem')

        if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
            print(f"Key pair not found for service under /keys.")
            raise Exception("Key pair not found.")

        with open(private_key_path, 'rb') as f:
            if as_string:
                private_key = f.read().decode('utf-8')
            else:
                private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None,
                    backend=default_backend()
                )

        with open(public_key_path, 'rb') as f:
            if as_string:
                public_key = f.read().decode('utf-8')
            else:
                public_key = serialization.load_pem_public_key(
                    f.read(),
                    backend=default_backend()
                )

        print(f"Key pair loaded for service under /keys.")
        return private_key, public_key
    except Exception as e:
        print(f"Error loading key pair for service: {e}")
        raise

UIM_SERVICE_PRIVATE_KEY, UIM_SERVICE_PUBLIC_KEY = get_key_pair()
UIM_SERVICE_LICENSE = os.getenv("UIM_SERVICE_LICENSE")

@app.get("/agents.json")
async def get_agents_json(request: Request):
    agents_json = create_agents_json(request)
    return JSONResponse(content=agents_json)

def create_agents_json(request: Request):
    base_url = f"{request.url.scheme}://{request.client.host}:{request.url.port}"
    public_key_pem = UIM_SERVICE_PUBLIC_KEY.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key_base64url = base64.urlsafe_b64encode(public_key_pem).decode('utf-8')

    return {
        "service-info": {
            "name": "fakerealestate.com",
            "description": "A fictional service providing property listings and real estate data.",
            "service_url": f"{base_url}",
            "service_logo_url": f"{base_url}/logo.png",
            "service_terms_of_service_url": f"{base_url}/terms",
            "service_privacy_policy_url": f"{base_url}/privacy"
        },
        "intents": [
            {
                "intent_uid": "fakerealestate.com:searchProperty:v1",
                "intent_name": "SearchProperty",
                "description": "Searches properties based on location, price range, and property type.",
                "input_parameters": SearchRequest.model_json_schema()["properties"],
                "output_parameters": SearchResponse.model_json_schema()["properties"],
                "tags": ["real estate", "search", "property"],
                "rate_limit": "1000/hour",
                "price": "0.00 USD"
            },
            {
                "intent_uid": "fakerealestate.com:getPropertyDetails:v1",
                "intent_name": "GetPropertyDetails",
                "description": "Fetches detailed information for a specific property based on property ID.",
                "input_parameters": DetailsRequest.model_json_schema()["properties"],
                "output_parameters": DetailsResponse.model_json_schema()["properties"],
                "tags": ["real estate", "details", "property"],
                "rate_limit": "1000/hour",
                "price": "0.01 USD"
            }
        ],
        "uim-public-key": public_key_base64url,
        "uim-policy-file": f"{base_url}/uim-policy.json",
        "uim-api-discovery": f"{base_url}/uim/intents/search",
        "uim-api-execute": f"{base_url}/uim/execute",
        "uim-compliance": {
            "standards": ["ISO27001", "GDPR"],
            "regional-compliance": {
                "EU": "GDPR",
                "US-CA": "CCPA"
            },
            "notes": "Data is encrypted in transit and at rest."
        },
        "uim-license": UIM_SERVICE_LICENSE
    }

@app.get("/uim-policy.json")
async def get_policy_json(request: Request):
    policy_json = create_policy_json(request)
    return JSONResponse(content=policy_json)

def create_policy_json(request: Request):
    base_url = f"{request.url.scheme}://{request.client.host}:{request.url.port}"
    
    return {
        "@context": "http://www.w3.org/ns/odrl.jsonld",
        "@type": "odrl:Set",
        "@id": f"{base_url}/uim-policy",
        "profile": "http://www.w3.org/ns/odrl/2/core",
        "permission": [
            {
            "target": f"{base_url}/uim/execute/SearchProperty",
            "action": {
                "id": "odrl:execute",
                "refinement": [
                {
                    "leftOperand": "odrl:count",
                    "operator": "odrl:lteq",
                    "rightOperand": 1000,
                    "unit": "odrl:hour"
                }
                ]
            }
            },
            {
            "target": f"{base_url}/uim/execute/GetPropertyDetails",
            "action": {
                "id": "odrl:execute",
                "refinement": [
                {
                    "leftOperand": "odrl:count",
                    "operator": "odrl:lteq",
                    "rightOperand": 1000,
                    "unit": "odrl:hour"
                }
                ]
            },
            "duty": [
                {
                "action": [
                    {
                        "rdf:value": { "@id": "odrl:compensate" },
                        "refinement": [{
                            "leftOperand": "payAmount",
                            "operator": "eq",
                            "rightOperand": { "@value": "0.01", "@type": "xsd:decimal" },
                            "unit": "http://dbpedia.org/resource/Euro"
                        }]
                    }
                ]
                }
            ]
            }
        ],
        "prohibition": [
            {
            "target": [
                f"{base_url}/uim/execute/SearchProperty",
                f"{base_url}/uim/execute/GetPropertyDetails"
            ],
            "action": {
                "id": "odrl:execute",
                "refinement": [
                {
                    "leftOperand": "odrl:count",
                    "operator": "odrl:gt",
                    "rightOperand": 1000,
                    "unit": "odrl:hour"
                }
                ]
            }
            }
        ],
        "party": [
            {
            "function": "odrl:assigner",
            "identifier": f"{base_url}/assigner"
            },
            {
            "function": "odrl:assignee",
            "identifier": f"{base_url}/assignee"
            }
        ],
        "asset": [
            {
            "id": f"{base_url}/uim/execute/SearchProperty",
            "type": "odrl:Asset"
            },
            {
            "id": f"{base_url}/uim/execute/GetPropertyDetails",
            "type": "odrl:Asset"
            }
        ]
    }

def verify_signed_policy(signed_policy: str, agent_public_key: str) -> Dict:
    try:
        # Decode the Base64URL-encoded public key string back to bytes
        decoded_public_key = base64.urlsafe_b64decode(agent_public_key)

        # Load the decoded bytes into a _RSAPublicKey object
        public_key = serialization.load_pem_public_key(
            decoded_public_key,
            backend=default_backend()
        )
        # Decode and verify the signed policy
        decoded_policy = jwt.decode(signed_policy, public_key, algorithms=["RS256"])
        print(f"Verification successful for policy: {decoded_policy}")
        return True
    except jwt.ExpiredSignatureError as e:
        print(f"Error during policy verification: Signature has expired. Full error: {e}")
        return False
    except jwt.InvalidTokenError as e:
        print(f"Error during policy verification: Invalid token. Full error: {e}")
        return False

def verify_pat(request: Request):
    authorization_header = request.headers.get("Authorization")
    if not authorization_header:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if authorization_header:
        token_type, token = authorization_header.split(" ")
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    try:
        # Decode the token without verification to extract the payload
        decoded_pat = jwt.decode(token, options={"verify_signature": False})
        UIM_SERVICE_PRIVATE_KEY, UIM_SERVICE_PUBLIC_KEY = get_key_pair(True)
        
        # Verify the token's signature
        jwt.decode(
            token,
            UIM_SERVICE_PRIVATE_KEY,
            algorithms=["HS256"],
            options={"verify_aud": False}
        )
        
        # Check if the PAT is expired
        if datetime.fromisoformat(decoded_pat["valid_to"]) < datetime.now(timezone.utc):
            raise HTTPException(status_code=403, detail="PAT expired.")
        
        # Additional checks can be added here, such as permissions and obligations
        print (f"Verification successful for PAT: {decoded_pat}")
        
    except jwt.InvalidTokenError as e:    # Invalid token
        raise HTTPException(status_code=403, detail=f"Invalid PAT: {e}")
    
    return decoded_pat

@app.post("/pat/issue")
async def issue_pat(request: PolicyAgreementRequest):
    print(f"Received policy agreement request: {request}")
    
    if not request.signed_policy:
        raise HTTPException(status_code=400, detail="Missing policy agreement.")
    if not request.agent_public_key:
        raise HTTPException(status_code=400, detail="Missing agent public key.")
    if not request.agent_id:
        raise HTTPException(status_code=400, detail="Missing agent id.")
    
    # Verify the signed policy
    if not verify_signed_policy(request.signed_policy, request.agent_public_key):
        raise HTTPException(status_code=400, detail="Policy verification failed.")
    
    # Generate and sign a PAT
    pat = {
        "uid": f"uim-pat-{uuid.uuid4()}",
        "issued_to": request.agent_id,
        "policy_reference": "uim-policy.json",
        "valid_from": datetime.now(timezone.utc).isoformat(),
        "valid_to": (datetime.now(timezone.utc) + timedelta(days=365)).isoformat()
    }
    UIM_SERVICE_PRIVATE_KEY, UIM_SERVICE_PUBLIC_KEY = get_key_pair(True)
    token = jwt.encode(pat, UIM_SERVICE_PRIVATE_KEY, algorithm="HS256")
    return {"uim-pat": token}

# Define the security scheme
security_scheme = HTTPBearer()
@app.post("/uim/execute", dependencies=[Depends(security_scheme)])
async def execute_intent(request: ExecuteRequest, pat: dict = Depends(verify_pat)):
    intent_uid = request.intent_uid
    parameters = request.parameters

    if intent_uid == "fakerealestate.com:searchProperty:v1":
        location = parameters.get('location')
        min_price = parameters.get('min_price')
        max_price = parameters.get('max_price')
        property_type = parameters.get('property_type')

        # Simulate a search operation
        if location == "New York" and property_type == "apartment":
            response = {
                "total_results": 1,
                "properties": [
                    {
                        "property_id": "123",
                        "name": "Luxury Apartment",
                        "price": 2000,
                        "location": "New York",
                        "property_type": "apartment"
                    }
                ]
            }
        else:
            response = {
                "total_results": 0,
                "properties": []
            }
    elif intent_uid == "fakerealestate.com:getPropertyDetails:v1":
        property_id = parameters.get('property_id')

        # Simulate fetching property details
        if property_id == "123":
            response = {
                "property_details": {
                    "property_id": "123",
                    "name": "Luxury Apartment",
                    "price": 2000,
                    "location": "New York",
                    "property_type": "apartment",
                    "description": "A luxurious apartment in the heart of New York."
                }
            }
        else:
            response = {
                "property_details": {}
            }
    else:
        raise HTTPException(status_code=400, detail="Unknown intent_uid")

    return JSONResponse(content=response)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)```

--------------------------------------------------------------------------------

### File: uim-mock-webservice/requirements.txt
```
Path: uim-mock-webservice/requirements.txt
Size: 0.06 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
cryptography
fastapi
pydantic
pyjwt
python-dotenv
uvicorn
requests```

--------------------------------------------------------------------------------

### File: uim-mock-webservice/keys/private_key.pem
```
Path: uim-mock-webservice/keys/private_key.pem
Size: 1.66 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCsYQ10NefvoV+U
/UPiCmAkx66wnZsaBYDeszl6dMgHwc7LzuzTqQ5rp0enA/kQzkHthX54cX5Gcpul
B0SDsS0CgEs6Dss7Zdvq43uc79pgSrVVPQ2zbuqJ+d48jeCdI44T2s5bdHuR21qn
UQoOijeE/c2nz3sOeXVV4xIxevOai0BPqvG5qgB9HpUfEfzpTYUsGxyLhsFAyxd1
NRURwezaUTDpGnG4bd3Lh86NLe+41yMJG2vqpsW/Yk8iZsSO8GWFwIqXTmCozm6A
H8ONWs48UqROEbM7W7Xs3AoOLCP/I5RcRVn90Cxn9z20ONTbAZxb+6Bo2BzrPvVl
68v6wzt/AgMBAAECggEAbuTs09MOB9IH/IBGGHfWTDMNxd9OdZoOwrYIByhzutHK
qMDRCIWcmlL+PIrIwy/9p8EWkINq2gVG7g7T2+iybQZ93ra/tdGcfeqkjlybXxEQ
wOpLEyEKz4KonsojMtQ5xbogwSMZj8bO9g6jaqEugGcK06cdoj0u5/bxsFVJvCRE
/97WjY+VfIC0qaE4xNYudY8x6FndfnKgIB3LgPKC0mlx63W5KkOEXzDtKuJ4DvNb
KSKFi2klrOnc/b3B7SGOghDJyVg4kkPhQo92IP4iJbD282h1G1cZROwUkbFre6Aq
qd1rcvHjDjt75b9K1F9Nz22Fmci6ZgtCZOvr09qQkQKBgQDWNhkxBpIKLeronq6D
XRDRKsBKfg2Y+EM+ulvd2Yj/X/i+fwH8F8xWw4H0flM48jB/v+o+mqywaO8wFC4t
j1Vs6vuWQfmtVwIwbLa2m+RSJNr2GwcEIxuMJNLbnCOsoAsTPV1MHYjakIEsuTor
ve1TfxE3huMR+50/gCLqdI/3WQKBgQDOAdEa4k7v+c36x3rUynNkOjPcJy7vRAS5
pJt9jX82Rm9GhuD55i/t6Q3VkOAf2tTks8ZyLMkhc22KsIawfsxCaVwoycdmfO+2
MdzpW9eObIqEkuW2+KahQ+0SQsHAS6MgIhHHYN5aisNRsaspWwATdjAtJqEMU/La
hDl8rSZGlwKBgQCIS6WdtwOG7I5x8j0xoi6IF/5/p1K5iQUoTWUUdEwhyQu5EZDO
uMmwTvdJ/HKxYhAPyKmfqcTE/g9qdPyoynFdOupXQaU+cIUZEKL0753H0mFrg+jj
7f6iHe/4AZIFTVOeq0XIn2YrQxSdw0FLAa6WmNv4i5/BGmqEM+CDcyUDCQKBgClt
Lhqk5dDWQDitAqNl7tx549Hiw0p0OCsI0gfme21zro7VMsquIndKRXDsCFX/kI5J
JJ/zJ6MlbiLUqtE1Pmggfdrp8MJIX4AY+N6ojGlkpFpSnAU2bXPCkBr697FuxGgC
0eZxMWWtv+devhe76AEB5GBAA2TSQOT2cAUFYMwTAoGBAI2y7mmqrc7bwTi9jPmB
Fe82Fi1Fooa6O6CArbAZsVon5RPPDntZTrxwRiG1lRqW27n6hgnOCwrd81j7WsYj
0GdRxDe2ZOkkIr82rAkoJhCDB30DVDfhHNmBNlQN0kXWZAxa192yrFXAxY9VHuRY
60j9Ay5DtiuM5ywUfE5tGGjf
-----END PRIVATE KEY-----
```

--------------------------------------------------------------------------------

### File: uim-mock-webservice/keys/public_key.pem
```
Path: uim-mock-webservice/keys/public_key.pem
Size: 0.44 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArGENdDXn76FflP1D4gpg
JMeusJ2bGgWA3rM5enTIB8HOy87s06kOa6dHpwP5EM5B7YV+eHF+RnKbpQdEg7Et
AoBLOg7LO2Xb6uN7nO/aYEq1VT0Ns27qifnePI3gnSOOE9rOW3R7kdtap1EKDoo3
hP3Np897Dnl1VeMSMXrzmotAT6rxuaoAfR6VHxH86U2FLBsci4bBQMsXdTUVEcHs
2lEw6RpxuG3dy4fOjS3vuNcjCRtr6qbFv2JPImbEjvBlhcCKl05gqM5ugB/DjVrO
PFKkThGzO1u17NwKDiwj/yOUXEVZ/dAsZ/c9tDjU2wGcW/ugaNgc6z71ZevL+sM7
fwIDAQAB
-----END PUBLIC KEY-----
```

--------------------------------------------------------------------------------

### File: images/abstract-dark.png
```
Path: images/abstract-dark.png
Size: 98.35 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/abstract.png
```
Path: images/abstract.png
Size: 100.53 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/adoption.png
```
Path: images/adoption.png
Size: 42.86 KB
Last Modified: 2024-08-27 17:04:04
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/ai-agent-architecture.png
```
Path: images/ai-agent-architecture.png
Size: 105.57 KB
Last Modified: 2024-08-30 13:42:31
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/ai-capabilities.png
```
Path: images/ai-capabilities.png
Size: 56.32 KB
Last Modified: 2024-08-27 17:02:31
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/ai-discovery.png
```
Path: images/ai-discovery.png
Size: 56.54 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/architecture-comparison.png
```
Path: images/architecture-comparison.png
Size: 49.71 KB
Last Modified: 2024-08-30 13:50:28
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/billing-benefits.png
```
Path: images/billing-benefits.png
Size: 87.85 KB
Last Modified: 2024-08-27 16:53:11
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/blockchain.png
```
Path: images/blockchain.png
Size: 42.29 KB
Last Modified: 2024-08-27 16:20:00
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/catalyst.png
```
Path: images/catalyst.png
Size: 101.99 KB
Last Modified: 2024-08-27 18:50:41
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/central-arch-box.png
```
Path: images/central-arch-box.png
Size: 12.80 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/central-arch.png
```
Path: images/central-arch.png
Size: 44.89 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/centralized-repo.png
```
Path: images/centralized-repo.png
Size: 93.22 KB
Last Modified: 2024-08-30 13:41:30
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/challenges-spec.png
```
Path: images/challenges-spec.png
Size: 94.16 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/challenges.png
```
Path: images/challenges.png
Size: 136.77 KB
Last Modified: 2024-08-27 18:47:22
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/concept.png
```
Path: images/concept.png
Size: 65.19 KB
Last Modified: 2024-08-27 16:03:55
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/decentral-arch-box.png
```
Path: images/decentral-arch-box.png
Size: 42.52 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/decentral-arch.png
```
Path: images/decentral-arch.png
Size: 35.68 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/developer-ecosystem.png
```
Path: images/developer-ecosystem.png
Size: 55.12 KB
Last Modified: 2024-08-27 17:06:55
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/discoverability.png
```
Path: images/discoverability.png
Size: 106.18 KB
Last Modified: 2024-08-27 16:10:02
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/dns-txt-and-agents-txt.png
```
Path: images/dns-txt-and-agents-txt.png
Size: 92.59 KB
Last Modified: 2024-08-27 16:57:37
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/dns-vs-txt.png
```
Path: images/dns-vs-txt.png
Size: 63.78 KB
Last Modified: 2024-08-27 16:38:04
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/ecommerce-example.png
```
Path: images/ecommerce-example.png
Size: 51.85 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/execute-method.png
```
Path: images/execute-method.png
Size: 86.70 KB
Last Modified: 2024-08-27 16:05:40
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/execution-method.png
```
Path: images/execution-method.png
Size: 72.42 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/future-development.png
```
Path: images/future-development.png
Size: 59.56 KB
Last Modified: 2024-08-27 17:01:08
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/future-timeline.png
```
Path: images/future-timeline.png
Size: 97.95 KB
Last Modified: 2024-08-27 19:05:18
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/hybrid-arch-box.png
```
Path: images/hybrid-arch-box.png
Size: 28.53 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/hybrid-arch.png
```
Path: images/hybrid-arch.png
Size: 37.71 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/intent-discovery.png
```
Path: images/intent-discovery.png
Size: 72.23 KB
Last Modified: 2024-08-27 16:12:01
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/intent-format.png
```
Path: images/intent-format.png
Size: 40.91 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/logo-white.png
```
Path: images/logo-white.png
Size: 101.48 KB
Last Modified: 2024-09-16 22:41:33
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/logo.png
```
Path: images/logo.png
Size: 477.16 KB
Last Modified: 2024-09-16 16:37:52
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/main-architecture.png
```
Path: images/main-architecture.png
Size: 47.15 KB
Last Modified: 2024-08-30 13:44:16
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/mediator-platform.png
```
Path: images/mediator-platform.png
Size: 57.57 KB
Last Modified: 2024-08-27 16:14:07
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/odrl-benefits.png
```
Path: images/odrl-benefits.png
Size: 114.37 KB
Last Modified: 2024-08-27 16:54:56
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/pat-implementation.png
```
Path: images/pat-implementation.png
Size: 139.66 KB
Last Modified: 2024-08-27 16:42:51
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/policy-fields.png
```
Path: images/policy-fields.png
Size: 83.92 KB
Last Modified: 2024-08-27 16:39:57
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/policy-flow.png
```
Path: images/policy-flow.png
Size: 41.04 KB
Last Modified: 2024-08-27 16:34:40
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/realestate-example.png
```
Path: images/realestate-example.png
Size: 46.21 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/revenue-sharing.png
```
Path: images/revenue-sharing.png
Size: 55.43 KB
Last Modified: 2024-08-27 16:21:03
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/solution-comparison.png
```
Path: images/solution-comparison.png
Size: 49.07 KB
Last Modified: 2024-08-30 13:56:35
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/subscription.png
```
Path: images/subscription.png
Size: 52.56 KB
Last Modified: 2024-08-27 16:18:00
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/transaction-flow.png
```
Path: images/transaction-flow.png
Size: 68.73 KB
Last Modified: 2024-08-27 16:51:14
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/uim-benefits.png
```
Path: images/uim-benefits.png
Size: 77.16 KB
Last Modified: 2024-08-27 16:25:48
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/uim-protocol.png
```
Path: images/uim-protocol.png
Size: 64.94 KB
Last Modified: 2024-08-27 19:17:20
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/usage-based.png
```
Path: images/usage-based.png
Size: 54.54 KB
Last Modified: 2024-08-27 16:16:59
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: images/vocabulary.png
```
Path: images/vocabulary.png
Size: 52.22 KB
Last Modified: 2024-08-27 16:28:11
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/Dockerfile
```
Path: centralized-discovery-service/Dockerfile
Size: 0.19 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/README.md
```
Path: centralized-discovery-service/README.md
Size: 2.19 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# Centralized Intent Discovery Service

This project implements a centralized intent discovery service using FastAPI, enabling AI agents to discover and search for intents across multiple web services as per the UIM protocol.

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip package manager

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/synaptiai/uim-protocol.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd centralized-intent-discovery
   ```

3. **Configure the database**:

   - Update `app/config.py` with your PostgreSQL database URL.

4. **Run the setup script**:

   ```bash
   bash scripts/setup.sh
   ```

5. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

- **Discovery**:
  - `GET /api/intents/search`: Search for intents based on criteria.
  - `GET /api/search/`: Search intents using a natural language query.

## Crawling Mechanism

- The crawler starts on application startup.
- It fetches `agents.json` files using DNS TXT records or directly.
- Intents are stored in the PostgreSQL database for fast querying.

## Testing

Run the unit tests using:

```bash
python -m unittest discover -s tests
```

## Configuration

Modify `app/config.py` to change application settings such as the database URL.

## License

This project is licensed under the Apache License 2.0.

## Contributing suggestions

1. Implement authentication and rate limiting for API endpoints.
2. Extend natural language processing capabilities for better query handling.
3. Add a web interface for monitoring crawled intents.
4. Integrate a scheduler to periodically update the intent index.
5. Deploy the application using a production-grade server like Gunicorn.
6. Add CI/CD Pipeline: Use GitHub Actions to automate testing and deployment.
7. Include Code Quality Tools: Integrate tools like flake8, black, and isort for code formatting and linting.
8. Enhance NLP Capabilities: Use a library like spaCy or NLTK for advanced natural language processing in the search functionality.
9. Add a Frontend Interface: Optionally, create a simple web interface using React or Vue.js for users to interact with the service.
```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/docker-compose.yml
```
Path: centralized-discovery-service/docker-compose.yml
Size: 0.38 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:password@db/uim_db
  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: uim_db
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/pytest.ini
```
Path: centralized-discovery-service/pytest.ini
Size: 0.07 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# pytest.ini

[pytest]
asyncio_default_fixture_loop_scope = function```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/requirements.txt
```
Path: centralized-discovery-service/requirements.txt
Size: 0.14 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
fastapi
uvicorn
SQLAlchemy
psycopg2-binary
aiohttp
dnspython
pydantic
python-dotenv
alembic
spacy
pytest
pytest-asyncio
pydantic-settings
httpx```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/config.py
```
Path: centralized-discovery-service/app/config.py
Size: 0.29 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Configuration settings for the application."""
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/database.py
```
Path: centralized-discovery-service/app/database.py
Size: 0.46 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
import logging

logger = logging.getLogger(__name__)

try:
    engine = create_engine(settings.DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except Exception as e:
    logger.error(f"Database connection failed: {e}")
    raise```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/dependencies.py
```
Path: centralized-discovery-service/app/dependencies.py
Size: 0.23 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/dependencies.py

from app.database import SessionLocal
from contextlib import contextmanager

def get_db():
    """Provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/main.py
```
Path: centralized-discovery-service/app/main.py
Size: 0.54 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/main.py

from fastapi import FastAPI
from app.routers import discovery, search
from app.database import engine, Base
from app.utils.logging import setup_logging

def create_app():
    """Initialize FastAPI app and include routers."""
    app = FastAPI(title="Centralized Intent Discovery Service")

    # Set up logging
    setup_logging()

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Include routers
    app.include_router(discovery.router)
    app.include_router(search.router)

    return app

app = create_app()```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/routers/__init__.py
```
Path: centralized-discovery-service/app/routers/__init__.py
Size: 0.12 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/routers/__init__.py

from .discovery import router as discovery_router
from .search import router as search_router```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/routers/discovery.py
```
Path: centralized-discovery-service/app/routers/discovery.py
Size: 1.09 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/routers/discovery.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas
from app.dependencies import get_db
from app.crud.intent import get_intents_by_filters

router = APIRouter(prefix="/api/intents", tags=["Discovery"])

@router.get("/search", response_model=List[schemas.Intent])
def search_intents(
    intent_name: Optional[str] = Query(None, min_length=3),
    uid: Optional[str] = None,
    description: Optional[str] = Query(None, min_length=3),
    tags: Optional[str] = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Search for intents based on criteria."""
    tag_list = [tag.strip() for tag in tags.split(',')] if tags else None
    intents = get_intents_by_filters(
        db=db,
        intent_name=intent_name,
        uid=uid,
        description=description,
        tags=tag_list,
        skip=skip,
        limit=limit
    )
    if not intents:
        raise HTTPException(status_code=404, detail="No intents found.")
    return intents```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/routers/search.py
```
Path: centralized-discovery-service/app/routers/search.py
Size: 0.77 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/routers/search.py

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.dependencies import get_db
from app.services.nlp import process_natural_language_query

router = APIRouter(prefix="/api/search", tags=["Search"])

@router.get("/", response_model=List[schemas.Intent])
def search_intents_by_query(
    query: str = Query(..., min_length=3),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """Search intents using a natural language query."""
    intents = process_natural_language_query(db=db, query=query, skip=skip, limit=limit)
    if not intents:
        raise HTTPException(status_code=404, detail="No intents found.")
    return intents```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/models/__init__.py
```
Path: centralized-discovery-service/app/models/__init__.py
Size: 0.10 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/models/__init__.py

from .service import Service
from .intent import Intent
from .tag import Tag```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/models/intent.py
```
Path: centralized-discovery-service/app/models/intent.py
Size: 1.05 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/models/intent.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from app.database import Base

intent_tags = Table(
    'intent_tags',
    Base.metadata,
    Column('intent_id', Integer, ForeignKey('intents.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Intent(Base):
    """Intent model representing a single intent."""
    __tablename__ = 'intents'

    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    intent_uid = Column(String, unique=True, index=True, nullable=False)
    intent_name = Column(String, index=True, nullable=False)
    description = Column(Text)
    input_parameters = Column(JSON)
    output_parameters = Column(JSON)
    endpoint = Column(String, nullable=False)

    service = relationship('Service', back_populates='intents')
    tags = relationship('Tag', secondary=intent_tags, back_populates='intents')```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/models/service.py
```
Path: centralized-discovery-service/app/models/service.py
Size: 0.72 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/models/service.py

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Service(Base):
    """Service model representing an intent provider."""
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)
    service_url = Column(String, nullable=False)
    service_logo_url = Column(String, nullable=True)
    service_terms_of_service_url = Column(String, nullable=True)
    service_privacy_policy_url = Column(String, nullable=True)

    intents = relationship('Intent', back_populates='service', cascade='all, delete-orphan')```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/models/tag.py
```
Path: centralized-discovery-service/app/models/tag.py
Size: 0.45 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/models/tag.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from .intent import intent_tags

class Tag(Base):
    """Tag model for intent categorization."""
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    intents = relationship('Intent', secondary=intent_tags, back_populates='tags')```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/schemas/__init__.py
```
Path: centralized-discovery-service/app/schemas/__init__.py
Size: 0.29 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/schemas/__init__.py

from .intent import (
    InputParameter,
    OutputParameter,
    IntentBase,
    IntentCreate,
    IntentUpdate,
    Intent
)
from .service import (
    ServiceInfo,
    ServiceBase,
    ServiceCreate,
    ServiceUpdate,
    Service,
    AgentsJson
)
from .tag import Tag```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/schemas/intent.py
```
Path: centralized-discovery-service/app/schemas/intent.py
Size: 1.22 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/schemas/intent.py

from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from .tag import Tag

class InputParameter(BaseModel):
    name: str
    type: str
    required: bool
    description: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class OutputParameter(BaseModel):
    name: str
    type: str
    description: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class IntentBase(BaseModel):
    intent_uid: str
    intent_name: str
    description: str
    input_parameters: List[InputParameter]
    output_parameters: List[OutputParameter]
    endpoint: str
    tags: Optional[List[Tag]] = None
    model_config = ConfigDict(from_attributes=True)

class IntentCreate(IntentBase):
    pass
    model_config = ConfigDict(from_attributes=True)

class IntentUpdate(BaseModel):
    description: Optional[str] = None
    input_parameters: Optional[List[InputParameter]] = None
    output_parameters: Optional[List[OutputParameter]] = None
    endpoint: Optional[str] = None
    tags: Optional[List[Tag]] = None
    model_config = ConfigDict(from_attributes=True)

class Intent(IntentBase):
    id: int
    service_id: int
    model_config = ConfigDict(from_attributes=True)```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/schemas/service.py
```
Path: centralized-discovery-service/app/schemas/service.py
Size: 1.17 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/schemas/service.py

from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from .intent import Intent, IntentCreate

class ServiceBase(BaseModel):
    name: str
    description: str
    service_url: str
    service_logo_url: Optional[str] = None
    service_terms_of_service_url: Optional[str] = None
    service_privacy_policy_url: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class ServiceCreate(ServiceBase):
    model_config = ConfigDict(from_attributes=True)
    pass

class ServiceUpdate(BaseModel):
    description: Optional[str] = None
    service_url: Optional[str] = None
    service_logo_url: Optional[str] = None
    service_terms_of_service_url: Optional[str] = None
    service_privacy_policy_url: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class Service(ServiceBase):
    id: int
    intents: List[Intent] = []
    model_config = ConfigDict(from_attributes=True)

class ServiceInfo(ServiceBase):
    model_config = ConfigDict(from_attributes=True)
    pass

class AgentsJson(BaseModel):
    service_info: ServiceInfo
    intents: List[IntentCreate]
    model_config = ConfigDict(from_attributes=True)```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/schemas/tag.py
```
Path: centralized-discovery-service/app/schemas/tag.py
Size: 0.22 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/schemas/tag.py

from pydantic import BaseModel, ConfigDict

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    model_config = ConfigDict(from_attributes=True)```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/crud/__init__.py
```
Path: centralized-discovery-service/app/crud/__init__.py
Size: 0.26 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/crud/__init__.py

from .intent import (
    get_intent_by_uid,
    create_intent,
    update_intent,
    delete_intent,
    get_intents_by_filters
)
from .service import (
    get_service_by_name,
    create_service,
    update_service,
    delete_service
)```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/crud/intent.py
```
Path: centralized-discovery-service/app/crud/intent.py
Size: 3.04 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/crud/intent.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas
import logging

logger = logging.getLogger(__name__)

def get_intent_by_uid(db: Session, intent_uid: str):
    """Retrieve an intent by its unique identifier."""
    return db.query(models.Intent).filter(models.Intent.intent_uid == intent_uid).first()

def get_intents_by_filters(
    db: Session,
    intent_name: str = None,
    uid: str = None,
    description: str = None,
    tags: list = None,
    skip: int = 0,
    limit: int = 10
):
    """Retrieve intents based on filters."""
    query = db.query(models.Intent)
    if intent_name:
        query = query.filter(models.Intent.intent_name.ilike(f"%{intent_name}%"))
    if uid:
        query = query.filter(models.Intent.intent_uid == uid)
    if description:
        query = query.filter(models.Intent.description.ilike(f"%{description}%"))
    if tags:
        query = query.join(models.Intent.tags).filter(models.Tag.name.in_(tags))
    return query.offset(skip).limit(limit).all()

def create_intent(db: Session, intent_data: schemas.IntentCreate, service_id: int):
    """Create a new intent associated with a service."""
    db_intent = models.Intent(
        service_id=service_id,
        intent_uid=intent_data.intent_uid,
        intent_name=intent_data.intent_name,
        description=intent_data.description,
        input_parameters=intent_data.input_parameters,
        output_parameters=intent_data.output_parameters,
        endpoint=intent_data.endpoint
    )
    # Handle tags
    if intent_data.tags:
        tags = []
        for tag_name in intent_data.tags:
            # Check if the tag already exists
            tag = db.query(models.Tag).filter_by(name=tag_name).first()
            if not tag:
                tag = models.Tag(name=tag_name)
                db.add(tag)
                db.flush()  # To get the tag ID
            tags.append(tag)
        db_intent.tags = tags
    try:
        db.add(db_intent)
        db.commit()
        db.refresh(db_intent)
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error creating intent: {e}")
        raise
    return db_intent

def update_intent(db: Session, intent: models.Intent, updates: schemas.IntentUpdate):
    """Update an existing intent."""
    for key, value in updates.dict(exclude_unset=True).items():
        if key == "tags" and value is not None:
            # Update tags
            tags = []
            for tag_name in value:
                tag = db.query(models.Tag).filter(models.Tag.name == tag_name).first()
                if not tag:
                    tag = models.Tag(name=tag_name)
                    db.add(tag)
                    db.commit()
                    db.refresh(tag)
                tags.append(tag)
            intent.tags = tags
        else:
            setattr(intent, key, value)
    db.commit()
    db.refresh(intent)
    return intent

def delete_intent(db: Session, intent: models.Intent):
    """Delete an intent."""
    db.delete(intent)
    db.commit()```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/crud/service.py
```
Path: centralized-discovery-service/app/crud/service.py
Size: 1.48 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/crud/service.py

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app import models, schemas
import logging

logger = logging.getLogger(__name__)

def get_service_by_name(db: Session, name: str):
    """Retrieve a service by its name."""
    return db.query(models.Service).filter(models.Service.name == name).first()

def create_service(db: Session, service_info: schemas.ServiceCreate):
    """Create a new service."""
    db_service = models.Service(
        name=service_info.name,
        description=service_info.description,
        service_url=service_info.service_url,
        service_logo_url=service_info.service_logo_url,
        service_terms_of_service_url=service_info.service_terms_of_service_url,
        service_privacy_policy_url=service_info.service_privacy_policy_url
    )
    try:
        db.add(db_service)
        db.commit()
        db.refresh(db_service)
    except IntegrityError as e:
        db.rollback()
        logger.error(f"Integrity error creating service: {e}")
        raise
    return db_service

def update_service(db: Session, service: models.Service, updates: schemas.ServiceUpdate):
    """Update an existing service."""
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(service, key, value)
    db.commit()
    db.refresh(service)
    return service

def delete_service(db: Session, service: models.Service):
    """Delete a service and its associated intents."""
    db.delete(service)
    db.commit()```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/services/__init__.py
```
Path: centralized-discovery-service/app/services/__init__.py
Size: 0.18 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/services/__init__.py

from .crawler import start_crawler
from .dns_utils import get_agents_json_url_from_dns
from .nlp import process_natural_language_query  # If NLP is implemented```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/services/crawler.py
```
Path: centralized-discovery-service/app/services/crawler.py
Size: 3.14 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/services/crawler.py

import asyncio
import aiohttp
import logging
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.crud.service import create_service, get_service_by_name
from app.crud.intent import create_intent
from app.schemas.service import ServiceCreate
from app.schemas.intent import IntentCreate
from app.models import Service, Intent
from app.config import settings
import dns.asyncresolver

logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self, domains: List[str], db_session: Session):
        self.domains = domains
        self.db_session = db_session

    async def start(self):
        tasks = [self.process_domain(domain) for domain in self.domains]
        await asyncio.gather(*tasks)

    async def process_domain(self, domain: str):
        agents_json_url = await get_agents_json_url_from_dns(domain)
        if not agents_json_url:
            agents_json_url = f"https://{domain}/agents.json"

        agents_json_data = await self.fetch_agents_json(agents_json_url)
        if agents_json_data:
            self.process_agents_json(agents_json_data)

    async def fetch_agents_json(self, url: str) -> Dict[str, Any]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Failed to fetch {url}, status code: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def process_agents_json(self, agents_json_data: Dict[str, Any]):
        """Process the agents.json data."""
        try:
            service_info = agents_json_data['service_info']
            service_data = ServiceCreate(**service_info)
            service = get_service_by_name(self.db_session, service_info['name'])
            if not service:
                service = create_service(self.db_session, service_data)
            for intent_data in agents_json_data['intents']:
                create_intent(self.db_session, IntentCreate(**intent_data), service.id)
            self.db_session.commit()
        except Exception as e:
            logger.error(f"Error saving agents.json data: {e}")
            self.db_session.rollback()

async def get_agents_json_url_from_dns(domain: str) -> str:
    """Fetch the agents.json URL from DNS TXT records."""
    try:
        resolver = dns.asyncresolver.Resolver()
        answers = await resolver.resolve(domain, 'TXT')
        for rdata in answers:
            for txt_string in rdata.strings:
                if txt_string.startswith(b"agents_json_url="):
                    return txt_string.decode().split("=", 1)[1]
        return None
    except Exception as e:
        logger.error(f"Error fetching DNS TXT records for {domain}: {e}")
        return None

async def start_crawler(domains: List[str], db_session: Session):
    """Start the crawler for a list of domains."""
    crawler = Crawler(domains=domains, db_session=db_session)
    await crawler.start()```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/services/dns_utils.py
```
Path: centralized-discovery-service/app/services/dns_utils.py
Size: 0.59 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/services/dns_utils.py

import dns.resolver
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)

@lru_cache(maxsize=1024)
def get_agents_json_url_from_dns(domain):
    """Retrieve agents.json URL from DNS TXT records."""
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            txt_record = rdata.to_text().strip('"')
            if 'uim-agents-file=' in txt_record:
                return txt_record.split('=')[1]
    except Exception as e:
        logger.error(f"DNS lookup failed for {domain}: {e}")
    return None```

--------------------------------------------------------------------------------

### File: centralized-discovery-service/app/services/nlp.py
```
Path: centralized-discovery-service/app/services/nlp.py
Size: 0.71 KB
Last Modified: 2024-09-13 21:07:58
```

**Contents:**
```
# app/services/nlp.py

import logging
from typing import List
from app.models.intent import Intent
from sqlalchemy.orm import Session
from sqlalchemy import func

logger = logging.getLogger(__name__)

def process_natural_language_query(db: Session, query: str, skip: int = 0, limit: int = 10) -> List[Intent]:
    """Process a natural language query to search for intents."""
    try:
        # Using PostgreSQL full-text search
        intents = db.query(Intent).filter(
            func.to_tsvector('english', Intent.description).match(query)
        ).offset(skip).limit(limit).all()
        return intents
    except Exception as e:
        logger.error(f"Error processing natural language query: {e}")
        return []```

--------------------------------------------------------------------------------

### File: podcast/UIM Protocol.m4a
```
Path: podcast/UIM Protocol.m4a
Size: 3208.42 KB
Last Modified: 2024-09-20 16:27:51
```

**Contents:**
```
[Binary file or non-UTF-8 encoding]
```

--------------------------------------------------------------------------------

### File: podcast/transcript.txt
```
Path: podcast/transcript.txt
Size: 15.51 KB
Last Modified: 2024-09-20 17:58:46
```

**Contents:**
```
0:00: Ever try to, like, get your smart assistant to book something online? 
 0:04: Oh, tell me about it. 
 0:05: It's like pulling teeth. 
 0:06: Why is that still so clunky. 
 0:07: Yeah, it's like the A I is stuck in the dark ages of the internet, like trying to stream a movie but you're still on dial up. 
 0:13: It just doesn't work well. 
 0:14: Ouch. 
 0:15: Yeah. 
 0:16: So what's the issue then? 
 0:17: Well, the way A I currently interacts with websites super inefficient, it's like if you had to read a whole book by translating each individual letter, one by one that sounds awful and slow. 
 0:30: A I is basically doing that right now with web scraping and all these clunky workarounds. 
 0:34: So we need a faster, a more reliable way for A I to talk to websites. 
 0:37: Exactly. 
 0:38: Enter U I, right. 
 0:39: Unified intent mediator protocol. 
 0:41: Got it. 
 0:41: U I is like a universal translator. 
 0:44: So instead of all this fumbling around U I, lets A I and websites directly communicate, you know, understand each other's intentions. 
 0:53: So instead of teaching A I to like decode the entire internet, we're giving it a set of tools and a common language and at the heart of it intense, intense. 
 1:04: Basically, imagine a predefined action a website can say, hey, I offer this book flight intent and the A I doesn't have to struggle to interpret all the messy website code. 
 1:15: It just says I want to use the book flight intent and boom, the website knows exactly what to do smoother faster. 
 1:20: I like it. 
 1:21: But are we talking about like a massive library of every single action on the internet? 
 1:28: That's where things get interesting. 
 1:29: There are two main approaches being explored, centralized versus decentralized. 
 1:33: One's like a giant digital card catalog and the other is more like A I agents browsing independent bookstores. 
 1:41: I'm intrigued. 
 1:42: So centralized first. 
 1:44: What are we looking at there? 
 1:45: Picture a single massive repository. 
 1:48: Every website using U I registers its intents there. 
 1:52: A I agents can search it to find the specific actions. 
 1:55: They need one stop shop convenient, but a little risky. 
 2:00: Right. 
 2:00: Putting all your eggs in one basket. 
 2:02: What happens if that central repository goes down? 
 2:04: You're right. 
 2:05: That's the potential downside single point of failure, which is why there's the decentralized approach? 
 2:11: Ok. 
 2:11: So how does that work instead of that central repository information is stored directly on each website A I agents would use something similar to like what we use now, DNS to find websites more resilient because no single point of failure. 
 2:25: Right. 
 2:25: Right. 
 2:26: So both approaches have their pros and cons. 
 2:28: It seems like it's early days still. 
 2:29: Right. 
 2:30: Still figuring all this out. 
 2:31: Oh, absolutely. 
 2:32: The draft specification even mentions a potential hybrid approach, best of both worlds, maybe hybrid. 
 2:40: Tell me more, think of it like this. 
 2:42: A central directory helps A I agents discover services. 
 2:47: But the actual interaction happens directly with the website. 
 2:51: OK. 
 2:51: So you get the ease of searching with the flexibility of a decentralized system. 
 2:55: Exactly. 
 2:55: I'm starting to see the potential here. 
 2:57: How U I could be a game changer. 
 2:59: But let's bring it down to earth for a sec. 
 3:01: How would this work in practice? 
 3:03: Say I want to buy something online. 
 3:05: U I changes that. 
 3:07: How? 
 3:07: OK. 
 3:08: So you tell your A I assistant, find me the best deal on noise, canceling headphones. 
 3:12: But instead of just searching one website or clumsily scraping data, it uses U I to instantly connect with a bunch of retailers simultaneously. 
 3:20: So like having a personal shopper. 
 3:22: Exactly. 
 3:22: And because they're using U I, their websites can communicate product info pricing all directly to the A I. 
 3:29: Makes the whole process incredibly efficient. 
 3:31: No more digging through endless websites, no more comparing prices on a million tabs. 
 3:35: Precisely. 
 3:36: I like where this is going. 
 3:37: But we've all heard the stories, right? 
 3:39: A I running wild. 
 3:40: How do we make sure it's using this power responsibly? 
 3:43: Well, U I has built in security and control mechanisms. 
 3:46: OK. 
 3:46: Good, good. 
 3:47: And it all revolves around something called a policy adherence token or pat A pat like a digital hall pass for A I pretty much and A I needs to obtain a Pat before it can use a particular intent on a website. 
 4:00: It's like a key that unlocks specific actions. 
 4:03: So websites still have control. 
 4:04: It's not just open season for A I to do whatever it wants. 
 4:07: Exactly. 
 4:08: And that's where something called the open digital rights language where ODR comes in ODL at PAT. 
 4:15: Lots of acronyms today. 
 4:16: we'll unpack that one next. 
 4:17: Ok. 
 4:18: So back to ODR L like a digital content. 
 4:21: Yeah, exactly. 
 4:21: It's how websites set the ground rules for A I. 
 4:25: So it's not just like hoping A I will behave itself with ODR. 
 4:30: Website owners can specify, you know exactly how their data and services can be used. 
 4:34: So they can say how often an intent can be used, what data the A I can access. 
 4:39: Yeah, even implement billing systems. 
 4:41: So this is starting to sound more like well run systems. 
 4:44: That's the idea. 
 4:45: And this is where pa t the digital hall pass comes back in to use an intent. 
 4:49: The A I has to show a Pat proving it's allowed access, you know, according to the website's rules. 
 4:54: So no Pat, no service. 
 4:56: Exactly. 
 4:57: That's how websites keep control. 
 4:59: Even with A I in the mix, it's all about responsible access this whole system. 
 5:04: It's like what building a secure infrastructure for A I on the web. 
 5:07: Yes. 
 5:08: And think about what this could mean. 
 5:10: For something, like, say online shopping. 
 5:13: Oh, yeah. 
 5:14: Ok. 
 5:14: Imagine a world where you've got an A I shopping assistant that just knows what you want instead of being bombarded with irrelevant stuff. 
 5:21: Exactly. 
 5:22: And because all these online retailers are using U I, your A I assistant can compare everything instantly. 
 5:28: Products, prices, reviews across what, dozens of sites all at once. 
 5:33: It's like having a superhuman shopping buddy. 
 5:35: No more. 
 5:36: Endless scrolling. 
 5:37: Ok. 
 5:37: I'm sold. 
 5:38: But what are those of us who aren't like tech wizards? 
 5:41: That's a great point. 
 5:42: But that's the thing about U I, it has the potential to make the web easier for everyone even if you don't know all the ins and outs of websites and stuff. 
 5:49: Right. 
 5:50: Imagine, for example, booking a doctor's appointment. 
 5:53: Oh, yeah, those websites can be a nightmare with U I. 
 5:56: You could just tell your A I assistant schedule a doctor's appointment for next week and it just does it. 
 6:03: Wow, that would be amazing. 
 6:05: Especially for people with disabilities or anyone who struggles with tech. 
 6:08: Absolutely breaks down those barriers. 
 6:10: Makes the web more inclusive. 
 6:12: Yeah, I love that. 
 6:13: And it's not just about convenience, it's about empowering people to actually use the internet confidently. 
 6:18: Ok. 
 6:18: Yeah, that's huge. 
 6:19: This is what tech about. 
 6:21: Exactly. 
 6:22: But like anything new, it has its challenges. 
 6:25: We've got to make sure it's accessible to everyone. 
 6:27: Not just the big tech companies. 
 6:29: Exactly. 
 6:29: If only a handful of companies control it, it could actually make inequality worse. 
 6:34: So it needs to be developed in an open way with everyone at the table. 
 6:38: Exactly. 
 6:39: It's about democratizing access to information, to opportunity. 
 6:43: It's like we're building a new digital city. 
 6:45: I like that. 
 6:46: We want to make sure it's designed for everyone. 
 6:47: Yes. 
 6:48: And just like building a city, it takes planning, collaboration and a shared vision. 
 6:53: Absolutely. 
 6:54: So how do we get there from where we are now with U I still in its early stages to this more inclusive future? 
 7:02: I think the first step is talking about it, having open and honest conversations, getting everyone on the same page, policymakers, tech leaders, researchers, the public, everyone because it's going to impact all of us. 
 7:14: Exactly. 
 7:15: We need to talk about the good and the bad, the ethical stuff and we need to do that now before it's too late to change. 
 7:21: Course, absolutely. 
 7:22: We have to be proactive in shaping the future. 
 7:24: We want responsible innovation, right? 
 7:26: Embracing the potential but being cautious and that brings us to another big one. 
 7:31: Security. 
 7:32: The million dollar question with A I, we're talking about giving A I more access. 
 7:36: Of course, security is a concern but that's where those safeguards come in. 
 7:40: Right. 
 7:40: Exactly. 
 7:40: Patties and ODR they're there to give websites control over how A I interacts with their stuff, like building a house with strong locks. 
 7:49: Exactly. 
 7:50: It can be welcoming and secure. 
 7:53: So U I has huge potential but it's not a magic solution. 
 7:58: Exactly. 
 7:58: It's a powerful tool and we need to proceed carefully having those open conversations every step of the way. 
 8:04: Exactly. 
 8:05: It feels like U I could be a turning point but it's not just up to the developers to figure this out is it. 
 8:10: You're right. 
 8:10: This is where our listeners come in. 
 8:12: Wait, really? 
 8:13: What can our listeners do? 
 8:14: I thought we were just like along for the ride U I has the potential to change so much about our lives, how we shop, access, health care, you name it, but it's still being shaped. 
 8:25: So there's still time to influence it. 
 8:26: Absolutely. 
 8:27: And the more people understand U I, the more they can help shape it. 
 8:31: Yes. 
 8:32: Learn about it, talk about it, make your voice heard. 
 8:34: Exactly. 
 8:35: And this project is designed to be collaborative. 
 8:38: So they want our feedback, they're asking for it. 
 8:40: Share your ideas, get involved. 
 8:42: I love that. 
 8:43: OK. 
 8:43: Before we get too carried away, let's talk about where things stand right now, right. 
 8:47: So still a work in progress, technical stuff is being finalized. 
 8:51: There's a lot of experimentation going on. 
 8:54: So not quite ready for prime time, not quite, but we're starting to see some real world pilot program. 
 9:00: Really? 
 9:02: What are people doing with it? 
 9:03: A few retailers are integrating it into their platforms, testing it out, seeing how it improves A I powered shopping. 
 9:10: Those A I shopping assistants, we talked about, they might be closer than we think. 
 9:14: What else. 
 9:15: Travel, booking, customer service, even health care. 
 9:19: It's like the early days of the iphone. 
 9:20: Exactly. 
 9:21: And those early adopters, they were crucial. 
 9:24: The same goes for U I. 
 9:25: The more people who use it give feedback, the faster it'll develop. 
 9:29: Makes sense. 
 9:30: This is a really exciting time to be following U I. 
 9:32: But we've got to be realistic too. 
 9:34: It's not a magic bullet, it has its limitations and we need to keep those ethical considerations in mind, making sure it benefits everyone. 
 9:41: Absolutely. 
 9:41: This is about humanity, not just technology, so big question for it. 
 9:46: If U I takes off, what happens to the web as we know it? 
 9:51: Oh, that is a big question. 
 9:54: It could be huge. 
 9:56: Think about it. 
 9:56: The web right now. 
 9:58: It's designed for us, for humans. 
 10:00: We click, we scroll, we read. 
 10:02: But what if A I becomes a primary citizen of the web? 
 10:06: Are you saying U I could change the entire online landscape potentially? 
 10:10: Yes. 
 10:11: If A I can directly access and understand the information on websites, who knows what's possible? 
 10:18: A I powered search engines that actually get us talking to websites instead of using clunky interfaces. 
 10:24: The possibilities are really exciting. 
 10:26: I'm getting a little bit of a like nervous excitement about all this. 
 10:29: Me too. 
 10:30: It's like standing on the edge of something brand new. 
 10:32: A little exhilarating a little daunting. 
 10:34: Exactly. 
 10:34: But it's definitely going to be interesting. 
 10:35: So it's like we're watching the trailer for this crazy sci fi movie. 
 10:38: Right. 
 10:39: And we're all on the edge of our seats waiting to see what happens next. 
 10:42: But, ok, let's rewind a little bit back to reality. 
 10:45: What needs to happen to take U I M from experiment to like mainstream. 
 10:52: Well, for starters we need the big players to get on board. 
 10:56: Yeah. 
 10:56: Imagine if like a Google Amazon Microsoft, the Big guns. 
 11:00: Exactly. 
 11:01: Imagine if they embraced U I integrated it into everything they do, that would definitely get everyone's attention, right? 
 11:08: And the good news is a lot of them are already involved in developing this and other A I standard. 
 11:13: So things are moving definitely, but it can't just be about big tech, right? 
 11:17: What about everybody else? 
 11:18: We need to make sure U I works for smaller businesses, developers, regular people. 
 11:23: Exactly. 
 11:23: If we want a truly inclusive web, everyone needs to be able to use it. 
 11:27: So how do we make that happen? 
 11:28: Well, we need to make U I easy to use, right? 
 11:31: Build tools and resources so anyone can adopt it regardless of their tech skills. 
 11:36: Exactly. 
 11:37: Democratize access, so to speak, I like that, make it available to everyone. 
 11:41: But even with the best tools, people still need to know what it is, right? 
 11:44: That's right. 
 11:44: Education is key, the more people understand U I, the more likely they are to embrace it, right? 
 11:50: Because knowledge is power. 
 11:51: Right. 
 11:52: Exactly. 
 11:52: So we need more resources, tutorials, workshops, make it easy to learn and not just the technical stuff, we need to talk about the ethical side, the social impact because ultimately U I is a tool and like any tool it can be used for good or bad. 
 12:09: It's up to us to decide how we want to use it. 
 12:11: It really is, we have to be mindful of the consequences, make sure it's being used to benefit everyone. 
 12:16: So that's the goal, right? 
 12:17: To create a better future for everybody. 
 12:20: That's what we're hoping for. 
 12:21: And that's where honestly our listeners come in. 
 12:24: All right, what can they do? 
 12:26: Stay informed, ask questions, talk about it, start a conversation. 
 12:30: Exactly. 
 12:31: The future isn't set in stone. 
 12:33: We all have a role to play in shaping it. 
 12:35: I like that. 
 12:35: It's a collaborative effort. 
 12:36: Well, on that note, I think we've reached the end of our deep dive into U I. 
 12:41: It's been a, a lot to process. 
 12:44: Yeah, but super fascinating. 
 12:46: It really feels like we're on the cusp of something big here. 
 12:49: We really do. 
 12:49: This could change everything about how we use the internet and it's exciting to think about where it might lead. 
 12:55: It certainly is. 
 12:56: So to all our listeners out there. 
 12:57: Thank you as always for joining us. 
 12:59: Thank you. 
 13:00: And remember the future is in our hands, stay curious, stay engaged and we'll see you next time for another deep dive. 
```

--------------------------------------------------------------------------------

### File: uim-mock-agent/README.md
```
Path: uim-mock-agent/README.md
Size: 2.31 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
# UIM Mock Agent

UIM Mock Agent is a Python-based application that simulates an AI agent interacting with a mock web service according to the Unified Intent Mediator (UIM) specification. It demonstrates the discovery and execution of intents, issuance of Policy Adherence Tokens (PATs), policy retrieval and signing, and secure key management for multiple web services.

## Overview

The UIM Mock Agent is designed with a modular architecture, separating concerns into distinct components:

- Discovery module for fetching and interpreting intent metadata
- Execution module for running intents
- Policy management for retrieving and signing ODRL policies
- Key management for generating and storing RSA key pairs
- Error handling module for centralized error management

Technologies used:

- Python 3.x
- requests library for HTTP interactions
- jwt for JSON Web Token handling
- cryptography for key pair generation and management
- pytest for testing (not implemented in the current state)

Project structure:

```txt
uim-mock-agent/
├── src/
│   ├── discovery.py
│   ├── intent_execution.py
│   ├── pat_issuance.py
│   ├── policy_management.py
│   ├── policy_signing.py
│   ├── key_management.py
│   ├── error_handling.py
│   └── cli_interface.py
├── keys/
│   └── {service_url}/
│       ├── private_key.pem
│       └── public_key.pem
- `requirements.txt`: Lists project dependencies
└── README.md
```

## Features

- Discover available intents from a mock web service
- Execute intents with proper input handling
- Retrieve and sign ODRL policies for verification
- Generate and manage RSA key pairs for each web service
- Handle errors and provide clear feedback
- Command-line interface for user interaction

## Getting Started

### Requirements

- Python 3.7 or higher
- pip (Python package manager)

### Quickstart

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd uim-mock-agent
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:

   ```bash
   python src/cli_interface.py
   ```

This will demonstrate the discovery of intents and key management functionality. For other features, you can run the respective Python files in the `src` directory.
```

--------------------------------------------------------------------------------

### File: uim-mock-agent/requirements.txt
```
Path: uim-mock-agent/requirements.txt
Size: 0.05 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
cryptography
pydantic
pyjwt
python-dotenv
requests```

--------------------------------------------------------------------------------

### File: uim-mock-agent/keys/http_localhost_4000/private_key.pem
```
Path: uim-mock-agent/keys/http_localhost_4000/private_key.pem
Size: 1.66 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC3KrKkgOHHY8ZX
CIlwsYresUJaZgYW2V8goY1GwnHdL2tq79BCLG14xk9OsjnrSu7UX+8QQ8vZMFex
MdfpnyMOS5OdhGARuRAVgPCNWtZYSE44h07cI1uspP9VmGb+jXq7XKWYIZvPfTMe
IPxLOV7K+9NG18otjdVYSnK7f3gKlVHefyinGOlgHv7jkoHktSL4fsfAZJzcHHp0
78M5DgRoyqL0M4BYuLXR60cBBjAOCphqTQX/S0fqv2Al8iBiVPwskF5Qh1mpcf9w
JJdATv1MJ4qvUl6JQmXYw4JRekHMvEqa7QSwGbNJ2+Fa1GDMfO0KmNO1hF7ukOGK
5R1XFHa/AgMBAAECggEAScXsxc0TItfQ3uUVVkpsAF2st/Q3p6RNaDspR8KxUcDz
ptKIMt7qCKb28l9ebKJ1pxwskYR86jFKYJgOuo3Z9LwD7IGQoBLFo6OXP5fClTQq
LSJyZL/pAJREMxl7AjPBpw0dtTR0KRHoMM5gT3v/7gmXgwUO7WIe97ykkVg55Sio
raPWzt91Muv8AfsZEPEPRfLiQlp2Qy8I56NY2aArtJ8CbANhUSJ/TTTRxX9QgifD
lO0OPHYQkhr2USNzsQz0ApSJHPORGZDq2D1DxfaM6Y5BGSw546ZL8vqKjSd/e/j8
Fnk/h+k/6EOgzfJT1bcVlSmZlP5LMGvhapMU33QHgQKBgQDYzJbg6SHzC/eopmSI
TiKVfkKdvQQnUsO+XirHcxbJzAqJBUgAREC0khloNs1UQW8BXKjhcBzoDrDROT/c
3Fcq26zyP49Catnp0o4M1+u34d4N3gFXuHIX8g2id5NTUGz0lTxKWSLpD7ToAZBn
bDhEZ7rG1p/AtguAiwaIuDEK8QKBgQDYSUzAcSGOnCS1kzGraxpUJmF7UBqV6dBp
oFRmNsShBSgnyskTzTTZQXyci+inBoYypfpjs2lep8R1R+wO8/cscnCOih2LsT+1
UXlAUbWuFGfgSlcWaXcfEJVjovNDBbZ88AfM6SGeuYRDPEuFiZgSdpKlu1IDwap8
mMokP9W8rwKBgArljZfUX+51ZYdGhbsMIlTdOb/v5iuLz2bcGM5ZjIWsCcOFTm8k
/xOUXE6OopdfipLI83wRRIKtalm5xOn28TKoQ/MRGsQ91qIYASfIGoLtiVmtFOgx
zxpBAkpuNCt12WQZtCQQgt6v+WnH2lg4akOV6x9fXjwzajSVyEhK6bwhAoGAXy56
yWG/+8t5WDLrs91RW+D8G1FYMcsQvbsiCU1m4NmtHz3dmYpADLAGD7p+ayqy2g0z
ELc+0roP+fDp0HbKutOt9vyPHg+l0ryFGKocwvwV7p2oj6NgGdqpc4ydc0xLT9Yu
CJ47/mbz7sbVEXJI6y8lQCwcXqzWwzhWFPfGrt8CgYEAngLqgzqOq7/qPYqk6pTE
O5kWoX9HC/32m4t/bz94tVnE/wkYZ+uUwJ2zvWxqH/xJqe/c5na7dECgn1cRBXZ2
i3fmpwQyZYrMK4kGoTmbSSHoWakb71thnKu4sbKZz9WFGrkL0DMy9fIbeLMYVzip
J5q3jCdIwIQMeKgmsskKP3s=
-----END PRIVATE KEY-----
```

--------------------------------------------------------------------------------

### File: uim-mock-agent/keys/http_localhost_4000/public_key.pem
```
Path: uim-mock-agent/keys/http_localhost_4000/public_key.pem
Size: 0.44 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtyqypIDhx2PGVwiJcLGK
3rFCWmYGFtlfIKGNRsJx3S9rau/QQixteMZPTrI560ru1F/vEEPL2TBXsTHX6Z8j
DkuTnYRgEbkQFYDwjVrWWEhOOIdO3CNbrKT/VZhm/o16u1ylmCGbz30zHiD8Szle
yvvTRtfKLY3VWEpyu394CpVR3n8opxjpYB7+45KB5LUi+H7HwGSc3Bx6dO/DOQ4E
aMqi9DOAWLi10etHAQYwDgqYak0F/0tH6r9gJfIgYlT8LJBeUIdZqXH/cCSXQE79
TCeKr1JeiUJl2MOCUXpBzLxKmu0EsBmzSdvhWtRgzHztCpjTtYRe7pDhiuUdVxR2
vwIDAQAB
-----END PUBLIC KEY-----
```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/cli_interface.py
```
Path: uim-mock-agent/src/cli_interface.py
Size: 4.72 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
from intent_execution import execute_intent, get_intent_params
from error_handling import handle_error, UIMMockAgentError
from discovery import fetch_agents_json, extract_intent_metadata
from policy_management import fetch_policy, display_policy
from policy_signing import sign_policy
from pat_issuance import handle_pat_issuance
from key_management import generate_key_pair, get_key_pair
import json
import os

current_pat = None
current_service_url = None

def display_menu():
    print("\nUIM Mock Agent CLI")
    print("1. Manage Keys")
    print("2. Discover Intents")
    print("3. View Policy")
    print("4. Sign Policy and Get PAT")
    print("5. Execute Intent")
    print("6. Exit")

def get_user_choice():
    try:
        choice = input("Enter your choice (1-7): ")
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def handle_discover_intents():
    global current_service_url
    try:
        agents_json = fetch_agents_json()
        current_service_url = agents_json.get("service_url", "http://localhost:4000")
        metadata = extract_intent_metadata(agents_json)
        intents = metadata["intents"]
        print("\nAvailable Intents:")
        for intent in intents:
            print(f"- {intent['name']}: {intent['description']} (Agent: {intent['agent']})")
    except Exception as e:
        print(handle_error(e))

def handle_execute_intent():
    global current_pat
    if not current_pat:
        print("No PAT available. Please sign the policy and get a PAT first.")
        return

    try:
        intent_uid = input("Enter the intent UID: ")
        params = get_intent_params(intent_uid)
        user_params = {}
        for param, details in params.items():
            user_params[param] = input(f"Enter value for {param} ({details['type']}): ")

        agents_json = fetch_agents_json()
        execute_endpoint = agents_json.get("uim-api-execute", "http://localhost:4000/uim/execute")

        result = execute_intent(intent_uid, user_params, execute_endpoint, current_pat)
        print("Intent Execution Result:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Error executing intent: {str(e)}")

def handle_view_policy():
    try:
        policy = fetch_policy()
        display_policy(policy)
    except Exception as e:
        print(handle_error(e))

def handle_sign_policy_and_get_pat():
    global current_pat
    global current_service_url
    try:
        policy = fetch_policy()
        signed_policy = sign_policy(policy, current_service_url)
        agent_id = input("Enter your agent ID: ")
        result = handle_pat_issuance(signed_policy, agent_id)
        if result["uim-pat"]:
            current_pat = result["uim-pat"]
            print(f"PAT issued successfully: {current_pat}")
        else:
            print(f"Failed to issue PAT: {result['error']}")
    except Exception as e:
        print(handle_error(e))

def handle_key_management():
    global current_service_url
    print("\nKey Management")
    print("1. Generate new key pair")
    print("2. View existing key pair")
    print("3. Set current service URL")
    choice = input("Enter your choice (1-3): ")

    try:
        if choice == '1':
            if not current_service_url:
                print("Please set the current service URL first.")
                return
            generate_key_pair(current_service_url)
            print(f"New key pair generated for {current_service_url}")
        elif choice == '2':
            if not current_service_url:
                print("Please set the current service URL first.")
                return
            private_key, public_key = get_key_pair(current_service_url)
            print(f"Existing key pair for {current_service_url}:")
            print(f"Private key: {private_key}")
            print(f"Public key: {public_key}")
        elif choice == '3':
            current_service_url = input("Enter the service URL: ")
            print(f"Current service URL set to: {current_service_url}")
        else:
            print("Invalid choice")
    except Exception as e:
        print(handle_error(e))

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            handle_key_management()            
        elif choice == '2':
            handle_discover_intents()
        elif choice == '3':
            handle_view_policy()
        elif choice == '4':
            handle_sign_policy_and_get_pat()
        elif choice == '5':
            handle_execute_intent()
        elif choice == '6':
            print("Exiting UIM Mock Agent CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/discovery.py
```
Path: uim-mock-agent/src/discovery.py
Size: 2.80 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import requests
import json
from typing import Dict, List
from error_handling import handle_error, NetworkError, APIError
from key_management import get_key_pair

SERVICE_URL = "http://localhost:4000"  # Adjust this URL if needed
AGENTS_ENDPOINT = f"{SERVICE_URL}/agents.json"

def fetch_agents_json() -> Dict:
    try:
        response = requests.get(AGENTS_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error fetching agents.json: {str(e)}")
    except json.JSONDecodeError as e:
        raise APIError(f"Error parsing agents.json: {str(e)}")

def extract_intent_metadata(agents_data: Dict) -> Dict:
    print(f"Debug: agents_data structure: {json.dumps(agents_data, indent=2)}")
    intents = []
    execute_endpoint = agents_data.get("uim-api-execute")
    print(f"Debug: execute_endpoint: {execute_endpoint}")

    service_url = agents_data.get("service-info", {}).get("service_url", SERVICE_URL)

    for intent in agents_data.get("intents", []):
        print(f"Debug: Processing intent: {json.dumps(intent, indent=2)}")
        intents.append({
            "name": intent.get("intent_name"),
            "description": intent.get("description"),
            "agent": agents_data.get("service-info", {}).get("name"),
            "intent_uid": intent.get("intent_uid"),
            "service_url": service_url
        })

    print(f"Debug: Extracted intents: {json.dumps(intents, indent=2)}")
    return {
        "intents": intents,
        "execute_endpoint": execute_endpoint,
        "service_url": service_url
    }

def main():
    try:
        agents_data = fetch_agents_json()
        print(f"Debug: Full agents_data structure: {json.dumps(agents_data, indent=2)}")
        service_info = agents_data.get("service-info", {})
        print(f"Debug: service_info: {service_info}")

        metadata = extract_intent_metadata(agents_data)
        print(f"Debug: metadata: {metadata}")

        intent_metadata = metadata["intents"]
        print(f"Debug: intent_metadata: {intent_metadata}")

        service_url = metadata["service_url"]
        private_key, public_key = get_key_pair(service_url)

        print(f"Service: {service_info.get('name')}")
        print(f"Description: {service_info.get('description')}")
        print(f"Service URL: {service_url}")
        print("\nAvailable Intents:")
        for intent in intent_metadata:
            print(f"Debug: Processing intent: {intent}")
            print(f"- {intent['name']} ({intent['agent']}): {intent['description']}")

        print(f"\nKey pair retrieved for service URL: {service_url}")

    except Exception as e:
        print(f"Debug: Exception occurred: {str(e)}")
        print(f"Debug: Exception type: {type(e)}")
        print(handle_error(e))

if __name__ == "__main__":
    main()```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/error_handling.py
```
Path: uim-mock-agent/src/error_handling.py
Size: 1.93 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import requests

class UIMMockAgentError(Exception):
    """Base exception class for UIM Mock Agent"""
    pass

class NetworkError(UIMMockAgentError):
    """Exception raised for network-related errors"""
    pass

class APIError(UIMMockAgentError):
    """Exception raised for API-related errors"""
    pass

class InputError(UIMMockAgentError):
    """Exception raised for invalid input errors"""
    pass

def handle_http_error(e: requests.RequestException) -> str:
    """Handle HTTP errors and return user-friendly error messages"""
    status_code = e.response.status_code if e.response else None
    if status_code == 400:
        return "Bad request. Please check your input and try again."
    elif status_code == 401:
        return "Unauthorized. Please check your credentials and try again."
    elif status_code == 403:
        return "Forbidden. You don't have permission to access this resource."
    elif status_code == 404:
        return "Resource not found. Please check the URL and try again."
    elif status_code == 429:
        return "Too many requests. Please wait and try again later."
    elif status_code == 500:
        return "Internal server error. Please try again later or contact support."
    elif status_code == 503:
        return "Service unavailable. Please try again later."
    else:
        return f"An error occurred: {str(e)}"

def handle_error(e: Exception) -> str:
    """Handle various types of errors and return user-friendly error messages"""
    if isinstance(e, requests.RequestException):
        return handle_http_error(e)
    elif isinstance(e, NetworkError):
        return "A network error occurred. Please check your internet connection and try again."
    elif isinstance(e, APIError):
        return "An API error occurred. Please try again later or contact support."
    elif isinstance(e, InputError):
        return f"Invalid input: {str(e)}"
    else:
        return f"An unexpected error occurred: {str(e)}"```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/intent_execution.py
```
Path: uim-mock-agent/src/intent_execution.py
Size: 2.18 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import requests
from typing import Dict, Any
from error_handling import NetworkError, APIError

MOCK_SERVICE_URL = "http://localhost:4000"

def execute_intent(intent_uid: str, params: Dict[str, Any], execute_endpoint: str, pat: str) -> Dict[str, Any]:
    """
    Execute an intent with the given parameters and PAT.

    Args:
        intent_uid (str): The UID of the intent to execute.
        params (Dict[str, Any]): The parameters for the intent.
        execute_endpoint (str): The endpoint for executing the intent.
        pat (str): Personal Access Token for authentication.

    Returns:
        Dict[str, Any]: The result of the intent execution.
    """
    print(f"Debug: Intent UID: {intent_uid}")
    print(f"Debug: Parameters: {params}")
    print(f"Debug: Execute Endpoint: {execute_endpoint}")

    url = execute_endpoint
    print(f"Debug: Constructed URL: {url}")

    payload = {
        "intent_uid": intent_uid,
        "parameters": params
    }
    print(f"Debug: Payload: {payload}")

    headers = {
        "Authorization": f"Bearer {pat}",
        "Content-Type": "application/json"
    }
    print(f"Debug: Headers: {headers}")

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error executing intent: {str(e)}")

def get_intent_params(intent_uid: str) -> Dict[str, Any]:
    """
    Get the required parameters for an intent.

    Args:
        intent_uid (str): The UID of the intent.

    Returns:
        Dict[str, Any]: The required parameters for the intent.
    """
    url = f"{MOCK_SERVICE_URL}/agents.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        agents_data = response.json()
        for intent in agents_data.get("intents", []):
            if intent.get("intent_uid") == intent_uid:
                return intent.get("input_parameters", {})
        return {}
    except requests.RequestException as e:
        raise NetworkError(f"Error fetching intent parameters: {str(e)}")
    except ValueError as e:
        raise APIError(f"Error parsing intent parameters: {str(e)}")```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/key_management.py
```
Path: uim-mock-agent/src/key_management.py
Size: 2.61 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def generate_key_pair(service_url):
    try:
        # Generate a new RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Create the directory structure
        key_dir = os.path.join('keys', service_url.replace('://', '_').replace(':', '_'))
        os.makedirs(key_dir, exist_ok=True)

        # Serialize and save the private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(os.path.join(key_dir, 'private_key.pem'), 'wb') as f:
            f.write(private_pem)

        # Serialize and save the public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(os.path.join(key_dir, 'public_key.pem'), 'wb') as f:
            f.write(public_pem)
        print(f"Key pair generated and saved for service URL: {service_url}")
    except Exception as e:
        print(f"Error generating key pair for service URL {service_url}: {e}")
        raise

def get_key_pair(service_url):
    try:
        key_dir = os.path.join('keys', service_url.replace('://', '_').replace(':', '_'))
        private_key_path = os.path.join(key_dir, 'private_key.pem')
        public_key_path = os.path.join(key_dir, 'public_key.pem')

        if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
            print(f"Key pair not found for service URL {service_url}, generating new key pair.")
            generate_key_pair(service_url)

        with open(private_key_path, 'rb') as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        with open(public_key_path, 'rb') as f:
            public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

        print(f"Key pair loaded for service URL: {service_url}")
        return private_key, public_key
    except Exception as e:
        print(f"Error loading key pair for service URL {service_url}: {e}")
        raise```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/pat_issuance.py
```
Path: uim-mock-agent/src/pat_issuance.py
Size: 1.10 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
from typing import Dict, Any
from cryptography.hazmat.primitives import serialization
import requests
import base64
from error_handling import NetworkError
from key_management import get_key_pair

def handle_pat_issuance(signed_policy: str, agent_id: str) -> Dict:
    private_key, public_key = get_key_pair("http://localhost:4000")
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key_base64url = base64.urlsafe_b64encode(public_key_pem).decode('utf-8')
    
    payload = { "signed_policy": signed_policy, "agent_id": agent_id, "agent_public_key": public_key_base64url}
    headers = {
        "Content-Type": "application/json"
    }
    try:
        print(f"Submitting signed policy for verification and PAT issuance: {payload}")
        response = requests.post("http://localhost:4000/pat/issue", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error executing intent: {str(e)}")
```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/policy_management.py
```
Path: uim-mock-agent/src/policy_management.py
Size: 2.70 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import requests
from error_handling import NetworkError, APIError
from policy_signing import sign_policy, submit_signed_policy_and_get_pat

MOCK_SERVICE_URL = "http://localhost:4000"
POLICY_ENDPOINT = f"{MOCK_SERVICE_URL}/uim-policy.json"

def fetch_policy():
    try:
        response = requests.get(POLICY_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise NetworkError(f"Error fetching policy: {str(e)}")
    except ValueError as e:
        raise APIError(f"Error parsing policy JSON: {str(e)}")

def display_policy(policy):
    print("\nODRL Policy:")
    print(f"Context: {policy.get('@context')}")
    print(f"Type: {policy.get('@type')}")
    print(f"ID: {policy.get('@id')}")
    print(f"Profile: {policy.get('profile')}")

    print("\nPermissions:")
    for permission in policy.get('permission', []):
        print(f"- Target: {permission.get('target')}")
        print(f"  Action: {permission.get('action', {}).get('id')}")
        for refinement in permission.get('action', {}).get('refinement', []):
            print(f"    Refinement: {refinement.get('leftOperand')} {refinement.get('operator')} {refinement.get('rightOperand')} {refinement.get('unit')}")

    print("\nProhibitions:")
    for prohibition in policy.get('prohibition', []):
        print(f"- Targets: {', '.join(prohibition.get('target', []))}")
        print(f"  Action: {prohibition.get('action', {}).get('id')}")
        for refinement in prohibition.get('action', {}).get('refinement', []):
            print(f"    Refinement: {refinement.get('leftOperand')} {refinement.get('operator')} {refinement.get('rightOperand')} {refinement.get('unit')}")

    print("\nParties:")
    for party in policy.get('party', []):
        print(f"- Function: {party.get('function')}")
        print(f"  Identifier: {party.get('identifier')}")

    print("\nAssets:")
    for asset in policy.get('asset', []):
        print(f"- ID: {asset.get('id')}")
        print(f"  Type: {asset.get('type')}")

def process_policy():
    try:
        policy = fetch_policy()
        display_policy(policy)

        signed_policy = sign_policy(policy)
        print(f"\nSigned Policy: {signed_policy}")

        pat_result = submit_signed_policy_and_get_pat(signed_policy)
        if "pat" in pat_result:
            print(f"\nPAT Issuance Result: Success")
            print(f"Personal Access Token: {pat_result['pat']}")
        else:
            print(f"\nPAT Issuance Result: Failed")
            print(f"Error: {pat_result.get('error', 'Unknown error')}")

        return pat_result
    except (NetworkError, APIError) as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    process_policy()```

--------------------------------------------------------------------------------

### File: uim-mock-agent/src/policy_signing.py
```
Path: uim-mock-agent/src/policy_signing.py
Size: 1.87 KB
Last Modified: 2024-09-12 19:39:32
```

**Contents:**
```
import jwt
from typing import Dict
from error_handling import APIError
from cryptography.hazmat.primitives import serialization
from pat_issuance import handle_pat_issuance
from key_management import get_key_pair

MOCK_SERVICE_URL = "http://localhost:4000"
POLICY_VERIFICATION_ENDPOINT = f"{MOCK_SERVICE_URL}/pat/issue"

def sign_policy(policy: Dict, service_url: str) -> str:
    """
    Sign the policy using the AI agent's private key.

    Args:
        policy (Dict): The policy to be signed
        service_url (str): The URL of the service to get the key pair for

    Returns:
        str: The signed policy as a JWS token
    """
    try:
        private_key, _ = get_key_pair(service_url)
        jws_token = jwt.encode(policy, private_key, algorithm="RS256")
        return jws_token
    except Exception as e:
        raise APIError(f"Error signing policy: {str(e)}")

def submit_signed_policy_and_get_pat(signed_policy: str, service_url: str) -> Dict:
    """
    Submit the signed policy for verification and PAT issuance.

    Args:
        signed_policy (str): The signed policy as a JWS token
        service_url (str): The URL of the service to get the key pair for

    Returns:
        Dict: The response containing the PAT
    """
    try:
        agent_id = "ai-agent-1"  # This should be a unique identifier for your AI agent
        _, public_key = get_key_pair(service_url)
        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

        result = handle_pat_issuance(signed_policy, agent_id, public_key_pem)

        if result["success"]:
            return {"pat": result["pat"]}
        else:
            raise APIError(f"Error issuing PAT: {result['error']}")
    except Exception as e:
        raise APIError(f"Error in PAT issuance process: {str(e)}")```

--------------------------------------------------------------------------------

