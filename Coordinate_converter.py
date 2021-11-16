import pandas as pd
import numpy as np
import csv
from matplotlib import pyplot as plt
import statistics as stat
from PIL import Image, ImageDraw

Data_log = pd.read_csv('/Users/arthurguy/Documents/MOREK/Data_processing/16_nov_2021/GPS_14.CSV',usecols = ['Latitude','Hemisphere (N-S)','Longitude','Hemisphere (E-W)'])

Data_log.rename(columns={'Hemisphere (N-S)': 'HEM_NS','Hemisphere (E-W)':'HEM_EW'}, inplace=True)


print(Data_log)

def dm(x):
    degrees = int(x) // 100
    minutes = x - 100*degrees

    return degrees, minutes

def decimal_degrees(degrees, minutes):
    return degrees + minutes/60 

Updated_coords = pd.DataFrame(columns=['Latitude','Longitude'])

for i in range(0,len(Data_log)):
    
    if Data_log.HEM_NS[i] == 'N':
    
        Updated_coords.loc[i,['Longitude']] = -decimal_degrees(*dm(Data_log.Longitude[i]))
    
    else:
        
        Updated_coords.loc[i,['Longitude']] = +decimal_degrees(*dm(Data_log.Longitude[i]))
        
    
    if Data_log.HEM_EW[i] == 'E':
    
         Updated_coords.loc[i,['Latitude']] = -decimal_degrees(*dm(Data_log.Latitude[i]))
    
    else:
        
        Updated_coords.loc[i,['Latitude']] = +decimal_degrees(*dm(Data_log.Latitude[i]))


Updated_coords.to_csv('/Users/arthurguy/Documents/GitHub/GPS-visualization-Python/Updated_GPS_14.csv')

