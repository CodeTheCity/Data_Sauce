# Data_Sauce
team Data Sauce at CTC15

Looking at tracing through what data is where, what the flow is for the sensors putting it there, and any other data sources that might be useful. 

# previous work

https://github.com/watty62/abdn_air_quality

# Comparisons of luftdaten and other sensors

https://seetheair.wordpress.com/2019/02/07/purpleair-ii-vs-luftdaten/

http://plumeplotter.com/news/LuftDEFRA.pdf

# Sensors in Aberdeen

| Luftdaten_ID | Madavi_ID |latitude| longitude|
| :------ |:----------|:--------|:--------|
| 5331    | 3654427   |57.138  |-2.077   |
| 7789    | **tbc**   |57.130  |-2.087   |
| 8554    | 12017738  |57.146  |-2.114   |
| 8733    | 3654335   |57.136  |-2.107   |
| 15462   |  xxx  | xxx  |  xxx |
| 17079   |  xxx  | xxx  | xxx  |

# Dataflow

Sensor nodes submit readings to madavi which is then pulled to luftdaten 

# Scrape

We have scrape of the historical data for these sensors (where ID is known). 

https://github.com/watty62/abdn_air_quality/tree/master/data/luftdaten
Folder for each sensor, then file for results for each day.

 `sensor_id;sensor_type;location;lat;lon;timestamp;P1;durP1;ratioP1;P2;durP2;ratioP2`

# Comparison of sensors

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
