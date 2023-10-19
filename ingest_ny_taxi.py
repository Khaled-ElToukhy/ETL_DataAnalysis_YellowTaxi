import pandas as pd

from sqlalchemy import create_engine
from time import time 

engine = create_engine('postgresql://user:user@pgdatabase:5432/ny_taxi')

engine.connect()

df_lookup = pd.read_csv('taxi+_zone_lookup.csv')
df_lookup.head(0).to_sql(name= 'ny_zones', con= engine, if_exists= 'fail')
df_lookup.to_sql(name = 'ny_zones',con = engine,if_exists = 'replace')

df_iter = pd.read_csv('yellow_tripdata_2021-01.csv' ,iterator=True,chunksize=100000)


df=next(df_iter)

df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

df.head(0).to_sql(name = 'ny_taxi_trips',con = engine,if_exists = 'fail')


df.to_sql(name = 'ny_taxi_trips',con = engine,if_exists = 'append')
count = 2
while True:
    tstart = time()
    df = next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    
    df.to_sql(name = 'ny_taxi_trips',con = engine,if_exists = 'append')
    tend = time()
    print(f'inserted chunk ({count}).. time spent:{tend-tstart:.3f}')
    count = count + 1
    
    
