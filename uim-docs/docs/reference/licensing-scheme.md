# UIM Licensing Scheme

The Unified Intent Mediator (UIM) Protocol includes a comprehensive licensing scheme that defines permissions, conditions, and prohibitions for data and services. This page provides a detailed reference for the UIM Licensing Scheme.

## Introduction

The **UIM Licensing Scheme** is a critical component of the UIM Protocol that standardizes how web services express usage policies for their data and functionality. Inspired by Creative Commons (CC) licenses and Responsible AI Licenses (RAIL), it provides a flexible framework for defining permissions, conditions, and prohibitions.

Unlike the ODRL-based policy system (which is covered in the [ODRL Vocabulary](odrl-vocabulary.md) section), the UIM Licensing Scheme offers a simpler, more standardized approach to licensing that is specifically tailored for AI agent interactions.

## Key Features

### 1. Modular License Elements

The UIM Licensing Scheme uses a modular approach with three types of license elements:

- **Permissions**: What users are allowed to do with the content
- **Conditions**: Requirements that must be met when using the content
- **Prohibitions**: Actions that are not allowed

These elements can be combined to create licenses that meet specific needs, similar to how Creative Commons licenses work.

### 2. Artifact Type Specification (DAMPS)

The UIM Licensing Scheme uses the **DAMPS** convention to specify which artifacts the license applies to:

- **D**: **Data**
- **A**: **Applications/Binaries/Services**
- **M**: **Model Architectures**
- **P**: **Parameters (Trained Weights)**
- **S**: **Source Code**

This expansion from the traditional DAMS convention adds "Parameters" as a separate category, allowing for more granular control over how model weights can be used compared to model architectures.

### 3. License Naming Convention

Licenses follow a structured naming convention:

```
[Open-][Artifact Type(s)-]UIM-[License Elements]-v[Version Number]
```

For example:
- `D-UIM-BY-NC-v1.0`: A license for data that requires attribution and prohibits commercial use
- `Open-S-UIM-BY-SA-v1.0`: An open license for source code that requires attribution and share-alike conditions

### 4. Three Formats

Each UIM license is available in three formats:

1. **Human-Readable**: A plain language summary of the license terms
2. **Lawyer-Readable**: Detailed legal terms and conditions
3. **Machine-Readable**: JSON-LD format aligned with schema.org for automated processing

## License Elements

### Permissions

Permissions specify what users are allowed to do with the licensed content:

| Permission | Description |
|------------|-------------|
| **Access** | Permission to access the content or service |
| **Reproduce** | Copy or replicate content |
| **Distribute** | Share content with others |
| **Modify** | Adapt, remix, transform, or build upon content |
| **Commercial Use** | Use content for commercial purposes |
| **NonCommercial Use** | Use content for non-commercial purposes |
| **Data Mining** | Use content for text and data mining |
| **Model Training** | Use content to train AI models |
| **Indexing** | Access and reproduce content solely for indexing and providing search results |

### Conditions

Conditions specify requirements that must be met when using the licensed content:

| Condition | Description |
|-----------|-------------|
| **Attribution (BY)** | Must give appropriate credit |
| **ShareAlike (SA)** | Derivative works must be licensed under identical terms |
| **NonCommercial (NC)** | Commercial use is prohibited |
| **NoDerivatives (ND)** | No modifications or adaptations allowed |
| **Ethical AI Use (EAU)** | Must comply with ethical guidelines, prohibiting harmful applications |
| **Indexing Only (IO)** | Access and reproduction are permitted solely for indexing and search purposes |
| **AI Output Attribution (AIATTR)** | AI systems must attribute outputs derived from the content back to the source |

### Prohibitions

Prohibitions specify actions that are not allowed:

| Prohibition | Description |
|-------------|-------------|
| **Harmful Use** | Prohibits use in applications causing harm (e.g., surveillance, discrimination) |
| **Reidentification** | Prohibits attempts to re-identify anonymized data |
| **Redistribution** | Prohibits unauthorized redistribution |
| **No Data Mining (NoDM)** | Prohibits the use of content for data mining |
| **No Model Training (NoMT)** | Prohibits the use of content for training AI models |
| **No Long-Term Storage (NoLTS)** | Prohibits storing content for long-term use |
| **Bypass Access Controls Prohibited (BACP)** | Prohibits bypassing paywalls or access restrictions |

## License Formats

### 1. Human-Readable Summary

The human-readable summary provides an easy-to-understand overview of the license terms. For example:

**UIM Attribution License (UIM-BY-v1.0)**

**You are free to:**
- Access, reproduce, distribute, modify, and use the work for any purpose, including commercial and non-commercial uses.

**Under the following conditions:**
- Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- Ethical AI Use: You must not use the work for harmful purposes.

**Prohibitions:**
- Harmful Use: Prohibited.

### 2. Lawyer-Readable Legal Code

The lawyer-readable legal code provides a detailed legal document specifying the license terms. For example:

**License Name**: UIM Attribution License Version 1.0 (UIM-BY-v1.0)

**1. Grant of Rights**
- Access, Reproduce, Distribute, Modify, Use: You are granted the rights to access, reproduce, distribute, modify, and use the Work for any purpose, including commercial uses.

**2. Conditions**
- Attribution (BY): You must give appropriate credit to the Licensor, provide a link to the license, and indicate if changes were made.
- Ethical AI Use (EAU): You must not use the Work for harmful purposes, including but not limited to violating human rights or privacy.

**3. Prohibitions**
- Harmful Use: You may not use the Work in any way that causes harm.

**4. Disclaimer**
- The Work is provided "as-is" without warranties of any kind.

### 3. Machine-Readable Code (JSON-LD)

The machine-readable code uses JSON-LD format aligned with schema.org to enable automated processing. For example:

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

## Standard UIM License Combinations

The UIM Licensing Scheme includes several standard license combinations that cover common use cases:

### 1. UIM Public Domain Dedication (UIM-PD-v1.0)

Places the work in the public domain with no restrictions.

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

### 2. UIM Attribution License (UIM-BY-v1.0)

Allows any use with attribution.

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

### 3. UIM Attribution-ShareAlike License (UIM-BY-SA-v1.0)

Allows any use with attribution, requiring derivative works to use the same license.

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

### 4. UIM Attribution-NonCommercial License (UIM-BY-NC-v1.0)

Allows non-commercial use with attribution.

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

### 5. UIM Attribution-NoDerivatives License (UIM-BY-ND-v1.0)

Allows use without modification, with attribution.

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

### 6. UIM Attribution-NonCommercial-ShareAlike License (UIM-BY-NC-SA-v1.0)

Allows non-commercial use with attribution, requiring derivative works to use the same license.

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

### 7. UIM Attribution-NonCommercial-NoDerivatives License (UIM-BY-NC-ND-v1.0)

Allows non-commercial use without modification, with attribution.

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

### 8. UIM Attribution with AI Output Attribution License (UIM-BY-AIATTR-v1.0)

Allows any use with attribution, requiring AI systems to attribute outputs derived from the content.

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

### 9. UIM Attribution-NoDerivatives Indexing License (UIM-BY-ND-IO-NoDM-NoMT-v1.0)

Allows access and indexing only, with attribution.

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

### 10. UIM Attribution-NoDerivatives Dynamic Content License (UIM-BY-ND-NoMT-NoLTS-v1.0)

Allows access and distribution without modification, prohibiting model training and long-term storage.

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

## Open-Prefixed Licenses

Licenses with the "Open-" prefix indicate that the artifact is offered at no charge and allows for free use, including modification and redistribution. For example:

### Open Data UIM Attribution License (Open-D-UIM-BY-v1.0)

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

## Differentiating Open-Prefixed Licenses from Public Domain Dedications

While both "Open-" prefixed licenses and public domain dedications (UIM-PD-v1.0, UIM-CC0-v1.0) promote openness, they differ in important ways:

1. **Conditions and Prohibitions**:
   - **Open-Prefixed Licenses**: May include conditions like Attribution and prohibitions like Harmful Use
   - **Public Domain Dedications**: Have no conditions or prohibitions

2. **Attribution Requirements**:
   - **Open-Prefixed Licenses**: Typically require attribution
   - **Public Domain Dedications**: Do not require attribution

3. **Legal Rights**:
   - **Open-Prefixed Licenses**: Some rights are reserved to ensure compliance with conditions
   - **Public Domain Dedications**: No rights are reserved; the work is placed entirely in the public domain

This differentiation allows licensors to choose the appropriate level of openness for their content while maintaining certain requirements when needed.
