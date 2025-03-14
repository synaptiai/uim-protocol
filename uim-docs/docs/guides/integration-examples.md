# Integration Examples

This page provides practical examples of how AI agents and web services can integrate with each other using the UIM Protocol. These examples demonstrate the key concepts and workflows of the protocol in real-world scenarios.

## E-commerce Integration Example

This example demonstrates how an AI agent can interact with an e-commerce web service to search for products and place orders.

### Scenario

A user asks an AI assistant to find and purchase a laptop with specific requirements:

> "I need a laptop with at least 16GB RAM, an i7 processor, and a budget of around $1500."

### Implementation Steps

#### 1. Service Discovery

The AI agent first discovers the e-commerce service using DNS TXT records:

```python
import dns.resolver
import requests
import json

# Query DNS TXT records
txt_records = dns.resolver.resolve('ecommerce.example.com', 'TXT')
agents_json_url = None

# Parse TXT records
for record in txt_records:
    for txt_string in record.strings:
        txt_string = txt_string.decode('utf-8')
        if txt_string.startswith('uim-agents-file='):
            agents_json_url = txt_string.split('=')[1]
            break

# Fetch agents.json
if agents_json_url:
    response = requests.get(agents_json_url)
    agents_json = response.json()
```

#### 2. Intent Discovery

The AI agent searches for relevant intents:

```python
# Get discovery endpoint from agents.json
discovery_endpoint = agents_json.get('uim-api-discovery')

# Search for intents
response = requests.get(
    discovery_endpoint,
    params={
        'tags': 'e-commerce,search,products'
    }
)
intents = response.json().get('intents', [])

# Find the search intent
search_intent = next((i for i in intents if i['intent_name'] == 'SearchProducts'), None)
```

#### 3. Policy Retrieval and PAT Acquisition

The AI agent retrieves the policy and requests a PAT:

```python
# Get policy URL from agents.json
policy_url = agents_json.get('uim-policy-file')

# Retrieve policy
response = requests.get(policy_url)
policy = response.json()

# Sign policy
policy_json = json.dumps(policy).encode('utf-8')
signature = private_key.sign(
    policy_json,
    padding.PKCS1v15(),
    SHA256()
)

# Request PAT
response = requests.post(
    f"{agents_json['service-info']['service_url']}/pat/issue",
    json={
        'agent_id': 'ai-agent-123',
        'signed_policy': signature.hex(),
        'agent_public_key': public_key.decode('utf-8')
    }
)
pat = response.json().get('uim-pat')
```

#### 4. Intent Execution

The AI agent executes the search intent:

```python
# Execute search intent
response = requests.post(
    f"{agents_json['service-info']['service_url']}/uim/execute",
    headers={
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    },
    json={
        'intent_uid': search_intent['intent_uid'],
        'parameters': {
            'query': 'laptop',
            'category': 'electronics',
            'filters': {
                'ram': '16GB+',
                'processor': 'i7',
                'price_range': '1000-2000'
            }
        }
    }
)
search_results = response.json()

# Process search results
laptops = search_results.get('products', [])
for laptop in laptops:
    print(f"Found: {laptop['name']} - ${laptop['price']}")
```

#### 5. Order Placement

After the user selects a laptop, the AI agent executes the order intent:

```python
# Find the order intent
order_intent = next((i for i in intents if i['intent_name'] == 'PlaceOrder'), None)

# Execute order intent
response = requests.post(
    f"{agents_json['service-info']['service_url']}/uim/execute",
    headers={
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    },
    json={
        'intent_uid': order_intent['intent_uid'],
        'parameters': {
            'product_id': selected_laptop['id'],
            'quantity': 1,
            'shipping_address': {
                'name': 'John Doe',
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA',
                'zip': '12345',
                'country': 'USA'
            },
            'payment_method': {
                'type': 'credit_card',
                'token': 'payment-token-123'
            }
        }
    }
)
order_result = response.json()
print(f"Order placed: {order_result['order_id']}")
```

## Content Management Integration Example

This example demonstrates how an AI agent can interact with a content management system (CMS) to create and publish content.

### Scenario

A user asks an AI assistant to create a blog post about a specific topic and publish it on their website:

> "Create a blog post about the benefits of artificial intelligence in healthcare and publish it on my website."

### Implementation Steps

#### 1. Service Discovery and Intent Discovery

Similar to the e-commerce example, the AI agent discovers the CMS service and its intents.

#### 2. Content Creation

The AI agent executes the content creation intent:

```python
# Execute content creation intent
response = requests.post(
    f"{agents_json['service-info']['service_url']}/uim/execute",
    headers={
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    },
    json={
        'intent_uid': 'cms.example.com:create-content:v1',
        'parameters': {
            'title': 'The Benefits of AI in Healthcare',
            'content_type': 'blog_post',
            'content': {
                'body': '# The Benefits of AI in Healthcare\n\nArtificial intelligence is transforming healthcare in numerous ways...',
                'excerpt': 'Discover how AI is revolutionizing healthcare delivery and patient outcomes.',
                'format': 'markdown'
            },
            'metadata': {
                'author': 'AI Assistant',
                'categories': ['Healthcare', 'Technology', 'AI'],
                'tags': ['artificial intelligence', 'healthcare', 'medical technology']
            }
        }
    }
)
content_result = response.json()
content_id = content_result['content_id']
```

#### 3. Content Publication

The AI agent executes the content publication intent:

```python
# Execute content publication intent
response = requests.post(
    f"{agents_json['service-info']['service_url']}/uim/execute",
    headers={
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    },
    json={
        'intent_uid': 'cms.example.com:publish-content:v1',
        'parameters': {
            'content_id': content_id,
            'publish_date': '2025-03-13T16:00:00Z',
            'status': 'published'
        }
    }
)
publication_result = response.json()
print(f"Content published: {publication_result['url']}")
```

## Calendar Integration Example

This example demonstrates how an AI agent can interact with a calendar service to schedule meetings.

### Scenario

A user asks an AI assistant to schedule a meeting with their team:

> "Schedule a team meeting for next Tuesday at 2 PM for 1 hour with the marketing team."

### Implementation Steps

#### 1. Service Discovery and Intent Discovery

Similar to the previous examples, the AI agent discovers the calendar service and its intents.

#### 2. Availability Check

The AI agent executes the availability check intent:

```python
# Execute availability check intent
response = requests.post(
    f"{agents_json['service-info']['service_url']}/uim/execute",
    headers={
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    },
    json={
        'intent_uid': 'calendar.example.com:check-availability:v1',
        'parameters': {
            'date': '2025-03-18',
            'start_time': '14:00',
            'end_time': '15:00',
            'timezone': 'America/New_York',
            'attendees': ['marketing-team@example.com']
        }
    }
)
availability_result = response.json()
```

#### 3. Meeting Creation

If everyone is available, the AI agent executes the meeting creation intent:

```python
# Execute meeting creation intent
response = requests.post(
    f"{agents_json['service-info']['service_url']}/uim/execute",
    headers={
        'Authorization': f'Bearer {pat}',
        'Content-Type': 'application/json'
    },
    json={
        'intent_uid': 'calendar.example.com:create-event:v1',
        'parameters': {
            'title': 'Marketing Team Meeting',
            'description': 'Weekly team sync to discuss ongoing projects and priorities.',
            'date': '2025-03-18',
            'start_time': '14:00',
            'end_time': '15:00',
            'timezone': 'America/New_York',
            'location': 'Conference Room A',
            'attendees': ['marketing-team@example.com'],
            'reminders': [
                {'type': 'email', 'minutes_before': 60},
                {'type': 'notification', 'minutes_before': 10}
            ]
        }
    }
)
meeting_result = response.json()
print(f"Meeting scheduled: {meeting_result['event_id']}")
```

## Conclusion

These examples demonstrate how the UIM Protocol enables AI agents to interact with web services in a standardized way. By following the protocol's discovery, policy adherence, and intent execution workflows, AI agents can provide users with seamless access to a wide range of services.

For more detailed implementation guidance, refer to the [AI Agent Implementation Guide](ai-agent-guide.md) and [Service Provider Implementation Guide](service-provider-guide.md).
