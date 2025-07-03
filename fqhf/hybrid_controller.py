from fqhf.classical_helper import optimize_data, hash_data, simulate_cpu_task
from fqhf.quantum_engine import QuantumEngine
from fqhf.utils import log_message

def hybrid_compute_pipeline(data: str, use_burst: bool = True):
    log_message("🚩 Starting hybrid compute pipeline.")

    # Step 1: Classical optimization
    optimized = optimize_data(data)
    hashed = hash_data(optimized)

    # Step 2: CPU intensive task
    cpu_result = simulate_cpu_task("PreprocessingAssets", duration=1.0)

    # Step 3: Decide whether to burst to quantum
    quantum_result = None
    if use_burst:
        log_message("⚡ Burst mode enabled — switching to quantum acceleration!")
        qe = QuantumEngine()
        qe.prepare_environment()
        quantum_result = qe.run_future_simulation(hashed)
        qe.shutdown()
    else:
        log_message("❄️ Burst mode disabled — skipping quantum.")

    # Step 4: Combine and return
    combined_result = {
        "optimized_data": optimized,
        "hashed_data": hashed,
        "cpu_result": cpu_result,
        "quantum_result": quantum_result
    }

    log_message("✅ Hybrid compute pipeline completed.")
    return combined_result
