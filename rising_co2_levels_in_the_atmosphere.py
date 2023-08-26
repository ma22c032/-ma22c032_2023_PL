# -*- coding: utf-8 -*-
"""Rising CO2 levels in the atmosphere

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mEFSqc2UwktMO3cNAahzn5nyio8M12cS
"""

!pip install gitpython

!pip install numpy matplotlib scipy

import urllib.request
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Step 1: Downloading Data
url = "ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt"
data_filename = "co2_data.txt"

urllib.request.urlretrieve(url, data_filename)

# Step 2: Data Munging
# Load data and mask missing values
data = np.genfromtxt(data_filename, skip_header=72)  # Skip header rows
data = np.ma.masked_invalid(data)  # Mask missing values

# Step 3: Extract Monthly Averages
monthly_averages = data[:, 3]  # Assuming the "average" column is at index 3

# Step 4: Plot Monthly Averages
plt.plot(data[:, 2], monthly_averages)
plt.xlabel("Year")
plt.ylabel("CO2 Monthly Average (ppm)")
plt.title("Monthly Average CO2 Levels Over Time")
plt.grid(True)
plt.show()

# Step 5: Estimate Rate of Change
# Calculate differences between consecutive monthly averages
differences = np.diff(monthly_averages)

# Convert to rates by dividing by time interval (assuming monthly data)
time_intervals = np.diff(data[:, 2])
rate_of_change = differences / time_intervals

# Step 6: Plot Rate of Change
plt.plot(data[:-1, 2], rate_of_change)  # Plot rate_of_change vs. time
plt.xlabel("Year")
plt.ylabel("Rate of Change (ppm/year)")
plt.title("Estimated Rate of Change of CO2 Levels Over Time")
plt.grid(True)
plt.show()