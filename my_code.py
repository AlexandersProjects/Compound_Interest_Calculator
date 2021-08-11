import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

# I want to make to calculate the compound interest and plot it on a graph from start till finish

# 1. User input

K = int(input("Insert starting capital: "))
p = int(input("Insert annual compounding: "))
n = int(input("Insert amount of years: "))

# 2. function

def Zinseszins_retainer(K, p, n, t, L_y):
    i = 0
    while i < n:
        K = K * (1+p/100)**t
        L_y.append(round(K, 2)) 
        i += 1
    
def x_values(n, L_x):
    x = 0
    while x <= n:
        x_values = x
        L_x.append(x_values)
        x += 1

def Zinseszins(K, p, n):
    Kn = K * (1+p/100)**n
    Kn = round(Kn, 2)
    return ("Compound Interest {} € \n with starting capital of {} € \n after {} years \n with compounding of {} %.".format(Kn, K, n, p))
     
L_y = [K]

L_x = []

Zinseszins_retainer(K, p, n, 1, L_y)

print(Zinseszins(K, p, n))

# 4. plotting results as a graph 

x_values(n, L_x)

plt.plot(L_x, L_y)

plt.xlabel("Time in years")


plt.ylabel("Money in €")

plt.title("Compound interest")


