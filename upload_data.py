import pandas as pd
from sqlalchemy import create_engine
from time import time

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

df_iter = pd.read_csv('yellow_tripdata_2021-07.csv', chunksize=100000, iterator=True)

while True:
    try:
        t_start = time()
        df = next(df_iter)
        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
        df.to_sql('yellow_taxi_data', con=engine, if_exists='append')
        t_end = time()
        print(f'Processed 100k rows in {t_end - t_start:.2f} seconds.')
    except StopIteration:
        break
