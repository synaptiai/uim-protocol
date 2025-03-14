# app/crud/__init__.py

from .intent import (
    get_intent_by_uid,
    create_intent,
    update_intent,
    delete_intent,
    get_intents_by_filters
)
from .service import (
    get_service_by_name,
    create_service,
    update_service,
    delete_service
)