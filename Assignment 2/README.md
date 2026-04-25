## Discussion

### Recovery of Parameters

The true model is:

$$
E(p) = 0.414 - 0.059p + \Theta
$$

Using linear regression, the fitted model is:

$$
\hat{E}(p) = \hat{E}_0 - \hat{k}p
$$

The parameter values are:

$E_0$ = 0.414
$k$  = 0.059


For an initial run with seed = 10, N = 15, and noise:

$\Theta$ ~ U(-0.005, 0.005)


the fitted parameters are close to the true values:


Estimated $E_0$ = appx. 0.414
Estimated $k$  = appx. 0.058


The small deviation is caused by the added random noise.

---

### Effect of Noise

The noise term $\Theta$ directly affects the quality of the fitted parameters.

For small noise:

$\Theta$ ~ U(-0.005, 0.005)

- Data points stay close to the true line  
- Parameter estimates are accurate  

For bigger noise, for example:

$\Theta$ ~ U(-0.05, 0.05)

- Data points are more scattered  
- Parameter estimates deviate more  

General trend:

higher noise  -> worse parameter recovery
lower noise   -> more accurate parameter recovery


---

### Effect of Number of Measurements

The number of measurements $N$ also impacts accuracy.

Small $N$ (e.g. 5–10):
- Estimates are unstable  
- Strong dependence on noise  

Large $N$ (e.g. 50–100):
- Estimates are more stable  
- Noise averages out  

General trend:

larger N  -> more accurate stable estimates
smaller N -> less stable estimates


---

### Evaluation of Metrics


Mean Squared Error (MSE)
Mean Absolute Error (MAE)

Definitions:

$$
MSE = \frac{1}{N} \sum_{i=1}^{N} (E_i - \hat{E}_i)^2
$$

$$
MAE = \frac{1}{N} \sum_{i=1}^{N} |E_i - \hat{E}_i|
$$

Observations:

- MSE penalizes large errors more strongly
- MAE gives average deviation

Typical values for small noise:

MSE = appx. 1e-6 to 1e-5
MAE = appx. 1e-3


As noise increases:
- Both MSE and MAE increase  
- MSE increases faster due to squaring  

---

### Numerical Results

| Noise range | N  | Estimated E0 | Estimated k | MSE       | MAE     |
|------------|----|-------------|-------------|-----------|---------|
| ±0.005     | 15 | ~0.414      | ~0.059      | small     | small   |
| ±0.020     | 15 | ~0.413 | ~0.058 | larger    | larger  |
| ±0.050     | 15 |  less accurate |  less accurate |  larger |  larger |
| ±0.005     | 50 | stable      | stable      | small     | small   |

Exact values depend on the random seed, but the trend is consistent.

