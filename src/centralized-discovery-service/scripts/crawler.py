# scripts/crawler.py
# USAGE: python scripts/crawler.py

import sys
import os
import asyncio
import logging

# Adjust the import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.crawler import start_crawler
from app.utils.logging import setup_logging

def main():
    """Entry point for the crawler script."""
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Starting crawler...")
    asyncio.run(start_crawler())
    logger.info("Crawler finished.")

if __name__ == "__main__":
    main()