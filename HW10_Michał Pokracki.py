# Homework for Topic 10:

# Task 1: Production Optimization using PuLP

from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Problem Definition
problem = LpProblem("Maximize_Beverage_Production", LpMaximize)

# Decision Variables (how many units of each beverage to produce)
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Objective Function (maximize total beverage production)
problem += lemonade + fruit_juice, "Total_Beverages"

# Constraints (resource limitations)
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solve the Problem
problem.solve()

# Display Optimal Solution
print(f"Optimal number of Lemonade units to produce: {lemonade.varValue}")
print(f"Optimal number of Fruit Juice units to produce: {fruit_juice.varValue}")
print(f"Maximum total number of products: {value(problem.objective)}")

# Task 2: Monte Carlo Integration

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Function to Integrate
def f(x):
    return x ** 2

# Integration Limits
a = 0
b = 2

# Plotting the function and integration area
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r', linewidth=2)
plt.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
plt.xlim([x[0], x[-1]])
plt.ylim([0, max(y) + 0.1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Graph of integration of f(x) = x^2 from {a} to {b}')
plt.grid(True)
plt.show()

# Monte Carlo Integration
N = 10000  # Number of random samples
random_x = np.random.uniform(a, b, N)
function_values = f(random_x)
monte_carlo_integral = (b - a) * np.mean(function_values)

# Verification using Scipy's quad function
quad_integral, quad_error = spi.quad(f, a, b)

print("Monte Carlo Integral:", monte_carlo_integral)
print("Quadrature Integral:", quad_integral)
print("Error:", abs(monte_carlo_integral - quad_integral))
