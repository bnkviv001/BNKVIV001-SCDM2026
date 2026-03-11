#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SEA4001W Intro to Data Science
# Assignment P2
# Vivienne Banks
# BNKVIV001
# 10/03/2026

# Import Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the data file as a dataframe
df = pd.read_csv("SAA2_WC_2017_metocean_10min_avg.csv", sep=",", parse_dates=["TIME_SERVER"],
    index_col="TIME_SERVER") 


# Display the data frame
print(df.head())
print(df.info())


# Selecting Data up until 4 July
df_subset_4_July = df.loc[:'2017-07-04']


# Temperature Time Series

plt.style.use("grayscale")

df_subset_4_July["TSG_TEMP"].plot()

plt.xlabel("Time (date)")

plt.ylabel("Temperature (°C)")
plt.title("Sea Surface Temperature Time Series")


plt.tight_layout()
plt.savefig("temperature_timeseries.png")
plt.show()



# Salinity Histogram

plt.hist(df_subset_4_July["TSG_SALINITY"], bins = np.arange(30, 35, 0.5))

plt.xlabel("Salinity (PSU)")
plt.ylabel("Frequency")
plt.title("Salinity Distribution")

plt.savefig("salinity_hist.png")
plt.show()


# Statistics of Temperature and Salinity

stats = pd.DataFrame({
    "Mean": df_subset_4_July[["TSG_TEMP","TSG_SALINITY"]].mean(),
    "Std Dev": df_subset_4_July[["TSG_TEMP","TSG_SALINITY"]].std(),
    "IQR": df_subset_4_July[["TSG_TEMP","TSG_SALINITY"]].quantile(0.75) -
           df_subset_4_July[["TSG_TEMP","TSG_SALINITY"]].quantile(0.25) })

stats.index = ["Temperature (ºC)", "Salinity (PSU)"]

print(stats)
stats.to_csv("temp_salinity_stats_table.csv")



def ddmm2dd(ddmm):     
    """     
    Converts a position input from degrees and minutes to degrees and decimals     
    Input is ddmm.cccc and output is dd.cccc     
    Note, it does not check if positive or negative     
    """     
    thedeg = np.floor(ddmm/100.)     
    themin = (ddmm-thedeg*100.)/60.     
    return thedeg+themin



# Scatter plot of wind speed and air temperature
plt.figure()


df_subset_4_July["LATITUDE"]=ddmm2dd(df_subset_4_July["LATITUDE"]) # Conver Latidue to degrees

sc = plt.scatter(
    df_subset_4_July["WIND_SPEED_TRUE"],
    df_subset_4_July["AIR_TEMPERATURE"],
    c=df_subset_4_July["LATITUDE"],
    cmap="viridis"
)

cbar = plt.colorbar(sc)
cbar.set_label("Latitude (°S)")
cbar.ax.invert_yaxis() 

plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Air Temperature (°C)")
plt.title("Wind Speed vs Air Temperature")

plt.savefig("wind_airtemp_scatter.png", dpi=300)
plt.show()

