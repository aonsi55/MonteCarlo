# Python Library to Solve N-Dimensional Integration ``onsi-mc``

## Mathematical Basis: Evaluating N-Dimensional Integration with Monte Carlo Methods

Another problem which can be solved using Monte Carlo's method is numerical integration. From the definition of the average of a function we have:

$$\langle f(x) \rangle = \frac{1}{b-a} \int_a^b f(x) dx$$

which can be rearranged as:

$$\int_a^b f(x) dx = (b-a) \langle f(x) \rangle$$

From this, we can conclude that with a large number of random points, we can approximate the value of the integral. If we have a function $f(x)$ and want to evaluate the integral from $a$ to $b$, we:

- Generate a large number of random points in the interval $[a,b]$ 
- Calculate the average value of $f(x)$ at these random points
- = Multiply this average by the length of the interval $(b-a)$

### Extension to Higher Dimensions 

This concept extends to 2D, 3D, and higher dimensional integrals:

For a 2D integral:

$$\langle f(x,y) \rangle = \frac{1}{b_x-a_x} , \frac{1}{b_y-a_y} , \int_{a_y}^{b_y} \int_{a_x}^{b_x} f(x,y) , dx , dy$$

Rearranged as:

$$\int_{a_y}^{b_y} \int_{a_x}^{b_x} f(x,y) , dx , dy = (b_x-a_x)(b_y-a_y) \langle f(x,y) \rangle$$

For a 3D integral:

$$\int_{a_z}^{b_z} \int_{a_y}^{b_y} \int_{a_x}^{b_x} f(x,y,z) , dx , dy , dz = (b_x-a_x)(b_y-a_y)(b_z-a_z) \langle f(x,y,z) \rangle$$

A general pattern emerges for $N$-dimensional integrals:

$$\int_{a_N}^{b_N} \cdots \int_{a_2}^{b_2} \int_{a_1}^{b_1} f(x_1, x_2, \ldots, x_N) , dx_1 , dx_2 , \ldots , dx_N = \left[\prod_{i=1}^N (b_i-a_i) \right] \cdot \langle f(x_1,x_2, \ldots, x_N) \rangle$$

What's impressive is that the difficulty of integrating a higher-order integral doesn't increase significantly with Monte Carlo methods, making it suitable for complex integrals.

# Python Implementation Example
A python library onsi-mc has been published on PyPI, which can be installed using 
```
pip install onsi-mc
```

### Quick Start

We will use the library to evaluate the following integral,

$$\int_0^{\pi/2} ~ \int_0^{\pi} ~ \int_0^1 ~ e^{-x_1^2} ~ \sin{x_2} ~ \cos{x_3} ~ d x_1 ~ d x_2 ~ d x_3$$

```
import numpy as np
from onsi_mc import ND

# Define a function to integrate
def func(x1, x2, x3):
    """3D integration function with vectorized support"""
    return np.exp(-x1**2) * np.sin(x2) * np.cos(x3)

# Create integrator with integration bounds
mc = ND(func, 0.0, 1.0, 0.0, np.pi, 0.0, np.pi/2)

# Run the integration
result = mc.run()

# Plot convergence analysis
mc.plot(save=True)
```
### API Reference
ND class: `ND(func, *args, n=50000, N=1000, convergence_threshold=0.1, use_numba=True)`
- `func`: Function to integrate. Must accept N arguments.
- `*args`: Integration bounds. Must be in pairs for each dimension. For example, for 3D: `a1, b1, a2, b2, a3, b3`.
- `n`: Number of random points to sample. Default is 50,000.
- `N`: Number of iterations for convergence analysis. Default is 1,000.
- `convergence_threshold`: Threshold for convergence analysis. Default is 0.5.
- `use_numba`: If True, uses Numba for JIT compilation. Default is True.

#### Methods
`run(verbose=True, progress_bar=True)`
This method runs the Monte Carlo integration and returns the result.
- `verbose`: If True, prints the result. Default is True.
- `progress_bar`: If True, shows a progress bar. Default is True.

`plot(show=True, save=False, filename=None)`
Visualizes convergence analysis.
- `show`: If True, displays the plot. Default is True.
- `save`: Saves plot to file. Default is False.
- `filename`:  Custom filename (default: "mc_convergence_n{n}_N{N}.png").


### Example Usage
A simple usage case for 1D integral evaluation, 

$$\int_0^2 ~ x^3 - 2 x + 1 ~ dx$$

```
from mc import ND
import numpy as np

# 1D integration example: ∫(x³ - 2x + 1)dx from 0 to 2
def f1d(x):
    return x**3 - 2*x + 1

# Create integrator with 0 to 2 limits
mc1 = ND(f1d, 0, 2)
result1 = mc1.run()

# 3D integration example
def f3d(x, y, z):
    return np.exp(-x**2) * np.sin(y) * np.cos(z)

# Create integrator with limits [0,1] × [0,π] × [0,π/2]
mc3 = ND(
    f3d, 
    0.0, 1.0,   # x limits
    0.0, np.pi, # y limits
    0.0, np.pi/2 # z limits
)

# Run with default settings
result3 = mc3.run()

# Plot convergence analysis
mc3.plot(save=True)
```

### Expected Output
When running the integration, you'll see one of two outcomes:
1. Successful Convergence
If the integration converges properly (standard deviation difference is below threshold):
```
Integrating: 100%|██████████| 1000/1000 [00:02<00:00, 396.60it/s]
Estimated integral: 0.60653211
```
The function returns this value, which you can use in subsequent calculations.

2. Non-Convergence Warning
If the integration fails to converge (standard deviation difference exceeds threshold):
```
Integrating: 100%|██████████| 1000/1000 [00:03<00:00, 327.42it/s]
Warning: Possible non-convergence (Δstd = 0.1237 > threshold = 0.1000)
Estimated integral: 0.60912458
```

In this case, the function returns None to indicate possible unreliability, though you can still access the estimated value as shown in the output message.

You can visualize the convergence behavior using the plot() method to determine whether increasing N or adjusting other parameters might help achieve convergence.

___________

Feel free to contact me, if you need help. 
aonsi@alexu.edu.eg
