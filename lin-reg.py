## Author: @panthadeep_b
##Created on: 25.Jan.25; 23.01 IST
#WAP to implement linear regression

import sys
import numpy as np
import pandas as pd
import math as math
from array import *
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  

data_set = pd.read_csv("data.csv");
              
df = pd.DataFrame(data_set); 
print(df);

##Display years
yrs = df.iloc[:,0];
x = yrs;
print("#Years =",len(x));
#print(x);

##Display Salary
sal = df.iloc[:,1];
y = sal;
print("#Salaries($) =",len(y));
#print(y);

x = x.to_numpy().reshape(len(x),1); ## # Reshape for compatibility with scikit-learn
y = y.to_numpy().reshape(len(y),1);

##Splitting the dataset into training and test set
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.3, random_state=1);

##Display the train, test data
print("X_train\n", x_train);
print("Y_train\n", y_train);
print("X_test\n", x_test);
print("Y_test\n", y_test);

# Plot the test data
plt.scatter(x_test, y_test, color='black');
plt.title('Test Data');
plt.xlabel('Size');
plt.ylabel('Price');
plt.xticks(());
plt.yticks(());

##Train the Linear Regression model
model = LinearRegression();
model.fit(x_train, y_train);

##Plot predictions
plt.plot(x_test, model.predict(x_test), color='red', linewidth=3);
plt.show();




   



   
   
   
   
   
