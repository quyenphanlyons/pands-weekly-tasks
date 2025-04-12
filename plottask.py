# Weekly Task 8
# Write a program called plottask.py that displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.
# Some marks will be given for making the plot look nice (legend etc).
# Please put a copy of the image of the plot (.png file) into the repository



# Plotting.
import matplotlib.pyplot as plt
# Numerical arrays.
import numpy as np

# Group 1: Mean = 5, Std Dev = 2, Size = 1000
x = np.random.normal(5, 2, 1000)

# Show.
print(x)

# Histogram.
plt.hist(x, bins=20, edgecolor='black')
plt.savefig("normalhistogram.png")



# Resources
# https://www.w3schools.com/python/matplotlib_histograms.asp
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
