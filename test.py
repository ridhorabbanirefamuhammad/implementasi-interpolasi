import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_new):
    def basis_polynomial(x, k, x_points):
        term = 1
        for i in range(len(x_points)):
            if i != k:
                term *= (x - x_points[i]) / (x_points[k] - x_points[i])
        return term

    y_new = np.zeros_like(x_new, dtype=float)
    for i in range(len(x_new)):
        y_new[i] = sum(y[k] * basis_polynomial(x_new[i], k, x) for k in range(len(x)))
    return y_new

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

def poly_lagrange(x):
    x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y_points = np.array([300, 200, 180, 160, 150, 140, 135, 130])
    return lagrange_interpolation(x_points, y_points, np.array([x]))[0]

def test_lagrange():
    test_x = np.array([12, 22, 28, 35])
    expected_y = [poly_lagrange(xi) for xi in test_x]
    print("Hasil Interpolasi Lagrange:", expected_y)

def test_newton():
    x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    y = np.array([300, 200, 180, 160, 150, 140, 135, 130])
    test_x = np.array([12, 22, 28, 35])
    expected_y = newton_interpolation(x, y, test_x)
    print("Hasil Interpolasi Newton:", expected_y)

test_lagrange()
test_newton()
