## Author: @panthadeep_b
##Created on: 18.Jan.25; 18.53 IST

import sys
import numpy as np
import math as math
from array import *

arr1 = np.array([[1,2],[3,4]]);
arr2 = np.array([[2,2],[4,4]]);

arr3 = np.add(arr1,arr2);
print(arr3,len(arr1));

arr = [1,2,3,4,5,6,7,8,9];
mean = np.mean(arr,axis=0);
print("The mean of arr is:", mean);

print("\nStd. deviation of arr : ", np.std(arr));  
print ("More precision with float32") 
print("std of arr : ", np.std(arr, dtype = np.float32)) 

print("\nVariance of arr : ", np.var(arr));  
print ("More precision with float32") 
print("var of arr : ", np.var(arr, dtype = np.float32)) 

##List with diff. item-type
listArr = [1,2,"cat",3];
for item in listArr:
    print(item);
    
arr = np.array([1,2,"tiger",3]);
for item in arr:
  print(item);
  
  
## Determinant of matrix
fp = open("matrix","rt");
matrix = [];
j = 0;
while(True):
     line = fp.readline();
     if(line == ""):
       break;
     else:         
       row = [int(i) for i in line.split()];
       matrix.insert(j,row);
       j += 1;
fp.close();       
       
print("The matrix is:\n", matrix);
det = np.linalg.det(matrix);
print("The determinant is:", int(det));

##Inverse of a matrix
inv_mat = np.linalg.inv(matrix);
print("The inverse of matrix is:", inv_mat);









  
  
