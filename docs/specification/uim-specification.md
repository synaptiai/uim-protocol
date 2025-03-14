Network Working Group                                    D. Bentes
Request for Comments: DRAFT                                    UIM Protocol
Category: Standards Track                                      March 2024


                Unified Intent Mediator (UIM) Protocol
                     draft-uim-protocol-core-01

Status of this Memo

   This document specifies an Internet Standards Track protocol for the
   Internet community, and requests discussion and suggestions for
   improvements. Please refer to the current edition of the "Internet
   Official Protocol Standards" (STD 1) for the standardization state
   and status of this protocol. Distribution of this memo is unlimited.

Copyright Notice

   Copyright (C) The Internet Society (2024). All Rights Reserved.

Abstract

   This document specifies the Unified Intent Mediator (UIM) Protocol,
   which enables standardized interactions between AI agents and web
   services through intent-based communication. The protocol defines
   mechanisms for intent discovery, execution, and policy management.
   It addresses challenges in AI-web service integration by providing
   a unified framework for service discovery, policy enforcement, and
   secure interactions.

Table of Contents

   1.  Introduction ................................................
       1.1.  Problem Statement .....................................
       1.2.  Terminology ..........................................
       1.3.  Requirements Language ................................
   2.  Protocol Overview ..........................................
       2.1.  Architecture Models ..................................
       2.2.  Protocol Operation ...................................
   3.  Intent System .............................................
       3.1.  Intent Structure ....................................
       3.2.  Intent Identifiers ..................................
       3.3.  Intent Metadata .....................................
   4.  Discovery Mechanisms ......................................
       4.1.  DNS-Based Discovery .................................
       4.2.  Service Description Format ..........................
   5.  Policy Management ........................................
       5.1.  Policy Adherence Tokens ............................
       5.2.  Policy Expression ..................................
   6.  Protocol Messages ........................................
       6.1.  Message Format .....................................
       6.2.  Message Types ......................................
   7.  Security Considerations ..................................
   8.  IANA Considerations .....................................
   9.  References ..............................................
       9.1.  Normative References ...............................
       9.2.  Informative References ............................
   Appendix A.  Examples .......................................
   Appendix B.  Implementation Notes ...........................
   Authors' Addresses ..........................................

1.  Introduction

1.1.  Problem Statement

   Current methods of integration between AI agents and web services
   face several challenges:

   o  Integration methods are fragmented and use inconsistent APIs.

   o  Service discovery mechanisms are limited or non-existent.

   o  Policy enforcement and compliance requirements are complex.

   o  Access to advanced service features is often restricted.

   o  Security and authentication mechanisms vary widely.

   The UIM Protocol addresses these challenges by providing a
   standardized framework for intent-based interactions.

1.2.  Terminology

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
   document are to be interpreted as described in [RFC2119].

   Intent        An action that a web service can perform.

   Parameters    Required inputs for intent execution.

   Service       A web service that implements the UIM protocol.

   Endpoint      An API endpoint for intent execution.

   PAT           Policy Adherence Token, used for secure intent
                 execution.

   AI Agent      A service that interacts with web services using
                 intents.

1.3. Requirements Language

   The following terms are used within this specification:

   MUST        This word means that the item is an absolute requirement
               of the specification.

   SHOULD      This word means that there may exist valid reasons in
               particular circumstances to ignore this item, but the
               full implications must be understood and carefully
               weighed.

   MAY         This word means that an item is truly optional.

2. Protocol Overview

2.1. Architecture Models

   The UIM Protocol supports three architectural models:

   Centralized Model
      Uses a central repository for intent discovery and management.
      All service registrations and intent discoveries pass through
      a central authority.

   Decentralized Model
      Enables direct interaction between agents and services without
      intermediaries. Services maintain their own intent registries.

   Hybrid Model
      Combines centralized and decentralized approaches, allowing
      flexibility in deployment while maintaining consistency.

2.2. Protocol Operation

   The protocol operates through the following steps:

   1. Service Registration
      Services MUST register their intents and capabilities using one
      or more discovery mechanisms (Section 4). Registration includes
      intent definitions, endpoint information, and policy requirements.

   2. Intent Discovery
      AI agents discover available services and intents through:
      
      o  DNS-based discovery (Section 4.1)
      o  Service description retrieval (Section 4.2)
      o  Direct endpoint queries

   3. Policy Acquisition
      Before executing intents, AI agents MUST obtain Policy Adherence
      Tokens (PATs) by:

      o  Authenticating with the service
      o  Accepting applicable policies
      o  Receiving a signed PAT

   4. Intent Execution
      AI agents execute intents by:

      o  Preparing a valid request with required parameters
      o  Including a valid PAT
      o  Sending the request to the specified endpoint
      o  Processing the response according to intent metadata

3. Intent System

3.1. Intent Structure

   Each intent MUST include:

   Identifier       A unique identifier following the format specified
                   in Section 3.2.

   Name            A human-readable name describing the intent's
                   purpose.

   Description     A detailed explanation of the intent's functionality
                   and usage.

   Parameters      Input and output parameter definitions, including
                   types and constraints.

   Endpoint        Information required to execute the intent.

   Metadata        Additional intent properties as defined in
                   Section 3.3.

3.2. Intent Identifiers

   Intent identifiers MUST follow the format:

      namespace:intent-name:version

   Where:

   namespace    Identifies the service provider (e.g., "example.com")

   intent-name  Uniquely identifies the intent within the namespace
               using lowercase letters, numbers, and hyphens

   version     Semantic version number (e.g., "v1", "v2.1")

   Example:
      example.com:search-products:v1

3.3. Intent Metadata

   Intent metadata MUST use the following JSON structure:

   {
     "intent_uid": "example.com:search-products:v1",
     "intent_name": "SearchProducts",
     "description": "Search for products based on criteria",
     "input_parameters": [
       {
         "name": "query",
         "type": "string",
         "required": true,
         "description": "Search query string"
       }
     ],
     "output_parameters": [
       {
         "name": "products",
         "type": "array",
         "description": "List of matching products"
       }
     ],
     "endpoint": {
       "url": "https://api.example.com/products/search",
       "method": "POST",
       "content_type": "application/json"
     },
     "tags": [
       "e-commerce",
       "search",
       "products"
     ]
   }

4. Discovery Mechanisms

4.1. DNS-Based Discovery

   Services MUST publish discovery information using DNS TXT records.
   Each record MUST contain one of the following fields:

   uim-agents     URL of the service description file (REQUIRED)
                 Example: "uim-agents=https://example.com/agents.json"

   uim-discovery  URL of the discovery endpoint (OPTIONAL)
                 Example: "uim-discovery=https://api.example.com/discovery"

   uim-policy    URL of the policy file (REQUIRED)
                 Example: "uim-policy=https://example.com/policy.json"

   Example DNS TXT records:

      _uim.example.com. IN TXT "uim-agents=https://example.com/agents.json"
      _uim.example.com. IN TXT "uim-discovery=https://api.example.com/discovery"
      _uim.example.com. IN TXT "uim-policy=https://example.com/policy.json"

4.2. Service Description Format

   Service descriptions MUST use JSON format with the following structure:

   {
     "service": {
       "name": "Example Service",
       "description": "Service description",
       "version": "1.0.0",
       "urls": {
         "service": "https://api.example.com",
         "terms": "https://example.com/terms",
         "privacy": "https://example.com/privacy",
         "documentation": "https://example.com/docs"
       }
     },
     "intents": [
       {
         "uid": "example.com:intent-name:v1",
         "name": "IntentName",
         "description": "Intent description",
         "endpoint": {
           "url": "https://api.example.com/endpoint",
           "method": "POST"
         }
       }
     ],
     "security": {
       "public_key": "base64-encoded-public-key",
       "policy_url": "https://example.com/policy.json",
       "supported_auth_methods": [
         "jwt",
         "oauth2"
       ]
     },
     "compliance": {
       "standards": [
         "ISO27001",
         "GDPR"
       ],
       "certifications": [
         "SOC2"
       ]
     }
   }

5. Policy Management

5.1. Policy Adherence Tokens

   Policy Adherence Tokens (PATs) MUST be implemented as JSON Web
   Tokens [RFC7519] with the following claims:

   Required Claims:

   iss         Token issuer (the service identifier)

   sub         Subject (the AI agent identifier)

   exp         Expiration time

   nbf         Not before time

   jti         JWT ID (unique identifier for the token)

   scope       Array of permitted intents and operations

   Additional Claims:

   pol         Policy reference URL

   lmt         Rate limiting parameters

   Example PAT payload:

   {
     "iss": "example.com",
     "sub": "ai-agent-123",
     "exp": 1735689600,
     "nbf": 1704153600,
     "jti": "pat-xyz-789",
     "scope": [
       "example.com:search-products:v1:execute",
       "example.com:get-product:v1:read"
     ],
     "pol": "https://example.com/policy/standard",
     "lmt": {
       "rate": 100,
       "period": 3600
     }
   }

5.2. Policy Expression

   Policies MUST be expressed using JSON-LD format, incorporating
   the Open Digital Rights Language (ODRL) vocabulary [ODRL-VOCAB].
   Each policy document MUST include:

   o  Policy identifier
   o  Permission statements
   o  Prohibition statements
   o  Duty statements
   o  Constraint definitions

   Example policy document:

   {
     "@context": [
       "http://www.w3.org/ns/odrl.jsonld",
       "http://uimprotocol.org/ns/policy.jsonld"
     ],
     "@type": "Policy",
     "uid": "http://example.com/policy/standard",
     "profile": "http://uimprotocol.org/ns/policy",
     "permission": [{
       "target": "example.com:search-products:v1",
       "action": "execute",
       "constraint": [{
         "leftOperand": "rate",
         "operator": "lteq",
         "rightOperand": "100",
         "unit": "requests/hour"
       }]
     }],
     "prohibition": [{
       "target": "example.com:search-products:v1",
       "action": "execute",
       "constraint": [{
         "leftOperand": "timeRange",
         "operator": "outside",
         "rightOperand": {
           "start": "09:00:00Z",
           "end": "17:00:00Z"
         }
       }]
     }],
     "duty": [{
       "action": "compensate",
       "constraint": [{
         "leftOperand": "paymentAmount",
         "operator": "eq",
         "rightOperand": "0.001",
         "unit": "USD"
       }]
     }]
   }

6. Protocol Messages

6.1. Message Format

   All protocol messages MUST:

   o  Use HTTP/2 or later
   o  Use JSON format for request and response bodies
   o  Include appropriate content-type headers
   o  Include protocol version headers
   o  Support compression (gzip, deflate)

   Required Headers:

   Content-Type           application/json or application/uim+json
   Accept                 application/json or application/uim+json
   UIM-Version           Protocol version (e.g., "1.0")
   UIM-Request-ID        Unique request identifier

6.2. Message Types

6.2.1. Intent Discovery Messages

   Request:

      GET /api/intents/search HTTP/2
      Host: api.example.com
      Accept: application/json
      UIM-Version: 1.0
      UIM-Request-ID: req-123

   Parameters:

   query           Search term for intent discovery (OPTIONAL)
                  Example: "search products"

   service         Filter by service name (OPTIONAL)
                  Example: "example.com"

   tags            Array of tags to filter intents (OPTIONAL)
                  Example: ["e-commerce", "search"]

   Response:

      HTTP/2 200 OK
      Content-Type: application/json
      UIM-Version: 1.0
      UIM-Request-ID: req-123

      {
        "intents": [
          {
            "uid": "example.com:search-products:v1",
            "name": "SearchProducts",
            "description": "Search for products based on criteria",
            "endpoint": {
              "url": "https://api.example.com/products/search",
              "method": "POST"
            },
            "tags": [
              "e-commerce",
              "search",
              "products"
            ]
          }
        ],
        "total": 1,
        "page": 1,
        "per_page": 10
      }

6.2.2. Intent Execution Messages

   Request:

      POST /api/intents/execute HTTP/2
      Host: api.example.com
      Content-Type: application/json
      Accept: application/json
      Authorization: Bearer <PAT>
      UIM-Version: 1.0
      UIM-Request-ID: req-456

      {
        "intent": {
          "uid": "example.com:search-products:v1",
          "parameters": {
            "query": "laptop",
            "price_range": {
              "min": 1000,
              "max": 2000
            },
            "category": "electronics"
          }
        },
        "context": {
          "locale": "en-US",
          "currency": "USD",
          "timezone": "America/Los_Angeles"
        }
      }

   Success Response:

      HTTP/2 200 OK
      Content-Type: application/json
      UIM-Version: 1.0
      UIM-Request-ID: req-456

      {
        "status": "success",
        "data": {
          "products": [
            {
              "id": "prod-123",
              "name": "Professional Laptop",
              "price": {
                "amount": 1499.99,
                "currency": "USD"
              },
              "category": "electronics",
              "description": "High-performance laptop for professionals"
            }
          ],
          "total": 1,
          "page": 1,
          "per_page": 10
        },
        "meta": {
          "processing_time": 0.123,
          "rate_limit": {
            "remaining": 99,
            "reset": 3600
          }
        }
      }

   Error Response:

      HTTP/2 400 Bad Request
      Content-Type: application/json
      UIM-Version: 1.0
      UIM-Request-ID: req-456

      {
        "status": "error",
        "error": {
          "code": "INVALID_PARAMETERS",
          "message": "Invalid price range specified",
          "details": {
            "field": "price_range.max",
            "reason": "Must be greater than price_range.min"
          }
        }
      }

7. Security Considerations

   This section identifies security risks and their countermeasures.

7.1. Attack Vectors and Countermeasures

   The following attack vectors MUST be considered:

   1. Man-in-the-Middle Attacks
      Risk: Intercepting and modifying intent execution requests
      Countermeasures:
      o  Mandatory TLS 1.3 or later for all communications
      o  Certificate pinning for critical endpoints
      o  Request signing for sensitive operations

   2. Token Theft and Replay
      Risk: Unauthorized use of stolen PATs
      Countermeasures:
      o  Short PAT validity periods
      o  Token revocation mechanism
      o  Binding tokens to specific IP ranges
      o  Nonce-based replay protection

   3. Intent Injection
      Risk: Malicious intents registered in discovery system
      Countermeasures:
      o  Verified service registration
      o  Intent signature verification
      o  Regular security audits

   4. Denial of Service
      Risk: Overwhelming services with requests
      Countermeasures:
      o  Rate limiting at service and intent levels
      o  Request throttling
      o  Circuit breakers
      o  Load shedding mechanisms

7.2. Environmental Impact

   Security measures affect the operating environment:

   o  Additional latency from TLS handshakes
   o  Increased CPU usage for cryptographic operations
   o  Higher memory usage for token management
   o  Extra network traffic for security verifications

8. Scalability and Stability Considerations

8.1. Scalability Factors

   Implementations MUST consider:

   o  Number of concurrent AI agents
   o  Intent execution rate
   o  Discovery system capacity
   o  Token management overhead

8.2. Stability Measures

   To ensure stability:

   o  Implement graceful degradation
   o  Use circuit breakers for dependent services
   o  Monitor system health indicators
   o  Maintain redundant components

9. Protocol Management

9.1. Management Information Base (MIB)

   The UIM-MIB provides management of UIM protocol entities:

   uimMIB MODULE-IDENTITY
       LAST-UPDATED "202403140000Z"
       ORGANIZATION "UIM Protocol Working Group"
       CONTACT-INFO
           "Email: contact@uimprotocol.org"
       DESCRIPTION
           "The MIB module for managing UIM protocol entities"
       ::= { mib-2 XXX }  -- to be assigned by IANA

   [Complete MIB definition to be added]

9.2. Protocol Versioning

   Version changes MUST be tracked:

   o  Major version: Incompatible API changes
   o  Minor version: Backwards-compatible additions
   o  Patch version: Bug fixes

10. IANA Considerations

10.1. URI Schemes

   New URI schemes for UIM protocol:

   o  uim://          - UIM protocol
   o  uim+json://     - JSON-based UIM protocol

10.2. Media Types

   New media types:

   o  application/uim+json
      Required parameters: None
      Optional parameters: version
      Encoding considerations: UTF-8 only
      Security considerations: See Section 7
      Contact: IANA

   o  application/uim-pat+json
      [Similar details for PAT media type]

   o  application/uim-policy+json
      [Similar details for policy media type]

10.3. Service Name and Transport Protocol Port Number Registry

   Service Name: uim-discovery
   Transport Protocol: TCP
   Assignee: UIM Protocol Working Group
   Contact: IANA
   Description: UIM Discovery Service
   Reference: This document
   Port Number: TBD

11. Change Log

11.1. Changes from Previous Versions

   Version 1.0.0 to 1.1.0:
   o  Added detailed security considerations
   o  Enhanced scalability measures
   o  Introduced MIB definition
   o  Updated IANA considerations

11.2. Version History

   o  1.0.0 (2024-01): Initial release
   o  1.1.0 (2024-03): Current version

Appendix A. Examples

A.1. Basic Intent Discovery

   The following examples demonstrate the basic intent discovery process
   using DNS TXT records and HTTP requests.

   1. DNS TXT Record Query

      $ dig +short TXT _uim.example.com
      "uim-agents=https://example.com/agents.json"
      "uim-discovery=https://api.example.com/discovery"
      "uim-policy=https://example.com/policy.json"

   2. Retrieving Service Description

      GET /agents.json HTTP/2
      Host: example.com
      Accept: application/json

      Response:
      {
        "service": {
          "name": "Example E-commerce Service",
          "description": "Product search and ordering service",
          "version": "1.0.0",
          "urls": {
            "service": "https://api.example.com",
            "terms": "https://example.com/terms",
            "privacy": "https://example.com/privacy",
            "documentation": "https://example.com/docs"
          }
        },
        "intents": [
          {
            "uid": "example.com:searchProducts:v1",
            "name": "SearchProducts",
            "description": "Search for products based on criteria",
            "endpoint": {
              "url": "https://api.example.com/products/search",
              "method": "POST"
            }
          },
          {
            "uid": "example.com:getProduct:v1",
            "name": "GetProduct",
            "description": "Get detailed product information",
            "endpoint": {
              "url": "https://api.example.com/products/get",
              "method": "GET"
            }
          }
        ],
        "security": {
          "public_key": "-----BEGIN PUBLIC KEY-----\n...",
          "policy_url": "https://example.com/uim-policy.json",
          "supported_auth_methods": [
            "jwt"
          ]
        },
        "compliance": {
          "standards": [
            "ISO27001",
            "GDPR"
          ],
          "certifications": [
            "SOC2"
          ]
        }
      }

   3. Intent Discovery Request

      GET /api/intents/search?query=product&tags=e-commerce HTTP/2
      Host: api.example.com
      Accept: application/json

      Response:
      {
        "intents": [
          {
            "uid": "example.com:searchProducts:v1",
            "name": "SearchProducts",
            "description": "Search for products based on criteria",
            "endpoint": {
              "url": "https://api.example.com/products/search",
              "method": "POST"
            },
            "tags": ["e-commerce", "search", "products"]
          }
        ],
        "total": 1
      }

A.2. Intent Execution

   The following examples demonstrate intent execution with PATs.

   1. Obtaining a PAT

      POST /api/policy/pat HTTP/2
      Host: api.example.com
      Content-Type: application/json
      Accept: application/json

      {
        "agent_id": "ai-agent-123",
        "policy_reference": "https://example.com/policy/standard",
        "billing_info": {
          "payment_method": "credit_card",
          "billing_address": "123 Main St, City, Country",
          "currency": "USD"
        }
      }

      Response:
      {
        "pat": {
          "iss": "example.com",
          "sub": "ai-agent-123",
          "exp": 1735689600,
          "nbf": 1704153600,
          "jti": "pat-xyz-789",
          "scope": [
            "example.com:searchProducts:v1:execute",
            "example.com:getProduct:v1:read"
          ],
          "pol": "https://example.com/policy/standard",
          "lmt": {
            "rate": 100,
            "period": 3600
          }
        },
        "signature": "..."
      }

   2. Executing an Intent

      POST /api/intents/execute HTTP/2
      Host: api.example.com
      Content-Type: application/json
      Accept: application/json
      Authorization: Bearer <PAT>

      {
        "intent_uid": "example.com:searchProducts:v1",
        "parameters": {
          "query": "laptop",
          "price_range": "1000-2000",
          "category": "electronics"
        }
      }

      Response:
      {
        "status": "success",
        "data": {
          "products": [
            {
              "id": "prod-123",
              "name": "Professional Laptop",
              "price": 1499.99,
              "category": "electronics",
              "description": "High-performance laptop for professionals"
            }
          ],
          "total": 1
        }
      }

Appendix B. Implementation Notes

B.1. Best Practices

   This section provides detailed implementation best practices for both
   service providers and AI agents.

   1. Intent Design

      o  Use clear, descriptive intent names
      o  Follow semantic versioning (MAJOR.MINOR.PATCH)
      o  Document all parameters thoroughly
      o  Provide example requests and responses
      o  Include comprehensive error documentation

   2. Security Implementation

      o  Rotate encryption keys regularly (90 days recommended)
      o  Implement token revocation mechanisms
      o  Use strong cryptographic algorithms
      o  Monitor for suspicious activity
      o  Implement request signing for sensitive operations

   3. Performance Optimization

      o  Cache DNS TXT records appropriately
      o  Implement connection pooling
      o  Use HTTP/2 server push when appropriate
      o  Compress responses using content encoding
      o  Implement efficient rate limiting

   4. Error Handling

      o  Provide detailed error messages
      o  Implement retry mechanisms with exponential backoff
      o  Use appropriate HTTP status codes
      o  Include error reference numbers
      o  Log errors comprehensively

B.2. Migration Guidelines

   This section provides guidelines for migrating existing services to
   the UIM protocol.

   1. Preparation Phase

      o  Audit existing API endpoints
      o  Map current functionality to intents
      o  Design intent hierarchy
      o  Plan security implementation
      o  Prepare documentation

   2. Implementation Phase

      o  Deploy discovery mechanism
      o  Implement intent endpoints
      o  Set up policy management
      o  Configure monitoring
      o  Test thoroughly

   3. Deployment Phase

      o  Roll out gradually
      o  Monitor performance
      o  Gather feedback
      o  Optimize based on usage
      o  Update documentation

B.3. Testing Guidelines

   This section outlines recommended testing procedures for UIM protocol
   implementations.

   1. Functional Testing

      o  Verify intent discovery
      o  Test parameter validation
      o  Check error handling
      o  Validate response formats
      o  Test version compatibility

   2. Security Testing

      o  Verify PAT validation
      o  Test rate limiting
      o  Check access controls
      o  Validate encryption
      o  Test token revocation

   3. Performance Testing

      o  Measure response times
      o  Test under load
      o  Verify scalability
      o  Check resource usage
      o  Test concurrent requests

Appendix C. Protocol Operation Examples

C.1. Normal Operation

   [Sequence diagram and explanation of normal operation]

C.2. Error Handling

   1. Invalid Intent Request
      [Example of error response and recovery]

   2. Token Expiration
      [Example of token renewal process]

   3. Service Unavailability
      [Example of fallback behavior]

Appendix D. Internationalization Considerations

D.1. Character Encoding

   All text fields MUST use UTF-8 encoding.

D.2. Language Tags

   Language preferences MUST use BCP 47 language tags.

D.3. Localization

   Services SHOULD support multiple languages through:

   o  Intent descriptions in multiple languages
   o  Localized error messages
   o  Language-specific content negotiation

Authors' Addresses

   Daniel Bentes
   UIM Protocol
   123 Innovation Drive
   San Francisco, CA 94105
   United States of America

   Phone: +1 415 555 0123
   Email: daniel.bentes@uimprotocol.org
   URI:   https://uimprotocol.org

Full Copyright Statement

   Copyright (C) The Internet Society (2024).  All Rights Reserved.

   This document and translations of it may be copied and furnished to
   others, and derivative works that comment on or otherwise explain it
   or assist in its implementation may be prepared, copied, published
   and distributed, in whole or in part, without restriction of any
   kind, provided that the above copyright notice and this paragraph are
   included on all such copies and derivative works.  However, this
   document itself may not be modified in any way, such as by removing
   the copyright notice or references to the Internet Society or other
   Internet organizations, except as needed for the purpose of
   developing Internet standards in which case the procedures for
   copyrights defined in the Internet Standards process must be
   followed, or as required to translate it into languages other than
   English.

   The limited permissions granted above are perpetual and will not be
   revoked by the Internet Society or its successors or assigns.

   This document and the information contained herein is provided on an
   "AS IS" basis and THE INTERNET SOCIETY AND THE INTERNET ENGINEERING
   TASK FORCE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING
   BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION
   HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF
   MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. 