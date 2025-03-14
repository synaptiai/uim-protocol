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
