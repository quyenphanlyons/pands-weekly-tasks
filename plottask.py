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

# Show x.
print(x)

# Histogram.
plt.hist(x, bins=20, color = 'orange', edgecolor='black', label='Histogram of normal distribution', alpha=0.5)

# Put the copy of the histogram as "plottask histogram" to my repository
plt.savefig("task8_histogram.png")


# Plotting.
import matplotlib.pyplot as plt
# Numerical arrays.
import numpy as np

# Create y composed by 10 value from 0 to 10
y = np.linspace(0.0, 10.0, 0.1)

# h(x)=x3
z = pow(y,3)

# Show y.
print(y)
print(z)

# Plot x vs y.
plt.plot(y, z, label='z = y3')

# Add a legend.
plt.legend()

# Add labels.
plt.xlabel('y')
plt.ylabel('$y^3$')

# Add a title.
plt.title('function  h(y)=y3')

plt.savefig("task8_plot_funtion.png")

# Resources
# https://www.w3schools.com/python/matplotlib_histograms.asp
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
