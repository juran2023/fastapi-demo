import logging
from app.core.logging import setup_logging


setup_logging()
logger = logging.getLogger(__name__)
logger.info("hello log")
