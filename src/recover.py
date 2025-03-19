# Python script to estimate parameters
# drafted with the help of ChatGPT
import numpy as np

def recover_parameters(R_obs, M_obs, V_obs):
    """Estimate drift rate (v_est), boundary separation (a_est), and nondecision time (tau_est)."""
    epsilon = 1e-10  # Small constant to prevent division by zero
    L = np.log(R_obs / (1 - R_obs + epsilon))

    print(f"Debug: R_obs={R_obs}, M_obs={M_obs}, V_obs={V_obs}")
# might be where the results are a little larger than expected
    v_est = np.sign(R_obs - 0.5) * ((L * (R_obs**2 * L - R_obs * L + R_obs - 0.5) / V_obs)**0.25)
    a_est = L / v_est
    tau_est = M_obs - (a_est / (2 * v_est)) * ((1 - np.exp(-v_est * a_est)) / (1 + np.exp(-v_est * a_est)))
    
    print(f"Debug: v_est={v_est}, a_est={a_est}, tau_est={tau_est}")
    
    return v_est, a_est, tau_est

def compute_errors(v_true, a_true, tau_true, v_est, a_est, tau_est):
    """Calculate bias and squared error."""
    bias = np.array([v_true - v_est, a_true - a_est, tau_true - tau_est])
    squared_error = bias ** 2
    return bias, squared_error
