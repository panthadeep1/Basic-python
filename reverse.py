##Author: panthadeep_b; IST: 11.11 IST
##WAP to reverse a string

import sys
import numpy as np
import math
from array import *

word = input("Enter the string: ");
#print(len(word));

wLen = len(word);
revList = [""]*wLen;
j = 0;
for i in range(wLen-1,-1,-1):
   revList[j] = word[i];
   j += 1;
   
print("The reverse of '",word,"'is:", end="'");
for i in range(0,len(revList)):
   print(revList[i], end="");
   
print("'\n");
