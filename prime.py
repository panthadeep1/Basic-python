##WAP to check for prime number
##Author: panthadeep_b; 16Jan25, 12:00pm

import sys
import numpy as np
import math
from array import *


num = int(input("Enter the number: "));
c_root = math.floor(math.sqrt(num));
count = c_root-1;
flag = 0;

##Logic: loop till sqrt
for i in range(2,c_root+1):
   if(num%i == 0):
     print(num," is not prime");
     break;
   else:
     flag += 1;
     
     
##Check for prime
if(flag == count):
  print(num,"is prime");

