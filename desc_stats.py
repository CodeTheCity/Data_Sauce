import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

in_frame = pd.read_csv('ABZ_P_data.csv')

#print(in_frame.head(5))

level = 40 #safety level assumed to be 40 micro grams per cubic metre

sensors = ['5331 P1','5331 P2','7789 P1','7789 P2','8554 P1','8554 P2','8733 P1','8733 P2']

for s in sensors:
    col = in_frame[s]
    col.dropna(axis=0,how='any',inplace=True)
    """
    print('descriptive stats for ',s,' ',stats.describe(col))
    print(s,' median',col.median(),
        ' lower decile: ', col.quantile(0.10),
        ' lower quartile: ',    col.quantile(0.25),
        ' higher quartile: ',   col.quantile(0.75),
        ' 9th decile: ' ,    col.quantile(0.90))
    print('count of instances where particulate matter > ',level,' micro grams per cubic meter: ', len(col[col > level]) )
    """
    print('Percentage of life of sensor ',s,' where particulate matter > '
        ,level,' micro grams per cubic meter: ',
        (len(col[col > level]))/len(col)*100,' %')



"""
P1_5331_frame = in_frame['5331 P1']
#print(P1_5331_frame)
P1_5331_frame.dropna(axis=0,how='any',inplace=True)
#print(P1_5331_frame)
#plt.boxplot(P1_5331_frame)
print('descriptive stats for P1 5331',stats.describe(P1_5331_frame))
print('P1_5331 median',P1_5331_frame.median(),
    ' lower decile: ',    P1_5331_frame.quantile(0.10),
    ' lower quartile: ',    P1_5331_frame.quantile(0.25),
    ' higher quartile: ',    P1_5331_frame.quantile(0.75),
    ' 9th decile: ' ,    P1_5331_frame.quantile(0.90))
print('count of instances where particulate matter (2.5 micro meters)=> 40 micro grams per cubic meter: ', len(P1_5331_frame[P1_5331_frame > 40]) )
print('Percentage of life of sensor where particulate matter 2.5 micro meters) => 40 micro grams per cubic meter: ',
    (len(P1_5331_frame[P1_5331_frame > 40])/len(P1_5331_frame))*100,' %')


P2_5331_frame = in_frame['5331 P2']
P2_5331_frame.dropna(axis=0,how='any',inplace=True)
#plt.boxplot(P2_5331_frame)
print('descriptive stats for P2 5331',stats.describe(P2_5331_frame))
print('P2_5331 median: ',P2_5331_frame.median(),
    ' lower decile: ',    P2_5331_frame.quantile(0.10),
    ' lower quartile: ',    P2_5331_frame.quantile(0.25),
    ' higher quartile: ',    P2_5331_frame.quantile(0.75),
    ' 9th decile: ' ,    P2_5331_frame.quantile(0.90))
print('count of instances where particulate matter (10 micro meters)=> 40 micro grams per cubic meter: ', len(P2_5331_frame[P2_5331_frame > 40]) )
print('Percentage of life of sensor where particulate matter (10 micro meters) => 40 micro grams per cubic meter: ',
    (len(P2_5331_frame[P2_5331_frame > 40])/len(P2_5331_frame))*100,' %')
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.boxplot(P1_5331_frame)
ax1.set_title('sensor 5331')
ax2.boxplot(P2_5331_frame)

plt.show()

P1_7789_frame = in_frame['7789 P1']
P1_7789_frame.dropna(axis=0,how='any',inplace=True)
print('descriptive stats for P1 7789',stats.describe(P1_7789_frame))
print('median',P1_7789_frame.median(),
    ' lower decile: ',    P1_7789_frame.quantile(0.10),
    ' lower quartile: ',    P1_7789_frame.quantile(0.25),
    ' higher quartile: ',    P1_7789_frame.quantile(0.75),
    ' 9th decile: ' ,    P1_7789_frame.quantile(0.90))
print('count of instances where particulate matter (2.5 micro meters)=> 40 micro grams per cubic meter: ', len(P1_7789_frame[P1_7789_frame > 40]) )
print('Percentage of life of sensor where particulate matter 2.5 micro meters) => 40 micro grams per cubic meter: ',
    (len(P1_7789_frame[P1_7789_frame > 40])/len(P1_7789_frame))*100,' %')
P2_7789_frame = in_frame['7789 P2']
P2_7789_frame.dropna(axis=0,how='any',inplace=True)
print('descriptive stats for P2 7889',stats.describe(P2_7789_frame))
print('median',P2_7789_frame.median(),
    ' lower decile: ',    P2_7789_frame.quantile(0.10),
    ' lower quartile: ',    P2_7789_frame.quantile(0.25),
    ' higher quartile: ',    P2_7789_frame.quantile(0.75),
    ' 9th decile: ' ,    P2_7789_frame.quantile(0.90))
print('count of instances where particulate matter (10 micro meters)=> 40 micro grams per cubic meter: ', len(P2_7789_frame[P2_7789_frame > 40]) )
print('Percentage of life of sensor where particulate matter (10 micro meters) => 40 micro grams per cubic meter: ',
    (len(P2_7789_frame[P2_7789_frame > 40])/len(P2_7789_frame))*100,' %')
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.boxplot(P1_7789_frame)
ax1.set_title('sensor 7789')
ax2.boxplot(P2_7789_frame)

plt.show()

P1_8554_frame = in_frame['8554 P1']
P1_8554_frame.dropna(axis=0,how='any',inplace=True)
print('descriptive stats for P1 8554',stats.describe(P1_8554_frame))
print('median',P1_8554_frame.median(),
    ' lower decile: ',    P1_8554_frame.quantile(0.10),
    ' lower quartile: ',    P1_8554_frame.quantile(0.25),
    ' higher quartile: ',    P1_8554_frame.quantile(0.75),
    ' 9th decile: ' ,    P1_8554_frame.quantile(0.90))
print('count of instances where particulate matter (2.5 micro meters)=> 40 micro grams per cubic meter: ', len(P1_8554_frame[P1_8554_frame > 40]) )
print('Percentage of life of sensor where particulate matter 2.5 micro meters) => 40 micro grams per cubic meter: ',
    (len(P1_8554_frame[P1_8554_frame > 40])/len(P1_8554_frame))*100,' %')
P2_8554_frame = in_frame['8554 P2']
P2_8554_frame.dropna(axis=0,how='any',inplace=True)
print('descriptive stats for P2 8554',stats.describe(P2_8554_frame))
print('median',P2_8554_frame.median(),
    ' lower decile: ',    P2_8554_frame.quantile(0.10),
    ' lower quartile: ',    P2_8554_frame.quantile(0.25),
    ' higher quartile: ',    P2_8554_frame.quantile(0.75),
    ' 9th decile: ' ,    P2_8554_frame.quantile(0.90))
print('count of instances where particulate matter (10 micro meters)=> 40 micro grams per cubic meter: ', len(P2_8554_frame[P2_8554_frame > 40]) )
print('Percentage of life of sensor where particulate matter (10 micro meters) => 40 micro grams per cubic meter: ',
    (len(P2_8554_frame[P2_8554_frame > 40])/len(P2_8554_frame))*100,' %')
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.boxplot(P1_8554_frame)
ax1.set_title('sensor 8554')
ax2.boxplot(P2_8554_frame)

plt.show()

P1_8733_frame = in_frame['8733 P1']
P1_8733_frame.dropna(axis=0,how='any',inplace=True)
#print(P1_8733_frame.head(5))
print('descriptive stats for P1 8733',stats.describe(P1_8733_frame))
print('median',P1_8733_frame.median(),
    ' lower decile: ',    P1_8733_frame.quantile(0.10),
    ' lower quartile: ',    P1_8733_frame.quantile(0.25),
    ' higher quartile: ',    P1_8733_frame.quantile(0.75),
    ' 9th decile: ' ,    P1_8733_frame.quantile(0.90))
print('count of instances where particulate matter (2.5 micro meters)=> 40 micro grams per cubic meter: ', len(P1_8733_frame[P1_8733_frame > 40]) )
print('Percentage of life of sensor where particulate matter 2.5 micro meters) => 40 micro grams per cubic meter: ',
    (len(P1_8733_frame[P1_8733_frame > 40])/len(P1_8733_frame))*100,' %')
P2_8733_frame = in_frame['8733 P2']
P2_8733_frame.dropna(axis=0,how='any',inplace=True)
#print(P2_8733_frame.head(5))
print('descriptive stats for P2 8773',stats.describe(P2_8733_frame))
print('median',P2_8733_frame.median(),
    ' lower decile: ',    P2_8733_frame.quantile(0.10),
    ' lower quartile: ',    P2_8733_frame.quantile(0.25),
    ' higher quartile: ',    P2_8733_frame.quantile(0.75),
    ' 9th decile: ' ,    P2_8733_frame.quantile(0.90))
print('count of instances where particulate matter (10 micro meters)=> 40 micro grams per cubic meter: ', len(P2_8733_frame[P2_8733_frame > 40]) )
print('Percentage of life of sensor where particulate matter (10 micro meters) => 40 micro grams per cubic meter: ',
    (len(P2_8733_frame[P2_8733_frame > 40])/len(P2_8733_frame))*100,' %')
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.boxplot(P1_8733_frame)
ax1.set_title('sensor 8733')
ax2.boxplot(P2_8733_frame)

plt.show()
"""
