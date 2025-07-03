from fqhf.quantum_engine import QuantumEngine
from fqhf.classical_helper import simulate_cpu_task
from fqhf.utils import generate_session_id, log_message, format_result

def cpu_plan_conversion_steps(data: str):
    """
    CPU decides the plan of what to do with the data.
    Returns a list of transformation steps.
    """
    log_message(f"🧠 CPU planning conversion steps for data: {data}")
    steps = [
        {"action": "reverse"},
        {"action": "uppercase"},
        {"action": "append_suffix", "value": "_FROZEN"}
    ]
    log_message(f"✅ CPU planned steps: {steps}")
    return steps

def quantum_execute_step(data: str, step: dict, qe: QuantumEngine):
    """
    Quantum engine executes a single step on the data.
    """
    action = step["action"]
    log_message(f"⚡ Quantum executing step: {action}")

    if action == "reverse":
        new_data = data[::-1]
    elif action == "uppercase":
        new_data = data.upper()
    elif action == "append_suffix":
        new_data = data + step.get("value", "")
    else:
        new_data = data  # No change if unknown

    # Simulate burst quantum processing
    qe.run_future_simulation(new_data)

    return new_data

def main():
    # Start session
    session_id = generate_session_id()
    log_message(f"Starting hybrid conversion session: {session_id}")

    # Original data
    data = "frozen game assets"

    # CPU plans what to do
    steps = cpu_plan_conversion_steps(data)

    # Initialize quantum engine
    qe = QuantumEngine()
    qe.prepare_environment()

    # Execute each step on quantum side
    final_data = data
    for step in steps:
        final_data = quantum_execute_step(final_data, step, qe)

    qe.shutdown()

    # Final simulated CPU finishing task
    simulate_cpu_task("Final CPU Wrapping", duration=1.0)

    # Combine results
    final_results = {
        "original_data": data,
        "final_converted_data": final_data,
        "steps_executed": steps
    }

    # Format results
    formatted = format_result(final_results)
    print(formatted)

    log_message("Hybrid CPU-decider + Quantum-executor session completed!", level="SUCCESS")

if __name__ == "__main__":
    main()
