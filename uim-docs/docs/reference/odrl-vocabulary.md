# ODRL Vocabulary

The UIM Protocol uses the Open Digital Rights Language (ODRL) Information Model 2.2 to define policies for AI agent-web service interactions. This page provides a reference for the ODRL vocabulary used in the UIM Protocol.

## Introduction to ODRL

The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model 2.2 is a W3C Recommendation and is used by the UIM Protocol to define policies for AI agent-web service interactions.

## ODRL Core Concepts

### Policy

A Policy is a set of rules that defines the permissions, prohibitions, and obligations for a particular asset or service. In the UIM Protocol, policies are used to define the terms under which AI agents can interact with web services.

```json
{
  "@context": "http://www.w3.org/ns/odrl.jsonld",
  "@type": "Set",
  "uid": "http://example.com/policy/12345",
  "profile": "http://example.com/profile/odrl-uim",
  "permission": [...],
  "prohibition": [...],
  "obligation": [...]
}
```

### Permission

A Permission is a rule that allows a particular action to be performed on an asset or service. In the UIM Protocol, permissions define what intents an AI agent can execute.

```json
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
```

### Prohibition

A Prohibition is a rule that forbids a particular action from being performed on an asset or service. In the UIM Protocol, prohibitions define what intents an AI agent cannot execute.

```json
{
  "target": "http://example.com/api/intents",
  "action": "exceedRateLimit"
}
```

### Obligation

An Obligation is a rule that requires a particular action to be performed on an asset or service. In the UIM Protocol, obligations define what an AI agent must do when executing intents.

```json
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
```

### Constraint

A Constraint is a condition that must be satisfied for a rule to be valid. In the UIM Protocol, constraints define limitations on intent execution, such as rate limits or time restrictions.

```json
{
  "leftOperand": "http://example.com/vocab/rateLimit",
  "operator": "lte",
  "rightOperand": 1000,
  "unit": "http://example.com/vocab/hour"
}
```

### Duty

A Duty is an obligation that must be fulfilled in order to exercise a permission. In the UIM Protocol, duties define what an AI agent must do to execute an intent, such as paying a fee.

```json
{
  "action": "pay",
  "target": "http://example.com/vocab/intentPrice",
  "amount": 0.01,
  "unit": "http://example.com/vocab/USD"
}
```

## UIM Protocol ODRL Extensions

The UIM Protocol extends the ODRL vocabulary with additional terms specific to AI agent-web service interactions.

### Actions

| Action | Description |
|--------|-------------|
| execute | Execute an intent |
| exceedRateLimit | Exceed the rate limit |
| pay | Pay for intent execution |
| signPayload | Sign a payload with a private key |
| logUsage | Log usage information |
| provideAttribution | Provide attribution to the service |

### Operators

| Operator | Description |
|----------|-------------|
| eq | Equal to |
| neq | Not equal to |
| gt | Greater than |
| gte | Greater than or equal to |
| lt | Less than |
| lte | Less than or equal to |
| use | Use a specific value |

### Left Operands

| Left Operand | Description |
|--------------|-------------|
| rateLimit | Rate limit for intent execution |
| timeWindow | Time window for intent execution |
| publicKey | Public key for signature verification |
| intentPrice | Price for intent execution |
| dataRetention | Data retention period |
| dataUsage | Data usage restrictions |

### Units

| Unit | Description |
|------|-------------|
| second | Second |
| minute | Minute |
| hour | Hour |
| day | Day |
| week | Week |
| month | Month |
| year | Year |
| USD | US Dollar |
| EUR | Euro |
| GBP | British Pound |
| JPY | Japanese Yen |

## Example UIM Protocol Policy

Here's an example of a UIM Protocol policy using the ODRL vocabulary:

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
  ]
}
```

## References

- [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
- [ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)
- [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)
