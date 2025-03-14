# Python script to generate and simulate data
import numpy as np

def generate_true_parameters():
    """Randomly sample parameters within realistic cognitive model ranges."""
    v = np.random.uniform(0.5, 2)  # Drift rate
    a = np.random.uniform(0.5, 2)  # Boundary separation
    tau = np.random.uniform(0.1, 0.5)  # Nondecision time
    return v, a, tau

def compute_predicted_statistics(v, a, tau):
    """Compute accuracy, mean RT, and variance using EZ diffusion forward equations."""
    y = np.exp(-a * v)
    R_pred = 1 / (y + 1)
    M_pred = tau + (a / (2 * v)) * ((1 - y) / (1 + y))
    V_pred = (a / (2 * v**3)) * ((1 - 2 * a * v * y - y**2) / (y + 1)**2)
    return R_pred, M_pred, V_pred

def simulate_observed_statistics(R_pred, M_pred, V_pred, N):
    """Simulate observed accuracy, mean RT, and variance using sampling distributions."""
    Robs = np.random.binomial(N, R_pred) / N
    Mobs = np.random.normal(M_pred, np.sqrt(V_pred / N))
    Vobs = np.random.gamma((N - 1) / 2, (2 * V_pred) / (N - 1))
    return Robs, Mobs, Vobs
