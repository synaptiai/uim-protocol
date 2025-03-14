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

- **Provide Tooling Support:** Develop tools and libraries to assist in creating, parsing, and enforcing ODRL policies using this vocabulary.