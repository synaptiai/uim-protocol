# Frequently Asked Questions (FAQ)

This page answers common questions about the Unified Intent Mediator (UIM) Protocol. If you don't find the answer to your question here, please reach out to us through GitHub Discussions or Discord.

## General Questions

### What is the UIM Protocol?

The Unified Intent Mediator (UIM) Protocol is a standardized framework that enables AI agents to interact with web services through well-defined intents, metadata, and execution methods. It provides a consistent way for AI agents to discover and use web service capabilities while ensuring security, privacy, and compliance.

### Why was the UIM Protocol created?

The UIM Protocol was created to address the fragmentation and inconsistency in how AI agents interact with web services. Before UIM, each AI agent had to implement custom integrations for each web service, leading to duplication of effort, inconsistent user experiences, and security concerns. UIM provides a standardized approach that benefits both AI agents and web services.

### Who can use the UIM Protocol?

The UIM Protocol is designed for:

- **AI Agent Developers**: Those building AI assistants, chatbots, or other AI systems that need to interact with web services.
- **Web Service Providers**: Organizations that want to make their services accessible to AI agents in a secure and standardized way.
- **Platform Providers**: Companies building platforms that connect AI agents and web services.
- **Researchers**: Those studying AI-web service interactions and developing new approaches.

### Is the UIM Protocol open source?

Yes, the UIM Protocol is open source and available under the Apache License 2.0. This means you can freely use, modify, and distribute it for both personal and commercial purposes.

### How does the UIM Protocol relate to other standards?

The UIM Protocol complements existing standards like OpenAPI, JSON Schema, and OAuth. It builds on these standards while adding specific features for AI-web service interactions, such as intent-based communication, policy adherence, and discovery mechanisms.

## Technical Questions

### How does service discovery work in the UIM Protocol?

Service discovery in the UIM Protocol works through two main mechanisms:

1. **DNS TXT Records**: Web services can publish TXT records in their DNS that point to their `agents.json` file, policy file, and discovery endpoint.
2. **agents.json File**: This file contains information about the service, its intents, and its policies.

AI agents can use these mechanisms to discover services and their capabilities without prior knowledge.

### What is a Policy Adherence Token (PAT)?

A Policy Adherence Token (PAT) is a signed JWT (JSON Web Token) that indicates an AI agent has agreed to adhere to a web service's policies. The AI agent obtains a PAT by signing the service's policy with its private key and sending the signature to the service. The service verifies the signature and issues a PAT, which the AI agent then uses for subsequent intent executions.

### How are intents defined in the UIM Protocol?

Intents in the UIM Protocol are defined with the following components:

- **Intent UID**: A unique identifier for the intent (e.g., `example.com:searchProducts:v1`).
- **Intent Name**: A human-readable name for the intent (e.g., `SearchProducts`).
- **Description**: A description of what the intent does.
- **Input Parameters**: The parameters required to execute the intent.
- **Output Parameters**: The parameters returned by the intent.
- **Endpoint**: The URL endpoint for executing the intent.
- **Tags**: Optional tags for categorizing the intent.

### How does the UIM Protocol handle versioning?

The UIM Protocol handles versioning through intent UIDs. Each intent UID includes a version component (e.g., `example.com:searchProducts:v1`). When a web service updates an intent in a backward-incompatible way, it creates a new version of the intent with a new UID. This allows AI agents to continue using the old version while transitioning to the new one.

### How does the UIM Protocol ensure security?

The UIM Protocol ensures security through several mechanisms:

1. **Policy Adherence Tokens (PATs)**: These tokens ensure that AI agents have agreed to adhere to a service's policies.
2. **RSA Key Pairs**: AI agents and web services use RSA key pairs for signing and verifying signatures.
3. **HTTPS**: All communication between AI agents and web services is encrypted using HTTPS.
4. **Rate Limiting**: Web services can implement rate limiting to prevent abuse.
5. **Scoped Permissions**: PATs can be scoped to specific intents and operations.

### Can the UIM Protocol work in a decentralized environment?

Yes, the UIM Protocol is designed to work in both centralized and decentralized environments. In a decentralized environment, AI agents can discover services directly through DNS TXT records and `agents.json` files, without relying on a central registry.

## Implementation Questions

### How do I implement the UIM Protocol in my AI agent?

To implement the UIM Protocol in your AI agent, follow these steps:

1. **Set up your development environment** with the necessary libraries for HTTP requests, JSON processing, and cryptography.
2. **Generate an RSA key pair** for your AI agent.
3. **Implement service discovery** using DNS TXT records and `agents.json` files.
4. **Implement intent discovery** using the service's discovery endpoint.
5. **Implement policy retrieval and PAT acquisition**.
6. **Implement intent execution**.

For detailed instructions, see the [AI Agent Implementation Guide](../guides/ai-agent-guide.md).

### How do I implement the UIM Protocol in my web service?

To implement the UIM Protocol in your web service, follow these steps:

1. **Set up your development environment** with the necessary libraries for HTTP requests, JSON processing, and cryptography.
2. **Generate an RSA key pair** for your web service.
3. **Define your intents** with their parameters, endpoints, and metadata.
4. **Define your policy** that AI agents must adhere to.
5. **Create an `agents.json` file** that describes your service and its intents.
6. **Configure DNS TXT records** to help AI agents discover your service.
7. **Implement the discovery API** that allows AI agents to search for intents.
8. **Implement the policy API** that allows AI agents to retrieve the policy.
9. **Implement the PAT issuance API** that allows AI agents to request PATs.
10. **Implement the intent execution API** that allows AI agents to execute intents.

For detailed instructions, see the [Service Provider Implementation Guide](../guides/service-provider-guide.md).

### Are there any SDKs or libraries for implementing the UIM Protocol?

Yes, we provide SDKs and libraries for implementing the UIM Protocol in various programming languages:

- **JavaScript/TypeScript**: `uim-protocol-js`
- **Python**: `uim-protocol-py`
- **Java**: `uim-protocol-java`
- **Go**: `uim-protocol-go`

These SDKs provide high-level abstractions for working with the UIM Protocol, making it easier to implement in your applications.

### How can I test my UIM Protocol implementation?

You can test your UIM Protocol implementation using the following tools:

1. **UIM Protocol CLI**: A command-line tool for testing UIM Protocol implementations.
2. **UIM Protocol Validator**: A tool for validating UIM Protocol implementations against the specification.
3. **Mock Agent and Mock Webservice**: Reference implementations that you can use for testing.

For more information, see the [Testing Guide](../guides/testing.md).

## Business Questions

### What are the benefits of implementing the UIM Protocol for my web service?

Implementing the UIM Protocol for your web service offers several benefits:

1. **Increased Reach**: Make your service accessible to a wide range of AI agents.
2. **Standardized Integration**: Reduce the effort required to integrate with AI agents.
3. **Enhanced Security**: Ensure that AI agents adhere to your policies.
4. **Improved User Experience**: Provide a consistent and seamless experience for users.
5. **New Revenue Streams**: Monetize access to your service through the UIM Protocol.

### How can I monetize my web service using the UIM Protocol?

You can monetize your web service using the UIM Protocol in several ways:

1. **Usage-based Pricing**: Charge based on the number of intent executions.
2. **Subscription-based Pricing**: Offer different tiers of access with varying capabilities.
3. **Freemium Model**: Provide basic intents for free and charge for premium intents.
4. **Pay-per-Result**: Charge based on the value of the results provided.

The UIM Protocol's policy framework allows you to define and enforce these monetization models.

### How does the UIM Protocol handle compliance with regulations?

The UIM Protocol helps with compliance in several ways:

1. **Policy Framework**: Define and enforce policies that comply with regulations.
2. **Audit Logging**: Track intent executions for compliance reporting.
3. **Data Minimization**: Only share the data necessary for intent execution.
4. **User Consent**: Implement consent mechanisms through policies.
5. **Regional Compliance**: Define different policies for different regions.

### How can I get support for implementing the UIM Protocol?

You can get support for implementing the UIM Protocol through:

1. **GitHub Discussions**: Ask questions and get help from the community.
2. **Discord**: Join our Discord server for real-time discussions and support.
3. **Documentation**: Refer to our comprehensive documentation.
4. **Workshops and Webinars**: Attend our workshops and webinars to learn more.
5. **Professional Services**: Contact us for professional implementation services.

## Community Questions

### How can I contribute to the UIM Protocol?

You can contribute to the UIM Protocol in several ways:

1. **Code Contributions**: Implement new features, fix bugs, or improve performance.
2. **Documentation**: Improve existing documentation or create new guides and tutorials.
3. **Testing**: Test the protocol in different environments and report issues.
4. **Use Cases**: Share how you're using the UIM Protocol in your projects.
5. **Feedback**: Provide feedback on the protocol design and implementation.

For more information, see the [Contributing Guide](contributing.md).

### Is there a community for UIM Protocol users and developers?

Yes, we have an active community of UIM Protocol users and developers. You can join us through:

1. **GitHub Discussions**: For general questions and discussions.
2. **Discord**: For real-time discussions and community support.
3. **Twitter**: For announcements and updates.
4. **Meetups**: For in-person and virtual events.

### How is the UIM Protocol governed?

The UIM Protocol is governed by a steering committee that oversees the project's direction and development. The committee includes representatives from various stakeholders, including AI agent developers, web service providers, and the open-source community.

For more information, see the [Governance](governance.md) page.

### What is the roadmap for the UIM Protocol?

The UIM Protocol roadmap includes:

1. **Short-term**: Enhancing discovery mechanisms, improving the policy framework, and developing developer tools.
2. **Medium-term**: Adding security enhancements, optimizing performance, and expanding the ecosystem.
3. **Long-term**: Standardization, enterprise features, and specialized extensions.

For more information, see the [Roadmap](roadmap.md) page.

## Troubleshooting

### I'm getting a "Policy Rejected" error when requesting a PAT. What should I do?

This error occurs when the web service rejects the policy signature. Check the following:

1. **Signature Algorithm**: Ensure you're using the correct algorithm (RSA-SHA256).
2. **Policy Format**: Ensure you're signing the exact policy returned by the service.
3. **Key Pair**: Verify that you're using the correct key pair.
4. **Service Requirements**: Check if the service has specific requirements for policy acceptance.

### My AI agent can't discover a service. What should I check?

If your AI agent can't discover a service, check the following:

1. **DNS TXT Records**: Verify that the service has published the correct TXT records.
2. **agents.json File**: Ensure the `agents.json` file is accessible and correctly formatted.
3. **HTTPS**: Verify that the service is using HTTPS.
4. **Network Issues**: Check for network connectivity issues.
5. **Service Status**: Verify that the service is online and operational.

### Intent execution is failing with a 400 error. What could be the issue?

A 400 error during intent execution could be due to:

1. **Invalid Parameters**: Check that you're providing all required parameters with the correct types.
2. **Parameter Format**: Ensure parameters are formatted correctly (e.g., dates in ISO 8601 format).
3. **Intent UID**: Verify that you're using the correct intent UID.
4. **PAT**: Ensure your PAT is valid and has not expired.
5. **Rate Limiting**: Check if you've exceeded the service's rate limits.

### How can I debug UIM Protocol interactions?

To debug UIM Protocol interactions:

1. **Enable Verbose Logging**: Turn on detailed logging in your implementation.
2. **Use the UIM Protocol CLI**: The CLI provides debugging tools for UIM Protocol interactions.
3. **Check Network Requests**: Use tools like Wireshark or browser developer tools to inspect network requests.
4. **Validate JSON**: Ensure your JSON payloads are valid and correctly formatted.
5. **Test with Mock Services**: Use mock services to isolate and debug specific issues.
