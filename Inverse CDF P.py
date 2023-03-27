#-------------------------------
# Inverse CDF examples in Python
#-------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

#--------------------------------
# example 1: Weibull realizations
#--------------------------------

# 1. Define Inverse CDF function
def Inverse_CDF_Weibull(n, alpha, beta) :
        u = np.random.uniform(low=0.0, high=1.0, size=n)          # generate uniform numbers
        data = beta*((-np.log(1-u))**(1/alpha))                   # forumla derived
        
        return pd.DataFrame(data = data, columns = ['data'])      # return a data frame instead of an arry

# 2. Generate realizations of the desired distribution
np.random.seed(2023)
dataset = Inverse_CDF_Weibull(n = 1000, alpha = 5, beta = 2)
dataset.head()
#   	data
#0	1.655497
#1	2.343973
#2	1.952544
#3	1.340683
#4	1.372833

# 3. Plot with seabortn
plot = sns.histplot(dataset, kde = True, bins = 20, facecolor="darkred", edgecolor='black')
plot.set(title='Histogram of Weibull(5,2) realizations')
plot.set(xlabel="value")

#----
# end
#----