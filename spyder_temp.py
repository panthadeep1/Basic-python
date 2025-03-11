# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import sys
import math
import numpy as np
from array import *
import matplotlib.pyplot as plt

##Read file
mat = [];
j = 0;
fp = open("matrix","rt");
for line in fp.read():
    print(line,end="");
