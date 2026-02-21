##Author: panthadeep_b; IST: 11.11 IST
##WAP to reverse a string

import sys
import numpy as np
import math
from array import *

word = input("Enter the string: ");
wlen = len(word);

##Initialize the forward/backward lists
fList = [""]*wlen;
bList = [""]*wlen;

for i in range(0,len(word)):
   fList[i] = word[i];

k = 0;   
for j in range(wlen-1,-1,-1):
   bList[k] = word[j];
   k += 1;
   
	
if(fList == bList):
  print("The string:<", word, "> is a Palindrome.");
else:
  print("The string:<", word, "> is NOT a Palindrome.");
