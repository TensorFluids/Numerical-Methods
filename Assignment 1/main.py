import numpy as np
import matplotlib.pyplot as plt
import os
from interpolation import vandermonde_interpolation

def f1(x):
    return np.sin(2*np.pi*x)

def f2(x):
    return 1.0 / (1.0+x**2)

x1_fine = np.linspace(0, 1, 1000)
x2_fine = np.linspace(-3, 3, 6000)


fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()


# Plot the true functions first
ax1.plot(x1_fine, f1(x1_fine), 'k-', linewidth=2, label="f1(x) true")
ax2.plot(x2_fine, f2(x2_fine), 'k-', linewidth=2, label="f2(x) true")

print("Running...")

N_values = [3, 5, 10]

# N_values = [100]
# ax2.set_ylim(-1.5, 1.5)       #uncomment when N=100
# ax1.set_ylim(-1.5, 1.5)       #uncomment when N=100

marker_map = {
    3: 'o',      
    5: 's',      
    10: 'x',     
    100: ''     
}

for N in N_values:
    x1_data = np.linspace(0, 1, N + 1)
    y1_data = f1(x1_data)

    x2_data = np.linspace(-3, 3, N + 1)
    y2_data = f2(x2_data)

    # Build matrix
    a1, t1, c1 = vandermonde_interpolation(x1_data, y1_data)
    a2, t2, c2 = vandermonde_interpolation(x2_data, y2_data)

    # Construct polynomial
    p1_fine = np.polyval(a1, x1_fine)
    p2_fine = np.polyval(a2, x2_fine)

    # Overlay on f1 axes
    ax1.plot(x1_fine, p1_fine, '--', label=f"N={N}")
    ax1.plot(x1_data, y1_data, linestyle='None', marker=marker_map[N], markersize=4, label=f"data N={N}")

    # Overlay on f2 axes
    ax2.plot(x2_fine, p2_fine, '--', label=f"N={N}")
    ax2.plot(x2_data, y2_data, linestyle='None', marker=marker_map[N], markersize=4, label=f"data N={N}")

    print(f"N = {N}")
    print("f1 coefficients:", a1)
    print("f1 time:", t1)
    print("f1 condition number:", c1)
    print("f2 coefficients:", a2)
    print("f2 time:", t2)
    print("f2 condition number:", c2)
    print()


# f1 plot
ax1.set_title("f1(x) = sin(2πx) — Vandermonde Interpolation")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()
ax1.legend()

# f2 plot
ax2.set_title("f2(x) = 1/(1+x²) — Vandermonde Interpolation")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid()
ax2.legend()


os.makedirs("Plots", exist_ok=True)
fig1.savefig("Plots/f1_interpolation.png", dpi=300, bbox_inches="tight")
fig2.savefig("Plots/f2_interpolation.png", dpi=300, bbox_inches="tight")
plt.show()
