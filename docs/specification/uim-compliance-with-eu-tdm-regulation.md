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
