# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:31:16 2024

@author: admin
"""

import numpy as np
import math as math

## input, pow test prog.
"""
a = input("Enter the value of a:");
b = input("Enter the value of b:");
e = math.pow(int(a), int(b));
print("The exponent of ",a,"^",b,"is:", e);
"""

##Loop prog
print("While loop test:"); ##While loop
i = 1;
while(i<=10):
  print(i);
  i += 1;
  
##For loop
print("The current value of i is:",i);
print("For loop test:"); ##For loop
a = 1;
for i in range(i, 15):
    a = a+1;
    a = pow(2,a-1);
    print("a is:",a);

##List in for loop
myList = [1,2,"ram"];
print("The length of the list", myList, "is:", len(myList));
for i in range(0,len(myList)):
    print(myList[i], end=" "); 
    
print("\n");
strName = "panthadeep";
print("The length of the string \"", strName, "\" is:",len(strName));




