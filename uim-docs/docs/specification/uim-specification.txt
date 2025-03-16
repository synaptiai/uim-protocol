Network Working Group                                    D. Bentes
Internet-Draft                                            UIM Protocol
Intended Status: Standards Track                             March 2025
Expires: September 2025


                                                        uimprotocol.com
                                  https://github.com/synaptiai/uim-protocol


                Unified Intent Mediator (UIM) Protocol
                     draft-uim-protocol-core-01

Status of this Memo

   This document is an Internet-Draft and is in full conformance with all
   provisions of Section 10 of RFC 7841.

   Internet-Drafts are working documents of the Internet Engineering Task
   Force (IETF). Note that other groups may also distribute working
   documents as Internet-Drafts. The list of current Internet-Drafts is
   at https://datatracker.ietf.org/drafts/current/.

   Internet-Drafts are draft documents valid for a maximum of six months
   and may be updated, replaced, or obsoleted by other documents at any
   time. It is inappropriate to use Internet-Drafts as reference material
   or to cite them other than as "work in progress."

   This Internet-Draft will expire on September 15, 2025.

Copyright Notice

   Copyright (c) 2025 IETF Trust and the persons identified as the
   document authors. All rights reserved.

   This document is subject to BCP 78 and the IETF Trust's Legal
   Provisions Relating to IETF Documents
   (https://trustee.ietf.org/license-info) in effect on the date of
   publication of this document. Please review these documents carefully,
   as they describe your rights and restrictions with respect to this
   document.

Abstract

   This document specifies the Unified Intent Mediator (UIM) Protocol,
   which enables standardized interactions between AI agents and web
   services through intent-based communication. The protocol defines
   mechanisms for intent discovery, execution, and policy management.
   It addresses challenges in AI-web service integration by providing
   a unified framework for service discovery, policy enforcement, and
   secure interactions.

Table of Contents

   1.  Introduction ................................................ 3
       1.1.  Problem Statement ..................................... 3
       1.2.  Terminology .......................................... 3
       1.3.  Requirements Language ................................ 4
   2.  Protocol Overview .......................................... 4
       2.1.  Architecture Models .................................. 4
       2.2.  Protocol Operation ................................... 5
   3.  Intent System ............................................. 6
       3.1.  Intent Structure .................................... 6
       3.2.  Intent Identifiers .................................. 6
       3.3.  Intent Metadata ..................................... 7
   4.  Discovery Mechanisms ...................................... 8
       4.1.  DNS-Based Discovery ................................. 8
       4.2.  Service Description Format .......................... 9
   5.  Policy Management ........................................ 10
       5.1.  Policy Adherence Tokens ............................ 10
       5.2.  Policy Expression .................................. 11
   6.  Protocol Messages ........................................ 12
       6.1.  Message Format ..................................... 12
       6.2.  Message Types ...................................... 13
   7.  Security Considerations .................................. 15
       7.1.  Attack Vectors and Countermeasures ................. 15
       7.2.  Environmental Impact ............................... 16
       7.3.  Implementation Vulnerabilities ..................... 16
       7.4.  Operational Security Considerations ................ 17
   8.  Scalability and Stability Considerations ................. 18
       8.1.  Scalability Factors ............................... 18
       8.2.  Stability Measures ................................ 18
   9.  Protocol Management ...................................... 19
       9.1.  Management Information Base (MIB) .................. 19
       9.2.  Protocol Versioning ............................... 19
   10. IANA Considerations ..................................... 20
       10.1. URI Schemes ....................................... 20
       10.2. Media Types ....................................... 20
       10.3. Service Name and Transport Protocol Port Number .... 21
   11. Change Log .............................................. 21
       11.1. Changes from Previous Versions .................... 21
       11.2. Version History ................................... 21
   12. References .............................................. 22
       12.1. Normative References .............................. 22
       12.2. Informative References ............................ 22
   Appendix A.  Examples ....................................... 23
   Appendix B.  Implementation Notes ........................... 25
   Appendix C.  Protocol Operation Examples .................... 28
   Appendix D.  Internationalization Considerations ............ 29
   Authors' Addresses .......................................... 30
   Full Copyright Statement .................................... 31

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
      uimprotocol.com:search-products:v1

3.3. Intent Metadata

   Intent metadata MUST use the following JSON structure:

   {
     "intent_uid": "uimprotocol.com:search-products:v1",
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
       "url": "https://api.uimprotocol.com/products/search",
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
                 Example: "uim-agents=https://uimprotocol.com/agents.json"

   uim-discovery  URL of the discovery endpoint (OPTIONAL)
                 Example: "uim-discovery=https://api.uimprotocol.com/discovery"

   uim-policy    URL of the policy file (REQUIRED)
                 Example: "uim-policy=https://uimprotocol.com/policy.json"

   Example DNS TXT records:

      _uim.uimprotocol.com. IN TXT "uim-agents=https://uimprotocol.com/agents.json"
      _uim.uimprotocol.com. IN TXT "uim-discovery=https://api.uimprotocol.com/discovery"
      _uim.uimprotocol.com. IN TXT "uim-policy=https://uimprotocol.com/policy.json"

4.2. Service Description Format

   Service descriptions MUST use JSON format with the following structure:

   {
     "service": {
       "name": "UIM Protocol Service",
       "description": "UIM Protocol reference implementation",
       "version": "1.0.0",
       "urls": {
         "service": "https://api.uimprotocol.com",
         "terms": "https://uimprotocol.com/terms",
         "privacy": "https://uimprotocol.com/privacy",
         "documentation": "https://uimprotocol.com/docs"
       }
     },
     "intents": [
       {
         "uid": "uimprotocol.com:intent-name:v1",
         "name": "IntentName",
         "description": "Intent description",
         "endpoint": {
           "url": "https://api.uimprotocol.com/endpoint",
           "method": "POST"
         }
       }
     ],
     "security": {
       "public_key": "base64-encoded-public-key",
       "policy_url": "https://uimprotocol.com/policy.json",
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
     "iss": "uimprotocol.com",
     "sub": "ai-agent-123",
     "exp": 1735689600,
     "nbf": 1704153600,
     "jti": "pat-xyz-789",
     "scope": [
       "uimprotocol.com:search-products:v1:execute",
       "uimprotocol.com:get-product:v1:read"
     ],
     "pol": "https://uimprotocol.com/policy/standard",
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
     "uid": "http://uimprotocol.com/policy/standard",
     "profile": "http://uimprotocol.org/ns/policy",
     "permission": [{
       "target": "uimprotocol.com:search-products:v1",
       "action": "execute",
       "constraint": [{
         "leftOperand": "rate",
         "operator": "lteq",
         "rightOperand": "100",
         "unit": "requests/hour"
       }]
     }],
     "prohibition": [{
       "target": "uimprotocol.com:search-products:v1",
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
      Host: api.uimprotocol.com
      Accept: application/json
      UIM-Version: 1.0
      UIM-Request-ID: req-123

   Parameters:

   query           Search term for intent discovery (OPTIONAL)
                  Example: "search products"

   service         Filter by service name (OPTIONAL)
                  Example: "uimprotocol.com"

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
            "uid": "uimprotocol.com:search-products:v1",
            "name": "SearchProducts",
            "description": "Search for products based on criteria",
            "endpoint": {
              "url": "https://api.uimprotocol.com/products/search",
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
      Host: api.uimprotocol.com
      Content-Type: application/json
      Accept: application/json
      Authorization: Bearer <PAT>
      UIM-Version: 1.0
      UIM-Request-ID: req-456

      {
        "intent": {
          "uid": "uimprotocol.com:search-products:v1",
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

7.3. Implementation Vulnerabilities

   Implementers MUST be aware of the following potential vulnerabilities:

   1. Token Validation Weaknesses
      Risk: Improper validation of PATs leading to unauthorized access
      Mitigation:
      o  Implement full JWT validation including signature, expiration,
         and claims validation
      o  Use established JWT libraries rather than custom implementations
      o  Validate all claims including issuer and audience

   2. Parameter Injection
      Risk: Injection attacks through intent parameters
      Mitigation:
      o  Implement strict parameter validation
      o  Use parameterized queries when accessing databases
      o  Apply context-specific escaping for all user inputs
      o  Validate parameter types, ranges, and formats

   3. Cryptographic Weaknesses
      Risk: Use of weak cryptographic algorithms or implementations
      Mitigation:
      o  Use only modern, strong cryptographic algorithms (e.g., ECDSA P-256)
      o  Implement proper key management procedures
      o  Rotate cryptographic keys regularly
      o  Follow cryptographic best practices from NIST or equivalent

   4. Information Disclosure
      Risk: Leaking sensitive information through error messages or logs
      Mitigation:
      o  Implement generic error messages for clients
      o  Log detailed errors only server-side
      o  Sanitize sensitive information in logs
      o  Implement proper access controls for logs and diagnostics

7.4. Operational Security Considerations

   Service providers and AI agents MUST implement the following operational
   security measures:

   1. Key Management
      o  Store private keys in hardware security modules (HSMs) when possible
      o  Implement proper key rotation procedures
      o  Use separate keys for different environments (development, testing,
         production)
      o  Establish secure key distribution mechanisms

   2. Monitoring and Alerting
      o  Implement real-time monitoring for suspicious activities
      o  Set up alerts for unusual patterns of intent execution
      o  Monitor for abnormal token usage patterns
      o  Establish incident response procedures

   3. Regular Security Assessments
      o  Conduct periodic security audits of implementations
      o  Perform penetration testing on critical components
      o  Review security configurations regularly
      o  Stay informed about security vulnerabilities in dependencies

   4. Secure Deployment
      o  Follow the principle of least privilege for all components
      o  Implement network segmentation
      o  Use container security best practices
      o  Keep all software components updated with security patches

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
       LAST-UPDATED "202503140000Z"
       ORGANIZATION "UIM Protocol Working Group"
       CONTACT-INFO
           "Email: contact@uimprotocol.org"
       DESCRIPTION
           "The MIB module for managing UIM protocol entities"
       ::= { mib-2 XXX }  -- to be assigned by IANA

   -- UIM Protocol Objects
   uimObjects OBJECT IDENTIFIER ::= { uimMIB 1 }

   -- UIM Protocol Statistics
   uimStats OBJECT IDENTIFIER ::= { uimMIB 2 }

   -- UIM Protocol Conformance
   uimConformance OBJECT IDENTIFIER ::= { uimMIB 3 }

   -- UIM Service Table
   uimServiceTable OBJECT-TYPE
       SYNTAX      SEQUENCE OF UimServiceEntry
       MAX-ACCESS  not-accessible
       STATUS      current
       DESCRIPTION
           "A table of UIM services registered in the system."
       ::= { uimObjects 1 }

   uimServiceEntry OBJECT-TYPE
       SYNTAX      UimServiceEntry
       MAX-ACCESS  not-accessible
       STATUS      current
       DESCRIPTION
           "An entry containing management information for a
            particular UIM service."
       INDEX       { uimServiceIndex }
       ::= { uimServiceTable 1 }

   UimServiceEntry ::= SEQUENCE {
       uimServiceIndex        Integer32,
       uimServiceName         DisplayString,
       uimServiceDescription  DisplayString,
       uimServiceVersion      DisplayString,
       uimServiceStatus       INTEGER,
       uimServiceUptime       TimeTicks,
       uimServiceLastUpdated  DateAndTime
   }

   -- UIM Intent Table
   uimIntentTable OBJECT-TYPE
       SYNTAX      SEQUENCE OF UimIntentEntry
       MAX-ACCESS  not-accessible
       STATUS      current
       DESCRIPTION
           "A table of intents provided by UIM services."
       ::= { uimObjects 2 }

   uimIntentEntry OBJECT-TYPE
       SYNTAX      UimIntentEntry
       MAX-ACCESS  not-accessible
       STATUS      current
       DESCRIPTION
           "An entry containing management information for a
            particular intent."
       INDEX       { uimServiceIndex, uimIntentIndex }
       ::= { uimIntentTable 1 }

   UimIntentEntry ::= SEQUENCE {
       uimIntentIndex         Integer32,
       uimIntentUID           DisplayString,
       uimIntentName          DisplayString,
       uimIntentDescription   DisplayString,
       uimIntentStatus        INTEGER,
       uimIntentExecutions    Counter64,
       uimIntentErrors        Counter64,
       uimIntentLastExecuted  DateAndTime
   }

   -- UIM Statistics
   uimStatsIntentExecutions OBJECT-TYPE
       SYNTAX      Counter64
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The total number of intent executions."
       ::= { uimStats 1 }

   uimStatsIntentErrors OBJECT-TYPE
       SYNTAX      Counter64
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The total number of intent execution errors."
       ::= { uimStats 2 }

   uimStatsActiveAgents OBJECT-TYPE
       SYNTAX      Gauge32
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The current number of active AI agents."
       ::= { uimStats 3 }

   uimStatsPATsIssued OBJECT-TYPE
       SYNTAX      Counter64
       MAX-ACCESS  read-only
       STATUS      current
       DESCRIPTION
           "The total number of PATs issued."
       ::= { uimStats 4 }

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
      Interoperability considerations: None
      Published specification: This document
      Applications that use this media type: UIM Protocol services and clients
      Fragment identifier considerations: Same as for application/json
      Additional information:
         Magic number(s): None
         File extension(s): .uim.json
         Macintosh file type code(s): None
      Person & email address to contact for further information: See Authors' Addresses
      Intended usage: COMMON
      Restrictions on usage: None
      Author: UIM Protocol Working Group
      Change controller: IETF
      Provisional registration: No

   o  application/uim-pat+json
      Required parameters: None
      Optional parameters: None
      Encoding considerations: UTF-8 only
      Security considerations: See Section 7
      Interoperability considerations: None
      Published specification: This document
      Applications that use this media type: UIM Protocol services and clients
      Fragment identifier considerations: Same as for application/json
      Additional information:
         Magic number(s): None
         File extension(s): .pat.json
         Macintosh file type code(s): None
      Person & email address to contact for further information: See Authors' Addresses
      Intended usage: COMMON
      Restrictions on usage: None
      Author: UIM Protocol Working Group
      Change controller: IETF
      Provisional registration: No

   o  application/uim-policy+json
      Required parameters: None
      Optional parameters: None
      Encoding considerations: UTF-8 only
      Security considerations: See Section 7
      Interoperability considerations: None
      Published specification: This document
      Applications that use this media type: UIM Protocol services and clients
      Fragment identifier considerations: Same as for application/json
      Additional information:
         Magic number(s): None
         File extension(s): .policy.json
         Macintosh file type code(s): None
      Person & email address to contact for further information: See Authors' Addresses
      Intended usage: COMMON
      Restrictions on usage: None
      Author: UIM Protocol Working Group
      Change controller: IETF
      Provisional registration: No

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

   o  1.0.0 (2024-09): Initial release
   o  1.1.0 (2025-03): Current version

12. References

12.1. Normative References

   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119,
              March 1997, <https://www.rfc-editor.org/info/rfc2119>.

   [RFC7519]  Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token
              (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015,
              <https://www.rfc-editor.org/info/rfc7519>.

12.2. Informative References

   [ODRL-VOCAB] Iannella, R., Villata, S., "ODRL Information Model 2.2",
                W3C Recommendation, February 2018,
                <https://www.w3.org/TR/odrl-model/>.

Appendix A. Examples

A.1. Basic Intent Discovery

   The following examples demonstrate the basic intent discovery process
   using DNS TXT records and HTTP requests.

   1. DNS TXT Record Query

      $ dig +short TXT _uim.uimprotocol.com
      "uim-agents=https://uimprotocol.com/agents.json"
      "uim-discovery=https://api.uimprotocol.com/discovery"
      "uim-policy=https://uimprotocol.com/policy.json"

   2. Retrieving Service Description

      GET /agents.json HTTP/2
      Host: uimprotocol.com
      Accept: application/json

      Response:
      {
        "service": {
          "name": "UIM E-commerce Service",
          "description": "Product search and ordering service",
          "version": "1.0.0",
          "urls": {
            "service": "https://api.uimprotocol.com",
            "terms": "https://uimprotocol.com/terms",
            "privacy": "https://uimprotocol.com/privacy",
            "documentation": "https://uimprotocol.com/docs"
          }
        },
        "intents": [
          {
            "uid": "uimprotocol.com:searchProducts:v1",
            "name": "SearchProducts",
            "description": "Search for products based on criteria",
            "endpoint": {
              "url": "https://api.uimprotocol.com/products/search",
              "method": "POST"
            }
          },
          {
            "uid": "uimprotocol.com:getProduct:v1",
            "name": "GetProduct",
            "description": "Get detailed product information",
            "endpoint": {
              "url": "https://api.uimprotocol.com/products/get",
              "method": "GET"
            }
          }
        ],
        "security": {
          "public_key": "-----BEGIN PUBLIC KEY-----\n...",
          "policy_url": "https://uimprotocol.com/uim-policy.json",
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
      Host: api.uimprotocol.com
      Accept: application/json

      Response:
      {
        "intents": [
          {
            "uid": "uimprotocol.com:searchProducts:v1",
            "name": "SearchProducts",
            "description": "Search for products based on criteria",
            "endpoint": {
              "url": "https://api.uimprotocol.com/products/search",
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
      Host: api.uimprotocol.com
      Content-Type: application/json
      Accept: application/json

      {
        "agent_id": "ai-agent-123",
        "policy_reference": "https://uimprotocol.com/policy/standard",
        "billing_info": {
          "payment_method": "credit_card",
          "billing_address": "123 Main St, City, Country",
          "currency": "USD"
        }
      }

      Response:
      {
        "pat": {
          "iss": "uimprotocol.com",
          "sub": "ai-agent-123",
          "exp": 1735689600,
          "nbf": 1704153600,
          "jti": "pat-xyz-789",
          "scope": [
            "uimprotocol.com:searchProducts:v1:execute",
            "uimprotocol.com:getProduct:v1:read"
          ],
          "pol": "https://uimprotocol.com/policy/standard",
          "lmt": {
            "rate": 100,
            "period": 3600
          }
        },
        "signature": "..."
      }

   2. Executing an Intent

      POST /api/intents/execute HTTP/2
      Host: api.uimprotocol.com
      Content-Type: application/json
      Accept: application/json
      Authorization: Bearer <PAT>

      {
        "intent_uid": "uimprotocol.com:searchProducts:v1",
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

   The following sequence diagram illustrates the normal operation flow
   of the UIM protocol:

   ```
   AI Agent                 Service                 Policy Server
      |                        |                         |
      |--- DNS Discovery ----->|                         |
      |<-- Service Description-|                         |
      |                        |                         |
      |----------------------->|-- Policy Request ------>|
      |                        |<-- Policy Document -----|
      |                        |                         |
      |-- PAT Request -------->|                         |
      |<-- PAT Response -------|                         |
      |                        |                         |
      |-- Intent Execution --->|                         |
      |<-- Intent Response ----|                         |
      |                        |                         |
   ```

   1. The AI agent performs DNS-based discovery to locate the service.
   2. The service returns its description, including available intents.
   3. The service requests policy information from the policy server.
   4. The policy server returns the policy document.
   5. The AI agent requests a Policy Adherence Token (PAT).
   6. The service validates the request and issues a PAT.
   7. The AI agent executes an intent, including the PAT.
   8. The service processes the intent and returns the response.

   This flow demonstrates the complete interaction cycle from discovery
   to intent execution, highlighting the role of policy management in
   the protocol.

C.2. Error Handling

   1. Invalid Intent Request

      ```
      AI Agent                 Service
         |                        |
         |-- Intent Execution --->|
         |                        |-- Validate Parameters --|
         |                        |-- Parameter Invalid ----|
         |<-- Error Response -----|
         |-- Corrected Request -->|
         |<-- Success Response ---|
         |                        |
      ```

      When an AI agent submits an intent with invalid parameters:
      
      a. The service validates the parameters and detects the issue.
      b. The service returns an error response with details about the invalid parameter.
      c. The AI agent corrects the parameter and resubmits the request.
      d. The service processes the corrected request and returns a success response.

   2. Token Expiration

      ```
      AI Agent                 Service
         |                        |
         |-- Intent Execution --->|
         |                        |-- Validate PAT ---------|
         |                        |-- PAT Expired ----------|
         |<-- 401 Unauthorized ---|
         |-- PAT Request -------->|
         |<-- New PAT ------------|
         |-- Intent Execution --->|
         |<-- Success Response ---|
         |                        |
      ```

      When a PAT expires:
      
      a. The AI agent attempts to execute an intent with an expired PAT.
      b. The service validates the PAT and detects that it has expired.
      c. The service returns a 401 Unauthorized response.
      d. The AI agent requests a new PAT.
      e. The service issues a new PAT.
      f. The AI agent retries the intent execution with the new PAT.
      g. The service processes the request and returns a success response.

   3. Service Unavailability

      ```
      AI Agent                 Service                 Fallback Service
         |                        |                         |
         |-- Intent Execution --->|                         |
         |                        |-- Service Unavailable --|
         |<-- 503 Service Unavailable                       |
         |                        |                         |
         |-- DNS Discovery ------------------------------>|
         |<-- Service Description ------------------------|
         |                                                |
         |-- PAT Request -------------------------------->|
         |<-- PAT Response -------------------------------|
         |                                                |
         |-- Intent Execution --------------------------->|
         |<-- Success Response ---------------------------|
         |                                                |
      ```

      When a service becomes unavailable:
      
      a. The AI agent attempts to execute an intent.
      b. The service is unavailable and returns a 503 Service Unavailable response.
      c. The AI agent performs discovery to locate an alternative service.
      d. The fallback service returns its description.
      e. The AI agent requests a PAT from the fallback service.
      f. The fallback service issues a PAT.
      g. The AI agent executes the intent on the fallback service.
      h. The fallback service processes the request and returns a success response.

   These error handling examples demonstrate how the protocol handles
   common failure scenarios, ensuring robust operation even when issues
   occur.

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
   UIM Protocol by Synapti.ai
   0057 Oslo
   Norway

   Email: daniel.bentes@synapti.ai
   URI:   https://uimprotocol.com

Full Copyright Statement

   Copyright (c) 2025 IETF Trust and the persons identified as the
   document authors. All rights reserved.

   This document is subject to BCP 78 and the IETF Trust's Legal
   Provisions Relating to IETF Documents
   (https://trustee.ietf.org/license-info) in effect on the date of
   publication of this document. Please review these documents carefully,
   as they describe your rights and restrictions with respect to this
   document.

   Code Components extracted from this document must include Simplified
   BSD License text as described in Section 4.e of the Trust Legal
   Provisions and are provided without warranty as described in the
   Simplified BSD License.
