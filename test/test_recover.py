import unittest
import numpy as np
from src.simulate import compute_predicted_statistics  # Import your forward function
#drafted with the help of ChatGPT
class TestForwardEquations(unittest.TestCase):
    
    def test_forward_equations(self):
        """Test if the forward equations output reasonable values."""
        # Define test parameters
        ν, α, τ = 1.0, 1.5, 0.3

        # Compute predicted summary statistics
        R_pred, M_pred, V_pred = compute_predicted_statistics(ν, α, τ)

        # Check that values are within expected ranges
        self.assertGreaterEqual(R_pred, 0.5)
        self.assertLessEqual(R_pred, 1.0)
        self.assertGreater(M_pred, τ)  # Mean RT should be greater than τ
        self.assertGreater(V_pred, 0)  # Variance should always be positive

    def test_forward_equations_zero_drift(self):
        """Test if drift rate of zero results in R_pred ~ 0.5."""
        ν, α, τ = 0.0, 1.0, 0.2  # Drift rate is 0

        R_pred, _, _ = compute_predicted_statistics(ν, α, τ)
        self.assertAlmostEqual(R_pred, 0.5, places=2)

if __name__ == "__main__":
    unittest.main()
    