import numpy as np
import matplotlib.pyplot as plt

def newton_divided_diff(x_points, y_points):
    n = len(x_points)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y_points
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (x_points[i+j] - x_points[i])
    
    return divided_diff

def newton_interpolation(x_points, y_points, x):
    divided_diff = newton_divided_diff(x_points, y_points)
    n = len(x_points)
    interpolated_value = divided_diff[0,0]
    product_term = 1.0
    
    for i in range(1, n):
        product_term *= (x - x_points[i-1])
        interpolated_value += divided_diff[0,i] * product_term
    
    return interpolated_value

x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

x_range = np.linspace(5, 40, 500)
y_range = [newton_interpolation(x_points, y_points, x) for x in x_range]

plt.figure(figsize=(10, 6))
plt.plot(x_points, y_points, 'o', label='Titik Data', markersize=8)
plt.plot(x_range, y_range, '-', label='Polinom Newton')
plt.title('Interpolasi Polinom Newton')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
