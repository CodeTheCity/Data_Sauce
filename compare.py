import pandas as pd
import glob


def load(sensors): 
    full = {}
    hourly = {}
    for s in sensors:
        path = r'../abdn_air_quality/data/luftdaten/{sensor}/*.csv'.format(sensor=s)
        df = pd.concat([pd.read_csv(f, sep=';') for f in glob.glob(path)],ignore_index=True)
        df['datetime'] = pd.to_datetime(df['timestamp'])
        df = df.set_index('datetime')
        df.drop(['timestamp', 'sensor_id', 'sensor_type', 'durP1', 'durP2', 'location', 'lat', 'lon', 'ratioP1', 'ratioP2'], axis=1, inplace=True)
        dfh = df.resample('H').mean()
        full[s] = df
        hourly[s] = dfh
    return full, hourly

sensors = [5331 , 7789, 8554]
if __name__ == "__main__":
    
    full, hourly = load(sensors)
    #  print(frames[5331])
    hdf = pd.DataFrame()
    for k in full:
        full[k] = full[k].rename(columns={'P1': str(k)+' P1', 'P2': str(k)+' P2'})
       
    hdf = pd.concat(full.values(), axis=1)
    print(hdf.info())
    print(hdf.corr())

