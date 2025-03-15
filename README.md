# simulate and recover background & description
## 1. Explain theoretical background of EZ diffusion. 2. Summarize results (plots of bias/squared error vs. NN). 3. Discuss interpretation (i.e., whether EZ diffusion is consistent).
 ### The EZ diffusion model is a simplified approach to the drift diffusion model (DDM), which is commonly used in cognitive science to analyze decision-making processes based on response times (RTs) and accuracy. The model is considered successful if it can successfully recover key parameters — drift rate (ν), boundary separation (α), and nondecision time (τ) - when applied to data that was originally generated using the same model. This is necessary in order to ensure that the model functions as expected before it is applied to experimental data.
 
 ### The process begins with selecting a set of “true” parameters and a sample size (N). Using these parameters, the forward equations of the EZ diffusion model generate predicted summary statistics, which include the accuracy rate (R_pred), mean RT (M_pred), and RT variance (V_pred). However, real-world data is noisy, meaning that observed data will not always perfectly match theoretical predictions. To account for this, observed summary statistics ( R_obs, M_obs, V_obs) are simulated using known probability distributions. For example, the accuracy rate is drawn from a binomial distribution, mean RT follows a normal distribution, and RT variance is modeled with a gamma distribution. These steps introduce realistic variability, mimicking the way actual experimental data may fluctuate.
 
 ### Once the observed summary statistics are generated, the inverse equations of the EZ diffusion model are applied to estimate the original parameters. The estimated values ( ν_est, α_est, τ_est) are then compared to the true values to assess the model’s accuracy. This is done by computing the estimation bias (b), which represents the difference between the true and estimated parameters, and the squared error (b^2), which measures the overall deviation. Ideally, the bias should be close to zero on average, and the squared error should decrease as the sample size increases. If these conditions are met, it suggests that the model can reliably recover its own parameters under controlled conditions.

### The results of this exercise demonstrate that, when applied to data that truly follows the EZ diffusion model, the estimation process is generally accurate. A key finding is that increasing the sample size improves the reliability of the parameter estimates, reducing variability and error. This confirms that the model is internally consistent and capable of extracting meaningful cognitive parameters from observed response patterns. However, while this validation is encouraging, it does not guarantee that the model will perform equally well on real-world data. In practice, human decision-making is influenced by additional cognitive and contextual factors that may not be fully captured by the simplified structure of the EZ diffusion model.

### Overall, the simulate-and-recover exercise serves as an important preliminary test for the EZ diffusion model. It confirms that the model can accurately estimate decision-making parameters under ideal conditions, providing a foundation for further research. However, additional validation is needed to assess its applicability to more complex experimental scenarios where noise and variability are even greater.