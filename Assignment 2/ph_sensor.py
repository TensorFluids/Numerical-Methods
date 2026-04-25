import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(10)
N = 5
noise = 0.005

def get_measurement (p: float):
    added_noise = random.uniform(-noise, noise)
    return 0.414 - 0.059*p + added_noise


def regression(p_values: np.ndarray, measurements):
    A = np.column_stack((np.ones(len(p_values)), -p_values))

    lhs = A.T @ A
    rhs = A.T @ measurements

    a = np.linalg.solve(lhs, rhs)

    E0_hat = a[0]
    k_hat = a[1]

    return E0_hat, k_hat

def mean_squared_error(E, E_hat):
    return np.mean((E - E_hat) ** 2)
def mean_absolute_error(E, E_hat):
    return np.mean(np.abs(E - E_hat))


########################################################

p_values = np.arange(N, dtype=float)
measurements = np.zeros(N)

for i, p in enumerate(p_values):
    measurements[i] = get_measurement(p)

E0_hat, k_hat = regression(p_values, measurements)

print("Estimated E0:", E0_hat)
print("Estimated k:", k_hat)

fitted_values = E0_hat - k_hat * p_values


mse = mean_squared_error(measurements, fitted_values)
mae = mean_absolute_error(measurements, fitted_values)
print("MSE:", mse)
print("MAE:", mae)

# Plot
plt.scatter(p_values, measurements, label="Noisy measurements", color='red')
plt.plot(p_values, fitted_values, label="Fitted line")

plt.xlabel("pH value p")
plt.ylabel("Voltage E(p) [V]")
plt.title("pH Sensor Calibration using Linear Regression")
plt.legend()
plt.grid(True)

plt.show()