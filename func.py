##WAP to test for functions
##Author: panthadeep_b; Time: 15:33 IST

import sys
import numpy as np
import math
from array import *

##Func: Add
def fun_add(a,b):
   return(a + b);

##Func: Sub
def fun_sub(a,b):
    return(a-b);

##Func: Mul
def fun_mul(a,b):
    return(a*b);

##Func: Div
def fun_div(a,b):
    return(a/b);

##Func: Mod
def fun_mod(a,b):
    return(a%b);

num1 = 2
num2 = 3

print("Function options:");
print("1 -- Add\n 2 -- Subtraction\n 3 -- Multiplication\n 4 -- Division\n 5 -- Modulus");

##Enter func. option
opt = input("\nEnter the func. option:");
opt = int (opt); ##Type-cast from char-to-int

if(opt == 1):
    print("Perform addition:");
    add = fun_add(num1,num2);
    print("Result:", add);
elif(opt == 2):
    print("Perform subtraction:");
    sub = fun_sub(num1,num2);
    print("Result:", sub);
elif(opt == 3):
    print("Perform multiplication:");
    mul = fun_mul(num1,num2);
    print("Result:", mul);
elif(opt == 4):
    print("Perform division:");
    div = fun_div(num1,num2);
    print("Result:", div);
elif(opt == 5):
    print("Perform modulus:");
    mod = fun_mod(num1,num2);
    print("Result:", mod);
else:
    print("Out of listed operations");





    











  
