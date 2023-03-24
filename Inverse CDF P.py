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

# Inverse CDF function
def Inverse_CDF_Weibull(n, alpha, beta) :
        u = np.random.uniform(low=0.0, high=1.0, size=n)          # generate uniform numbers
        data = beta*((-np.log(1-u))**(1/alpha))                   # forumla derived
        
        return pd.DataFrame(data = data, columns = ['data'])      # return a data frame instead of an arry

# realizations and plot
np.random.seed(2023)
dataset = Inverse_CDF_Weibull(n = 1000, alpha = 5, beta = 2)
dataset
#   	data
#0	1.655497
#1	2.343973
#2	1.952544
#3	1.340683
#4	1.372833
#...	...
#995	2.069098
#996	2.056594
#997	1.996904
#998	2.001000
#999	1.925175

# plot
plot = sns.histplot(dataset, kde = True, bins = 20, facecolor="darkred", edgecolor='black')
plot.set(title='Histogram of Weibull(5,2) realizations')
plot.set(xlabel="value")
plot

#----
# end
#----

# import a file in .csv
odataset = pd.read_csv("path/dataset.csv")
 

# Then plot. Other examples will follow.
# Julian, march 2023