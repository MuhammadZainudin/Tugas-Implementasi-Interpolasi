import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    interpolated_value = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        interpolated_value += term
    
    return interpolated_value

x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

x_range = np.linspace(5, 40, 500)
y_range = [lagrange_interpolation(x_points, y_points, x) for x in x_range]

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, 'o', label='Titik Data', markersize=8)
plt.plot(x_range, y_range, '-', label='Polinom Lagrange')
plt.title('Interpolasi Polinom Lagrange')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
