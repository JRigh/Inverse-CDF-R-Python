#--------------------------
# Inverse CDF examples in R
#--------------------------

library(tidyverse)

#--------------------------------
# example 1: Weibull realizations
#--------------------------------

# 1. Define Inverse CDF function
Inverse_CDF_Weibull <-function(n, alpha, beta) {
   u <- runif(n)                                    # generate uniform numbers
   data <- beta*((-log(1-u))^(1/alpha))             # formula derived
   return(data.frame(data))                         # return the data
}

# 2. Generate realizations of the desired distribution
set.seed(2023)
dataset <- Inverse_CDF_Weibull(n = 1000, alpha = 5, beta = 2)
head(dataset)
#        data
# 1 1.8226044
# 2 1.6719235
# 3 1.4157089
# 4 1.7441408
# 5 0.9975117
# 6 1.3275159

# 3. Plot an Histogram with ggplot2
ggplot(dataset, aes(x=data)) + 
  geom_histogram(aes(y = ..density..), color="black", fill="darkred", binwidth = 0.1) +
  geom_density(alpha=.2, color = 'black', lwd = 1.2) +
  labs(title = 'Histogram of Weibull(5,2) realizations',
       subtitle = 'Inverse CDF generated artificial dataset',
       y="count", x="value") +
  theme(axis.text=element_text(size=8),
        axis.title=element_text(size=8),
        axis.text.x=element_text(angle=40, hjust=1),
        plot.subtitle=element_text(size=9, face="italic", color="darkred"),
        panel.background = element_rect(fill = "white", colour = "grey50"),
        panel.grid.major = element_line(colour = "grey90"))

# histogram in base R
# hist(data,main = "Histogram for realizations of W(5,2)", 
#      xlab = "x", col = "firebrick2")

#----
# end
#----