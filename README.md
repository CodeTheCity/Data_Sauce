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

| 8554 P1 - 5331 P1 | 0.806795 |
| 8554 P2 - 5331 P2 | 0.672858 |

|       | 8554 P1 |  8554 P2 |  5331 P1 |  5331 P2 |  7789 P1 |  7789 P2 |  8733 P1 |  8733 P2 |
| 8554 P1  | 1.000000  | 0.806136  | 0.806795  | 0.672858  | 0.840279  | 0.831465  | 0.956321 | 0.802631 | 
| 8554 P2  | 0.806136  | 1.000000  | 0.825503  | 0.908280  | 0.748312  | 0.951232  | 0.847816 | 0.970601 | 
| 5331 P1  | 0.806795  | 0.825503  | 1.000000  | 0.836989  | 0.842277  | 0.576268  | 0.194654 | 0.280588 | 
| 5331 P2  | 0.672858  | 0.908280  | 0.836989  | 1.000000  | 0.598220  | 0.691692  | 0.240922 | 0.375951 | 
| 7789 P1  | 0.840279  | 0.748312  | 0.842277  | 0.598220  | 1.000000  | 0.785310  | 0.815039 | 0.735226 | 
| 7789 P2  | 0.831465  | 0.951232  | 0.576268  | 0.691692  | 0.785310  | 1.000000  | 0.774963 | 0.929308 | 
| 8733 P1  | 0.956321  | 0.847816  | 0.194654  | 0.240922  | 0.815039  | 0.774963  | 1.000000 | 0.860166 | 
| 8733 P2  | 0.802631  | 0.970601  | 0.280588  | 0.375951  | 0.735226  | 0.929308  | 0.860166 | 1.000000 | 


8554 P1  
8554 P2  
5331 P1  
5331 P2  
7789 P1  
7789 P2  
8733 P1   
8733 P2  
