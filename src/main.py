#!/usr/bin/env python3 and drafted with the help of ChatGPT
import numpy as np
from simulate import generate_true_parameters, compute_predicted_statistics, simulate_observed_statistics
from recover import recover_parameters
import os

def run_simulation(N, iterations=1000):
    """Runs the simulate-and-recover process for a given N and returns averaged results."""
    biases, squared_errors = [], []

    for _ in range(iterations):
        v_true, a_true, tau_true = generate_true_parameters()
        R_pred, M_pred, V_pred = compute_predicted_statistics(v_true, a_true, tau_true)
        R_obs, M_obs, V_obs = simulate_observed_statistics(R_pred, M_pred, V_pred, N)
        v_est, a_est, tau_est = recover_parameters(R_obs, M_obs, V_obs)
        
        bias = np.array([v_true - v_est, a_true - a_est, tau_true - tau_est])
        squared_error = bias ** 2

        biases.append(bias)
        squared_errors.append(squared_error)

    avg_bias = np.nanmean(biases, axis=0)
    avg_squared_error = np.nanmean(squared_errors, axis=0)

    print(f"Debug: v_true={v_true}, a_true={a_true}, tau_true={tau_true}")

    return avg_bias, avg_squared_error

def main():
    N_values = [10, 40, 4000]
    iterations = 1000
    results = {}

    for N in N_values:
        print(f"Running simulation for N={N}...")
        avg_bias, avg_squared_error = run_simulation(N, iterations)
        results[N] = {'avg_bias': avg_bias, 'avg_squared_error': avg_squared_error}
        print(f"Results for N={N} saved.")

    with open("simulation_results.txt", "w") as f:
        for N, result in results.items():
            f.write(f"N={N}\n")
            f.write(f"Average Bias: {result['avg_bias']}\n")
            f.write(f"Average Squared Error: {result['avg_squared_error']}\n\n")

if __name__ == "__main__":
    main()