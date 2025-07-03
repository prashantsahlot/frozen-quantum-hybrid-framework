import hashlib
import time

def optimize_data(data: str) -> str:
    """
    Simulate optimizing data before sending to quantum processor.
    Example: Remove whitespace, convert to uppercase.
    """
    print(f"🔧 Optimizing data: {data}")
    optimized = data.replace(" ", "").upper()
    print(f"✅ Optimized data: {optimized}")
    return optimized

def hash_data(data: str) -> str:
    """
    Hash the data using SHA-256 for integrity or pre-quantum prep.
    """
    print(f"🔒 Hashing data: {data}")
    hashed = hashlib.sha256(data.encode()).hexdigest()
    print(f"✅ Hashed data: {hashed}")
    return hashed

def simulate_cpu_task(task_name: str, duration: float = 1.0) -> str:
    """
    Simulate running a CPU-intensive task (e.g., local preprocessing, asset generation).
    """
    print(f"⚙️ Running classical CPU task: {task_name} for {duration} seconds...")
    time.sleep(duration)
    result = f"CPU_Result[{task_name}]"
    print(f"✅ Completed CPU task: {result}")
    return result

