# Weekly Task 8
# Write a program called plottask.py that displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axesy..
# Some marks will be given for making the plot look nice (legend etc).
# Please put a copy of the image of the plot (.png file) into the repository

# Plotting.
import matplotlib.pyplot as plt
# Numerical arrays.
import numpy as np

# Group 1: Mean = 5, Std Dev = 2, Size = 1000
x = np.random.normal(5, 2, 1000)

# Group 2: 
# Create y composed by 11 values from 0 to 10 (in my case, I just create 11 value, including 0 and 10, it can be any number of value)
y = np.linspace(0, 10, 11)

# Create z which is h(y)=y3, I use function pow() to calculate z from y, another way to calculate z is z = y**3
z = pow(y,3)

# Histogram of group 1
plt.hist(x, bins=20, color = 'orange', edgecolor='black', label='Normal distribution mean of 5 and standard deviation of 2', alpha=0.5)

# Plot the fucntion h(y)=y3
plt.plot(y, z, label='h(x) = x3', color = 'green')

# Add title and labels
plt.title('Histogram and Function Plot on Same Axes')
plt.xlabel('x')
plt.ylabel('Density / h(x)')
plt.legend()

# put a copy of the image of the plot (.png file) into the repository
plt.savefig("task8_plot.png")

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# Resources
# https://www.w3schools.com/python/matplotlib_histograms.asp
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html

