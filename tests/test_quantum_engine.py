import unittest
from fqhf.quantum_engine import QuantumEngine

class TestQuantumEngine(unittest.TestCase):
    def test_prepare_and_shutdown(self):
        qe = QuantumEngine()
        self.assertFalse(qe.environment_ready)
        qe.prepare_environment()
        self.assertTrue(qe.environment_ready)
        qe.shutdown()
        self.assertFalse(qe.environment_ready)

    def test_run_without_prepare(self):
        qe = QuantumEngine()
        with self.assertRaises(RuntimeError):
            qe.run_future_simulation("test")

if __name__ == "__main__":
    unittest.main()

