## Author: @panthadeep_b
##Created on: 16.Jan.25; 12:35 IST
##WAP to print the digits of a number

import sys
import numpy as np
import math as math
from array import *

num = int(input("Enter the number: "));
#Logic
digList = [];
while(num > 0):
     r = int(num%10);
     digList.append(r); 
     q = int(num/10);
     num = q;
     
digList.reverse();

print("The digits are:");
print(digList);
