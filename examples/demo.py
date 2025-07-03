from fqhf.quantum_engine import QuantumEngine
from fqhf.classical_helper import optimize_data, hash_data, simulate_cpu_task
from fqhf.utils import generate_session_id, log_message, format_result

def main():
    # Start session
    session_id = generate_session_id()
    log_message(f"Starting new hybrid compute session: {session_id}")

    # Prepare data
    data = "future game data for quantum burst"
    optimized = optimize_data(data)
    hashed = hash_data(optimized)

    # Run classical CPU task
    cpu_output = simulate_cpu_task("GeneratePreAssets", duration=1.5)

    # Decide whether to burst to quantum (example: always True for now)
    use_burst = True

    quantum_result = None
    if use_burst:
        log_message("⚡ Burst mode enabled — switching to quantum acceleration!")
        qe = QuantumEngine()
        qe.prepare_environment()
        quantum_result = qe.run_future_simulation(hashed)
        qe.shutdown()
    else:
        log_message("❄️ Burst mode disabled — skipping quantum.")

    # Combine results
    final_results = {
        "optimized_data": optimized,
        "hashed_data": hashed,
        "cpu_result": cpu_output,
        "quantum_result": quantum_result,
    }

    # Format results
    formatted = format_result(final_results)
    print(formatted)

    log_message("Hybrid compute session completed successfully!", level="SUCCESS")

if __name__ == "__main__":
    main()


