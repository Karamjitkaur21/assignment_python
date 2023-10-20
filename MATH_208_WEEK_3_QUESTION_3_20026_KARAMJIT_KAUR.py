import numpy as np
import matplotlib.pyplot as plt

# Given data
X = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
Y = np.array([30, 25, 95, 115, 265, 325, 570, 700, 1085, 1300])

# Calculate the values of b1 (slope) and b0 (y-intercept) using linear regression
n = len(X)
mean_X = np.mean(X)
mean_Y = np.mean(Y)
b1 = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X) ** 2)
b0 = mean_Y - b1 * mean_X

# Calculate the coefficient of determination (r^2)
r = np.corrcoef(X, Y)[0, 1]
r_squared = r ** 2

# Create a linear regression model
def linear_regression(x):
    return b0 + b1 * x

# Plot the dataset and the linear regression line
plt.scatter(X, Y, label="Data points")
plt.plot(X, linear_regression(X), color='red', label="Linear Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)

# Display the values of b1, b0, and r
print(f"b1 (slope): {b1}")
print(f"b0 (y-intercept): {b0}")
print(f"Coefficient of linear correlation (r): {r}")
print(f"Coefficient of determination (r^2): {r_squared}")

plt.show()
