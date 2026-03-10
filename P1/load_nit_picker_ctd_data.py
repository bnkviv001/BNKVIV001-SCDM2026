# SEA4001W Intro to Data Science
# Assignment P1
# Vivienne Banks
# BNKVIV001
# 10/03/2026

# Import Packages
import pandas as pd

# Load the data file as a dataframe
df = pd.read_csv("P1_for_nit_picker_CTD_temp_salinity_depth_20081129.dat", sep="\s+")  # Read data as space separated



# Display data frame
print(df.head()) # Prints the first few rows of the data set
# print(df) # Prints the entire data set


