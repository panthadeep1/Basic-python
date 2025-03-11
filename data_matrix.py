## Author: @panthadeep_b
##Created on: 06.Jan.25; 20.38 IST

import sys
import numpy as np
import math as math
from array import *

fp = open("data","rt");
dim = fp.readline(); #Read first line (dimensions)
#fp.close();

dimList = [int(i) for i in dim.split()]; ##Read & parse row
nrow = dimList[0];
ncol = dimList[1];
print("#Rows:", nrow, "#Columns:", ncol); 


##Load data-matrix
data_matrix = []; ##2-D list 
for i in range(0,nrow):
   line = fp.readline();
   rec = [int(i) for i in line.split()]; ## Entire row in encoded to list rec[]
   data_matrix.insert(i,rec);
   
##Display data-matrix
for i in range(0,nrow):
   print(data_matrix[i]);   
