import numpy as np
import time

def vandermonde_interpolation(x_dataPoints, y_dataPoints):
    start = time.time()

    V = np.vander(x_dataPoints)
    a = np.linalg.solve(V, y_dataPoints)

    end = time.time()
    runtime = end - start
    conditionNumber = np.linalg.cond(V)

    return a, runtime, conditionNumber