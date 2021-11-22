import pandas as pd
import numpy as np
import csv
import statistics as stat

Data_log = pd.read_csv('17_nov_2021/GPS_17.CSV',usecols = ['Time','Latitude','Hemisphere (N-S)','Longitude','Hemisphere (E-W)','Heading'])

Data_log.rename(columns={'Hemisphere (N-S)': 'HEM_NS','Hemisphere (E-W)':'HEM_EW'}, inplace=True)


print(Data_log)

def dm(x):
    degrees = int(x) // 100
    minutes = x - 100*degrees

    return degrees, minutes

def decimal_degrees(degrees, minutes):
    return degrees + minutes/60 

Updated_coords = pd.DataFrame(columns=['Time','Latitude','Longitude','Heading'])

for i in range(0,len(Data_log)):

    Updated_coords.loc[i,['Heading']] = Data_log.Heading[i]
    Updated_coords.loc[i,['Time']] = Data_log.Time[i]
    
    if Data_log.HEM_NS[i] == 'N':
    
        Updated_coords.loc[i,['Longitude']] = -decimal_degrees(*dm(Data_log.Longitude[i]))
    
    else:
        
        Updated_coords.loc[i,['Longitude']] = +decimal_degrees(*dm(Data_log.Longitude[i]))
        
    
    if Data_log.HEM_EW[i] == 'E':
    
         Updated_coords.loc[i,['Latitude']] = -decimal_degrees(*dm(Data_log.Latitude[i]))
    
    else:
        
        Updated_coords.loc[i,['Latitude']] = +decimal_degrees(*dm(Data_log.Latitude[i]))


Updated_coords.to_csv('Updated_GPS_17.csv')

