#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# SEA4001W Intro to Data Science
# Assignment P2
# Vivienne Banks
# BNKVIV001
# 10/03/2026

# Import Packages
import pandas as pd
import matplotlib.pyplot as plt



# Load the data file as a dataframe
df = pd.read_csv("P1_for_nit_picker_CTD_temp_salinity_depth_20081129_v01.dat", sep="\s+")  # Read data as space separated



# Display data frame
# print(df.head()) # Prints the first few rows of the data set
# print(df) # Prints the entire data set

# Create figure
fig, ax = plt.subplots(1, 2, sharey = True)

# Temperature
ax[0].plot(df["Temp_C"], df["Depth_m"], color="red")
ax[0].set_xlabel("Temperature (°C)")
ax[0].set_ylabel("Depth (m)")
ax[0].invert_yaxis()
ax[0].set_title("Temperature Profile")

# Salinity profile
ax[1].plot(df["Salinity_psu"], df["Depth_m"], color="blue")
ax[1].set_xlabel("Salinity (PSU)")
ax[1].set_title("Salinity Profile")

plt.tight_layout()

# Show and Save figure
plt.savefig("ctd_profiles.png")
plt.show()