# Python script to generate and simulate data
import numpy as np

def generate_true_parameters():
    """Randomly sample parameters within realistic cognitive model ranges."""
    v = np.random.uniform(0.5, 2)  # Drift rate
    a = np.random.uniform(0.5, 2)  # Boundary separation
    tau = np.random.uniform(0.1, 0.5)  # Nondecision time
    return v, a, tau

def compute_predicted_statistics(v, a, tau):
    # Ensure v is not zero to prevent division by zero error
    if v == 0:
        M_pred = tau  # Assign a reasonable default value when drift rate is 0
    else:
        y = np.exp(-2 * a * v)  # Assuming y is computed like this
        M_pred = tau + (a / (2 * v)) * ((1 - y) / (1 + y))  

    # Compute R_pred and V_pred as usual
    R_pred = 1 / (1 + np.exp(-2 * a * v))  # Example formula
    V_pred = max(0, M_pred * 0.1)  # Ensure variance is always positive

    return R_pred, M_pred, V_pred


def simulate_observed_statistics(R_pred, M_pred, V_pred, N):
    """Simulate observed accuracy, mean RT, and variance using sampling distributions."""
    Robs = np.random.binomial(N, R_pred) / N
    Mobs = np.random.normal(M_pred, np.sqrt(V_pred / N))
    Vobs = np.random.gamma((N - 1) / 2, (2 * V_pred) / (N - 1))
    return Robs, Mobs, Vobs
