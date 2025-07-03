from fqhf.quantum_engine import QuantumEngine
from fqhf.classical_helper import optimize_data, hash_data, simulate_cpu_task
from fqhf.utils import generate_session_id, log_message, format_result

def main():
    # Start session
    session_id = generate_session_id()
    log_message(f"Starting new hybrid compute session: {session_id}")

    # Prepare data
    data = "future game data"
    optimized = optimize_data(data)
    hashed = hash_data(optimized)

    # Run classical CPU task
    cpu_output = simulate_cpu_task("GeneratePreAssets", duration=1.5)

    # Setup and run quantum engine
    qe = QuantumEngine()
    qe.prepare_environment()
    quantum_result = qe.run_future_simulation(hashed)
    qe.shutdown()

    # Format results
    formatted_quantum = format_result(quantum_result)
    formatted_cpu = format_result(cpu_output)

    log_message("Hybrid session completed successfully!", level="SUCCESS")

if __name__ == "__main__":
    main()

