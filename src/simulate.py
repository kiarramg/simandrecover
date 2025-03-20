# Python script to generate and simulate data
import numpy as np

def generate_true_parameters():
    """Randomly sample parameters within realistic cognitive model ranges, ensuring they are never zero."""
    v = np.random.uniform(0.5, 2)  # Drift rate
    a = np.random.uniform(0.5, 2)  # Boundary separation
    tau = np.random.uniform(0.1, 0.5)  # Nondecision time
    
    # Ensure none of the parameters are zero (extra safeguard, though unlikely needed)
    while v == 0:
        v = np.random.uniform(0.5, 2)
    while a == 0:
        a = np.random.uniform(0.5, 2)
    while tau == 0:
        tau = np.random.uniform(0.1, 0.5)

    return v, a, tau

#note: everything above here was drafted with the help of ChatGPT

def compute_predicted_statistics(v, a, tau):
    if v == 0:
        # When drift rate is zero, set reasonable default values
        M_pred = tau  # Mean RT should just be non-decision time
        y = 1  # When v = 0, exp(-a * v) = exp(0) = 1
        R_pred = 1 / (1 + y)  # Which simplifies to 1 / 2
        V_pred = 0  # Variance should be 0 in the absence of drift
    else:
        y = np.exp(-a * v)
        R_pred = 1 / (1 + y)
        M_pred = tau + (a / (2 * v)) * ((1 - y) / (1 + y))
        V_pred = (a / (2 * (v**3))) * ((1 - 2 * a * v * y - y**2) / ((1 + y) ** 2))

    return R_pred, M_pred, V_pred


def simulate_observed_statistics(R_pred, M_pred, V_pred, N):
    """Simulate observed accuracy, mean RT, and variance using sampling distributions."""
    Robs = np.random.binomial(N, R_pred) / N
    Mobs = np.random.normal(M_pred, np.sqrt(V_pred / N))
    Vobs = np.random.gamma((N - 1) / 2, (2 * V_pred) / (N - 1))
    return Robs, Mobs, Vobs
