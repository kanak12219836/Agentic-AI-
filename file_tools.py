import os
from logger import get_logger

logger = get_logger(__name__)

def read_file(filepath: str) -> str:
    """Reads content from a file."""
    if not os.path.exists(filepath):
        logger.error(f"File not found at {filepath}")
        return ""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        logger.info(f"Read content from {filepath} ({len(content)} chars)")
        return content
    except Exception as e:
        logger.error(f"Failed to read file {filepath}: {e}")
        return ""

def write_file(filepath: str, content: str):
    """Writes content to a file, creating directories if needed."""
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"Content written to {filepath} ({len(content)} chars)")
    except Exception as e:
        logger.error(f"Failed to write to file {filepath}: {e}")
