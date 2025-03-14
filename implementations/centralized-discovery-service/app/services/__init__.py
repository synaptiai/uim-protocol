# app/services/__init__.py

from .crawler import start_crawler
from .dns_utils import get_agents_json_url_from_dns
from .nlp import process_natural_language_query  # If NLP is implemented