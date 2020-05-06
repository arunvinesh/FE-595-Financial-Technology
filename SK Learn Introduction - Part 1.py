# FE-595-Financial Technology
# SK Learn Introduction - Part 1
# Arun Thiravianathan
# CWID 10444121

# Required Libraries
import numpy as np
import matplotlib.pyplot as plt

# As suggested, from sklearn, I only import the features needed
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston


# Creating the Linear Regression object
linear_reg = LinearRegression()

# Loading boston data sets
boston = load_boston()

# Defining the Y, the house price
boston_price = boston.target

# For identifying the greatest and the least influence predictor, I could use two approaches
# 1) move the results to a dataset using pandas, and sort asc and desc to take the greater and
#     the least
# 2) using the loop to compare the values and keep the min and max while doing it
# i decided to use the second option to simplify the code
min_coef = 10000
max_coef = -10000
min_pos = 0
max_pos = 0

# Although I will use the score function to calculate R2, I have included
# the code for calculating R (using the formula showed during class

# As Y is not going to change for the 13 predictors, the Standar deviation and mean are calculated outside
# the loop
ystd = np.std(boston_price)
ymean = np.mean(boston_price)

N = len(boston_price)

Factor1 = boston_price - ymean
Factor1 = Factor1/ystd

Ninv = 1/(N-1)

# Added loop in order to review the 13 predictors
for j in range(0,13,1):
    # I skip the predictor 4th (column 3) CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
    if j !=3:

        # Selecting as X the predictor on the J column
        boston_data = boston.data[:, np.newaxis, j]

        boston_regresion = linear_reg.fit(boston_data,boston_price)

        boston_R2 = linear_reg.score(boston_data,boston_price)

        # Although I don't use the calculation below, i added to confirm that R2 was the influence factor as explained in class.
        # I don't use this factor and I use the score, is R2 instead of R, removing the problem of dealing with negatives
        xstd = np.std(boston_data)
        xmean = np.mean(boston_data)

        Factor0 = boston_data - xmean
        Factor0 = Factor0/xstd
        boston_score = 0

        for h in range(1,N,1):
            boston_score = boston_score+(Factor0[h]*Factor1[h])
        boston_score = (boston_score*Ninv)


        if boston_R2 > max_coef:
            max_coef = boston_R2
            max_pos = j
        if boston_R2 < min_coef:
            min_coef = boston_R2
            min_pos = j

#printing the results
print("The less influence predictor is " ,boston.feature_names[min_pos]," with R2 = ",min_coef)
print("The most influence predictor is " ,boston.feature_names[max_pos]," with R2 = ",max_coef)