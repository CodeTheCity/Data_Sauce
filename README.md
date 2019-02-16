# Data_Sauce
team Data Sauce at CTC15

Looking at tracing through what data is where, what the flow is for the sensors putting it there, and any other data sources that might be useful. 

# previous work

https://github.com/watty62/abdn_air_quality

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
