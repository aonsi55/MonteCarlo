## Evaluating N-Dimensional Integration with Monte Carlo Methods
### Mathematical Basis
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

### Python Implementation Example
The following Python code demonstrates how to integrate a one-dimensional integral:

$$\int_{\pi/2}^{\pi} \cos^2(x) \cdot e^{3x} \cdot \sin(x) \cdot x^3 , dx$$

```
import numpy as np
import pandas as pd
import random
import math 

# n is the total number of points to be generated
n = 1*10**3
# N is the number of loop repetitions
N = 1*10**3
int_list = []

for i in range(1,N):
    a = (math.pi)/2
    b = math.pi
    x = np.random.uniform(a,b,n)
    Integrand = []
    lengthx = b-a
    
    for i in range(0,n):
        Integrand.append((math.cos(x[i]))**2*(math.exp(x[i]))*x[i]**3*math.sin(x[i]))
        
    df = pd.DataFrame({'x':x,'Integrand':Integrand})
    Average_Func = sum(df['Integrand'])/len(df['Integrand'])
    Integration = Average_Func*lengthx
    int_list.append(Integration)
    
Average_Int = sum(int_list)/len(int_list)
print(Average_Int)

```

The output of this code yields an average of 72.808, while the exact value calculated using Wolfram Alpha is 72.7. This is remarkably accurate, considering the complexity of the integration. The execution time is only around 3.8 seconds for 1000 generated points, with the process repeated 1000 times.


--------------


# Monte Carlo's integration

- In this repository, we are going to write a code to integrate a 1D dimensional integration using Monte Carlo, this method can be extended to higher order dimensional integration. 



- The example integration being solved for is, 

$$\int_0^1 x^2 dx$$

- The code is written and executed using python 3. In order to use the code you need to make sure that numpy package is installed in your device, else the code will throw an error, you can check whether the package is installed via terminal for linux using the following 
```
pip3 show numpy
```
If the package is installed, the code would pirnt out the version information of the package, else you can use the following called to have numpy installed in your device,
```
pip3 install numpy
```


Feel free to contact me, if you need help. 
aonsi@alexu.edu.eg
