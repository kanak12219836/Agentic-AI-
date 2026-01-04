from logger import get_logger

logger = get_logger(__name__)

def summarize_text(text: str) -> str:
    """Summarizes the given text (Mock implementation)."""
    logger.info(f"Summarizing text ({len(text)} chars)...")
    
    if not text:
        return ""
        
    sentences = text.split(".")
    # Basic mock summary: take first 3 sentences
    summary = ".".join(sentences[:3])
    if len(sentences) > 3:
        summary += "."
        
    return summary

def analyze_text(text: str) -> str:
    """Analyzes the given text (Mock implementation)."""
    logger.info(f"Analyzing text ({len(text)} chars)...")
    
    if not text:
        return "No text to analyze."

    word_count = len(text.split())
    char_count = len(text)
    
    analysis = (
        f"Text Analysis:\n"
        f"Words: {word_count}\n"
        f"Characters: {char_count}\n"
    )
    return analysis
