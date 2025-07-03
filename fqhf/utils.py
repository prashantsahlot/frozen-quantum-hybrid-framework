import uuid
from datetime import datetime
import json

def generate_session_id() -> str:
    """
    Generate a unique session ID.
    """
    session_id = str(uuid.uuid4())
    print(f"🆔 Generated session ID: {session_id}")
    return session_id

def log_message(message: str, level: str = "INFO"):
    """
    Log a message with timestamp and level.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def format_result(result) -> str:
    """
    Format quantum results or CPU results into pretty JSON string.
    """
    formatted = json.dumps(result, indent=2)
    print(f"📝 Formatted result:\n{formatted}")
    return formatted

