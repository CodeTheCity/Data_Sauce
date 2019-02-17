# Data_Sauce
team Data Sauce at CTC15

Looking at tracing through what data is where, what the flow is for the sensors putting it there, and any other data sources that might be useful. 

# previous work

https://github.com/watty62/abdn_air_quality

# Comparisons of luftdaten and other sensors

https://seetheair.wordpress.com/2019/02/07/purpleair-ii-vs-luftdaten/

http://plumeplotter.com/news/LuftDEFRA.pdf

# Sensors in Aberdeen

| Luftdaten_ID (particulates)| luftdaten_ID (temp)| Madavi_ID |latitude| longitude|
| :------ |:----------|:----------|:--------|:--------|
| 5331    | 5332 |3654427   |57.138  |-2.077   |
| 7789    | 7790 | **tbc**   |57.130  |-2.087   |
| 8554    | 8556 | 12017738  |57.146  |-2.114   |
| 8733    | 8734? | 3654335   |57.136  |-2.107   |
| 15462   |  15463 | xxx  | xxx  |  xxx |
| 17079   |  17080 | xxx  | xxx  | xxx  |

# Dataflow

Sensor nodes submit readings to madavi which is then pulled to luftdaten 

# Scrape

We have scrape of the historical data for these sensors (where ID is known). 

https://github.com/watty62/abdn_air_quality/tree/master/data/luftdaten
Folder for each sensor, then file for results for each day.

 `sensor_id;sensor_type;location;lat;lon;timestamp;P1;durP1;ratioP1;P2;durP2;ratioP2`

# Comparison of sensors

Pearrson correlation between sensors:

|       | 8554 P1 |  8554 P2 |  5331 P1 |  5331 P2 |  7789 P1 |  7789 P2 |  8733 P1 |  8733 P2 |
| :------ |:----------|:--------|:--------| :------ |:----------|:--------|:--------|:--------|
| 8554 P1  | 1.000000  |           | 0.806795  |           | 0.840279  |           | 0.956321 |          | 
| 8554 P2  |           | 1.000000  |           | 0.908280  |           | 0.951232  |          | 0.970601 | 
| 5331 P1  | 0.806795  |           | 1.000000  |           | 0.842277  |           | 0.194654 |          | 
| 5331 P2  |           | 0.908280  |           | 1.000000  |           | 0.691692  |          | 0.375951 | 
| 7789 P1  | 0.840279  |           | 0.842277  |           | 1.000000  |           | 0.815039 |          | 
| 7789 P2  |           | 0.951232  |           | 0.691692  |           | 1.000000  |          | 0.929308 | 
| 8733 P1  | 0.956321  |           | 0.194654  |           | 0.815039  |           | 1.000000 |          | 
| 8733 P2  |           | 0.970601  |           | 0.375951  |           | 0.929308  |          | 1.000000 | 

Spearman correlation between sensors (more valid since data is skewed and has outliers): 

|       | 8554 P1 |  8554 P2 |  5331 P1 |  5331 P2 |  7789 P1 |  7789 P2 |  8733 P1 |  8733 P2 |
| :------ |:----------|:--------|:--------| :------ |:----------|:--------|:--------|:--------|
| 8554 P1  |1.0| |0.81091697049| |0.896579489448| |0.946524972808| |
| 8554 P2  | |1.0| |0.833924379799| |0.906765734563| |0.957153474657|
| 5331 P1  |0.81091697049| |1.0| |0.833241977099| |0.870656302456| |
| 5331 P2  | |0.833924379799| |1.0| |0.874029415016| |0.870762759225|
| 7789 P1  |0.896579489448| |0.833241977099| |1.0| |0.854244472158| |
| 7789 P2  | |0.906765734563| |0.874029415016| |1.0| |0.89751895235|
| 8733 P1  |0.946524972808| |0.870656302456| |0.854244472158| |1.0| |
| 8733 P2  | |0.957153474657| |0.870762759225| |0.89751895235| |1.0|


Percentage of life of sensor  5331 P1  where particulate matter >  40  micro grams per cubic meter:  8.581590063270923  %
Percentage of life of sensor  5331 P2  where particulate matter >  40  micro grams per cubic meter:  0.5372465843391006  %
Percentage of life of sensor  7789 P1  where particulate matter >  40  micro grams per cubic meter:  6.69374880519977  %
Percentage of life of sensor  7789 P2  where particulate matter >  40  micro grams per cubic meter:  0.24804052762378132  %
Percentage of life of sensor  8554 P1  where particulate matter >  40  micro grams per cubic meter:  6.048349700648166  %
Percentage of life of sensor  8554 P2  where particulate matter >  40  micro grams per cubic meter:  0.4771080861061591  %
Percentage of life of sensor  8733 P1  where particulate matter >  40  micro grams per cubic meter:  11.28586575844231  %
Percentage of life of sensor  8733 P2  where particulate matter >  40  micro grams per cubic meter:  0.7775600038556694  %

