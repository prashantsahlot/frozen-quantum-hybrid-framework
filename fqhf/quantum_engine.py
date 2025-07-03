class QuantumEngine:
    def __init__(self):
        self.environment_ready = False

    def prepare_environment(self):
        """
        Simulate preparing the quantum environment.
        """
        print("⚛️ Preparing quantum environment...")
        self.environment_ready = True

    def run_future_simulation(self, data):
        """
        Simulate running a heavy computation or game logic on quantum.
        """
        if not self.environment_ready:
            raise RuntimeError("Environment not ready. Call prepare_environment() first.")
        print(f"🚀 Running simulation on quantum with data: {data}")
        result = f"Processed[{data}]"
        return result

    def shutdown(self):
        """
        Simulate shutting down the quantum environment.
        """
        if self.environment_ready:
            print("❄️ Shutting down quantum environment...")
            self.environment_ready = False
        else:
            print("Environment already inactive.")

