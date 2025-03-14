# Testing Guide

This guide provides instructions for testing your UIM Protocol implementation. It covers testing tools, methodologies, and best practices.

## Overview

Testing is a critical part of implementing the UIM Protocol. It ensures that your implementation correctly follows the specification and can interoperate with other implementations. This guide will help you test your UIM Protocol implementation, whether you're developing an AI agent or a web service.

## Testing Tools

The UIM Protocol ecosystem provides several tools to help you test your implementation:

### UIM Protocol CLI

The UIM Protocol CLI is a command-line tool that allows you to interact with UIM-compatible web services. It can be used to:

- Discover services and intents
- Retrieve policies
- Request PATs
- Execute intents
- Validate responses

#### Installation

```bash
npm install -g uim-protocol-cli
```

#### Usage

```bash
# Discover a service
uim-cli discover --domain example.com

# Search for intents
uim-cli search-intents --service-url https://api.example.com --tags e-commerce,search

# Get a PAT
uim-cli get-pat --service-url https://api.example.com

# Execute an intent
uim-cli execute --service-url https://api.example.com --intent-uid example.com:searchProducts:v1 --parameters '{"query": "laptop", "category": "electronics"}'
```

### UIM Protocol Validator

The UIM Protocol Validator is a tool that validates your implementation against the specification. It can be used to:

- Validate intent definitions
- Validate policy definitions
- Validate PAT issuance
- Validate intent execution
- Validate error handling

#### Installation

```bash
npm install -g uim-protocol-validator
```

#### Usage

```bash
# Validate a service
uim-validator service --url https://api.example.com

# Validate an agent
uim-validator agent --agent-id my-agent
```

### Mock Implementations

The UIM Protocol provides mock implementations that you can use for testing:

- **[Mock Agent](../prototypes/mock-agent.md)**: A simulated AI agent that implements the UIM Protocol.
- **[Mock Webservice](../prototypes/mock-webservice.md)**: A simulated web service that implements the UIM Protocol.

These mock implementations can be used to test your own implementation without having to set up a complete environment.

## Testing Methodologies

### Unit Testing

Unit testing focuses on testing individual components of your implementation in isolation. For example:

- Testing the policy signing function
- Testing the intent discovery function
- Testing the PAT verification function

#### Example Unit Test (JavaScript)

```javascript
const { expect } = require('chai');
const { signPolicy } = require('../implementations/policy');

describe('Policy Signing', () => {
  it('should sign a policy correctly', () => {
    const policy = { /* policy object */ };
    const privateKey = '...';
    
    const signature = signPolicy(policy, privateKey);
    
    expect(signature).to.be.a('string');
    expect(signature.length).to.be.greaterThan(0);
  });
});
```

### Integration Testing

Integration testing focuses on testing the interaction between different components of your implementation. For example:

- Testing the flow from policy retrieval to PAT acquisition
- Testing the flow from intent discovery to intent execution
- Testing error handling across components

#### Example Integration Test (JavaScript)

```javascript
const { expect } = require('chai');
const { UIMAgent } = require('../implementations/agent');

describe('Intent Execution Flow', () => {
  it('should execute an intent successfully', async () => {
    const agent = new UIMAgent('test-agent');
    
    // Discover service
    const service = await agent.discoverService('example.com');
    expect(service).to.not.be.null;
    
    // Get policy and PAT
    const pat = await agent.getPAT(service.policyUrl);
    expect(pat).to.not.be.null;
    
    // Execute intent
    const result = await agent.executeIntent(
      service.url,
      'example.com:searchProducts:v1',
      { query: 'laptop' },
      pat
    );
    
    expect(result).to.not.be.null;
    expect(result.products).to.be.an('array');
  });
});
```

### End-to-End Testing

End-to-end testing focuses on testing the complete flow from an AI agent to a web service. For example:

- Testing the discovery, policy acquisition, and intent execution flow
- Testing error handling and recovery
- Testing performance and scalability

#### Example End-to-End Test (JavaScript)

```javascript
const { expect } = require('chai');
const { UIMAgent } = require('../implementations/agent');
const { MockWebservice } = require('uim-mock-webservice');

describe('End-to-End Flow', () => {
  let webservice;
  
  before(async () => {
    // Start mock webservice
    webservice = new MockWebservice();
    await webservice.start();
  });
  
  after(async () => {
    // Stop mock webservice
    await webservice.stop();
  });
  
  it('should complete the full flow successfully', async () => {
    const agent = new UIMAgent('test-agent');
    
    // Discover service
    const service = await agent.discoverService('localhost');
    expect(service).to.not.be.null;
    
    // Get policy and PAT
    const pat = await agent.getPAT(service.policyUrl);
    expect(pat).to.not.be.null;
    
    // Search for intents
    const intents = await agent.searchIntents(service.url, { tags: ['e-commerce'] });
    expect(intents).to.be.an('array');
    expect(intents.length).to.be.greaterThan(0);
    
    // Execute intent
    const intent = intents[0];
    const result = await agent.executeIntent(
      service.url,
      intent.intent_uid,
      { query: 'laptop' },
      pat
    );
    
    expect(result).to.not.be.null;
    expect(result.products).to.be.an('array');
  });
});
```

## Testing Best Practices

### Test Coverage

Ensure that your tests cover all aspects of the UIM Protocol:

- Service discovery
- Intent discovery
- Policy retrieval
- PAT acquisition
- Intent execution
- Error handling

### Test Edge Cases

Test edge cases and error conditions:

- Invalid parameters
- Expired PATs
- Network errors
- Rate limiting
- Invalid signatures

### Test Interoperability

Test your implementation with other implementations:

- Test AI agents with different web services
- Test web services with different AI agents
- Test with the mock implementations

### Continuous Integration

Set up continuous integration to run tests automatically:

- Run tests on every commit
- Run tests on every pull request
- Run tests on every release

### Performance Testing

Test the performance of your implementation:

- Test with a large number of intents
- Test with a large number of requests
- Test with a large number of clients

## Troubleshooting

### Common Issues

#### DNS Resolution Errors

If you're having trouble with DNS resolution:

1. Check that the domain exists and has TXT records
2. Try using a different DNS server
3. Use verbose logging to see more detailed error information

#### PAT Acquisition Errors

If you're having trouble acquiring PATs:

1. Check that your keys are generated correctly
2. Verify that the policy is accessible
3. Ensure that your agent ID is valid
4. Use verbose logging to see more detailed error information

#### Intent Execution Errors

If you're having trouble executing intents:

1. Check that you have a valid PAT
2. Verify that the intent UID is correct
3. Ensure that the parameters are valid
4. Use verbose logging to see more detailed error information

### Debugging

To debug UIM Protocol interactions:

1. **Enable Verbose Logging**: Turn on detailed logging in your implementation.
2. **Use the UIM Protocol CLI**: The CLI provides debugging tools for UIM Protocol interactions.
3. **Check Network Requests**: Use tools like Wireshark or browser developer tools to inspect network requests.
4. **Validate JSON**: Ensure your JSON payloads are valid and correctly formatted.
5. **Test with Mock Services**: Use mock services to isolate and debug specific issues.

## Conclusion

Testing is a critical part of implementing the UIM Protocol. By following the methodologies and best practices outlined in this guide, you can ensure that your implementation correctly follows the specification and can interoperate with other implementations.

For more information, see the [AI Agent Implementation Guide](ai-agent-guide.md) and [Service Provider Implementation Guide](service-provider-guide.md).
