import numpy as np
import matplotlib.pyplot as plt


def newton_interpolation(x, y, x_new):

    n = len(x)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i,j] = (divided_diff[i+1,j-1] - divided_diff[i,j-1]) / (x[i+j] - x[i])

    y_new = np.zeros_like(x_new, dtype=float)
    for i in range(len(x_new)):
        term = divided_diff[0,0]
        for j in range(1, n):
            term_j = divided_diff[0,j]
            for k in range(j):
                term_j *= (x_new[i] - x[k])
            term += term_j
        y_new[i] = term

    return y_new

x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([300, 200, 180, 160, 150, 140, 135, 130])

x_new = np.linspace(5, 40, 500)
y_new_newton = newton_interpolation(x, y, x_new)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Data asli')
plt.plot(x_new, y_new_newton, '-', label='Interpolasi Newton')
plt.xlabel('Tegangan (kg/mm²)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Tegangan vs Waktu Patah (Newton)')
plt.legend()
plt.grid(True)
plt.show()
