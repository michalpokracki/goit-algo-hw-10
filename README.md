## Homework 10: Production Optimization and Monte Carlo Integration

### Task 1: Production Optimization

The PuLP library was used to create a linear programming model to maximize beverage production given resource constraints. The optimal solution indicates the number of lemonade and fruit juice units that should be produced for maximum total output.

### Task 2: Monte Carlo Integration

The definite integral of the function f(x) = x^2 from 0 to 2 was calculated using the Monte Carlo method. The calculated value was then compared to the result obtained using SciPy's `quad` function (a numerical integration method).  

**Observations:**

*   The Monte Carlo method provided a reasonably accurate approximation of the definite integral.
*   The error between the Monte Carlo result and the quadrature result was 0.026165214137271686. This error can be reduced by increasing the number of random samples used in the Monte Carlo simulation.

**Conclusion:**

This homework demonstrates the application of linear programming for optimization and the Monte Carlo method for numerical integration.
