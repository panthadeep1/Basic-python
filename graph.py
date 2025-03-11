##Author: panthadeep_b; IST: 13.45 IST
##WAP to compute factorial of a number

import sys
import numpy as np
import math
from array import *

##Functions

##Read the #rows, #cols
fp = open("input.txt", "rt");
dimension = fp.readline();
#fp.close();

myDim = [int(i) for i in dimension.split()];
nrow = myDim[0]; 
ncol = myDim[1];  
print("#Rows:",nrow,"#Colums:",ncol);


##Load data-file
data_matrix = [];
for i in range(0,nrow):
   line = fp.readline();
   record = [int(j) for j in line.split()];
   data_matrix.insert(i,record);

fp.close();      

##Display data-matrix
print("The data-matrix is:");
for i in range(0,nrow):
   print(data_matrix[i]);
   
   
                                             ### ------------------------  Create the graph matrix ----------------- ###

##Initialize graph-matrix
graph_matrix = []; 
for i in range(0,nrow):                                             
      temp = [0]*nrow;                                       
      graph_matrix.insert(i,temp);
      
      
##Display initial graph-matrix
print("The initial graph-matrix is:");
for i in range(0,nrow):
   print(graph_matrix[i]);  
   
   

                                            ## ------------------- Find the edge-weights in the graph matrix ---------- ###
p_x = [];
p_y = [];      
for i in range(0,nrow):
   for j in range(0,nrow):
      p_x = data_matrix[i];
      p_y = data_matrix[j];
      #print(p_x,p_y);
      d_xy = math.dist(p_x,p_y);
      graph_matrix[i][j] = d_xy;      
      
      
print("The graph-matrix is:");
for i in range(0,nrow):
   print("Point ", i, "]:", graph_matrix[i], end="\n");  
                                    
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
                                             
      
