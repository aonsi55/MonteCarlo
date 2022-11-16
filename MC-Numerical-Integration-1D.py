# This code is for 1 dimension integration
import numpy as np
import pandas as pd
import random
# n is the total number of points to be generated
n=1*10**3;
# N is the number of loop repetitions
N=1*10**3;
int_list = [];
for i in range(1,N):
    a= 0;
    b= 1;
    x = np.random.uniform(a,b,n)
    Integrand = x**2;
    length = b-a;
    df = pd.DataFrame({'x':x,'Integrand':Integrand})
    Average_Func= sum(df['Integrand'])/len(df['Integrand'])
    Integration = Average_Func*length
    int_list.append(Integration)
Average_Int = sum(int_list)/len(int_list)
print(Average_Int)
