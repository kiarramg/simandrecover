# Unit tests for simulation
import unittest
from src.simulate import generate_true_parameters, compute_predicted_statistics

class TestSimulate(unittest.TestCase):

    def test_generate_true_parameters(self):
        v, a, tau = generate_true_parameters()
        self.assertTrue(0.5 <= v <= 2)
        self.assertTrue(0.5 <= a <= 2)
        self.assertTrue(0.1 <= tau <= 0.5)

    def test_compute_predicted_statistics(self):
        R_pred, M_pred, V_pred = compute_predicted_statistics(1.0, 1.0, 0.3)
        self.assertGreater(R_pred, 0)
        self.assertGreater(M_pred, 0)
        self.assertGreater(V_pred, 0)

if __name__ == "__main__":
    unittest.main()
