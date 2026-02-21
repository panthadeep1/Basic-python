##Author: panthadeep_b; IST: 13.45 IST
##WAP to compute factorial of a number

import sys
import numpy as np
import math
from array import *

##Read the #rows, #cols
fp = open("matrix-data", "rt");
dimension = fp.readline();
#fp.close();

myDim = [int(i) for i in dimension.split()];
nrow = myDim[0]; 
ncol = myDim[1];  
print("#Rows:",nrow,"#Colums:",ncol);


##Load data-file
data_matrix = [];
for i in range(0,nrow):
   record = [];
   line = fp.readline();
   record = [int(j) for j in line.split()];
   data_matrix.insert(i,record);

fp.close();      

##Display data-matrix
for i in range(0,nrow):
   print(data_matrix[i]);
   
   

      
