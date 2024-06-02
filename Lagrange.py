import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

#polinom lagrange
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])


poly_lagrange = lagrange(x, y)


x_new = np.linspace(5, 40, 500)
y_new_lagrange = poly_lagrange(x_new)


plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data asli')
plt.plot(x_new, y_new_lagrange, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Tegangan vs Waktu Patah (Lagrange)')
plt.legend()
plt.grid(True)
plt.show()
