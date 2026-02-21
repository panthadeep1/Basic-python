##Author: panthadeep_b; IST: 11.11 IST
##WAP to reverse a string

import sys
import numpy as np
import math
from array import *

def fact(num):
   if(num == 0 or num == 1):
      return 1;
   else:
      return num*fact(num-1);
      

num = int(input("Enter number: "));      
print("The factorial of", num, "is:", fact(num)); 
      
