## Author: @panthadeep_b
##Created on: 16.Jan.25; 13:27 IST
##WAP to print the Fibonacci number

import sys
import numpy as np
import math as math
from array import *


def fib(num):
   if(num == 0 or num==1):
     fibList[num] = num;
     return fibList[num];
   else:
     fibList[num] = fib(num-1) + fib(num-2);
     return fibList[num];     


N = int(input("Enter the index:"));
fibList = [0]*(N+1);
val = fib(N);
print("The Fibonacci series is:",fibList);
      
   

   
  
