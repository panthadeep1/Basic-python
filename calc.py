# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:31:16 2024

@author: admin
"""

import numpy as np
import math as math

## Exponent
print("Exponent");
a = input("Enter the value of a:")
b = input("Enter the value of b:")
e = math.pow(int(a), int(b))
print("The exponent is:", e)


##Square root
print("\nSquare root");
num = input("Enter the number");
sqr = math.sqrt(int(num));
print("The square-root of", num, " is:", sqr);


#Prime number
print("\nPrime number");
num = input("Enter the number: ");
sqr = math.sqrt(int(num));
num_sqr = math.floor(sqr);
print("The floor of square root is:", num_sqr);

flag = 2;
for i in range(2,num_sqr+1):
    if(int(num) % i == 0):
        flag += 1;
        break;
        
        
if(flag > 2):
   print(num, "is not prime");
elif(flag == 2):
   print(num, "is prime"); 






