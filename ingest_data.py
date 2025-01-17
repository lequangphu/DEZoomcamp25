import pandas as pd
import argparse
from sqlalchemy import create_engine
from time import time

def main(params):

    # parameters to create a connection to the database
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.database
    table = params.table

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    # parameter to load data
    url = params.url
    df = pd.read_csv(url, compression='gzip')
    csv_name = 'yellow_tripdata.csv'
    df.to_csv(csv_name, index=False)

    # read data input path and write to the database
    df_iter = pd.read_csv(csv_name, chunksize=100000, iterator=True)

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
            df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
            df.to_sql(table, con=engine, if_exists='append')
            t_end = time()
            print(f'Processed 100k rows in {t_end - t_start:.2f} seconds.')
        except StopIteration:
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # add arguments of postgresql engine connection and csv file path
    parser.add_argument('--user', type=str, help='PostgreSQL username')
    parser.add_argument('--password', type=str, help='PostgreSQL password')
    parser.add_argument('--host', type=str, help='PostgreSQL host')
    parser.add_argument('--port', type=str, help='PostgreSQL port')
    parser.add_argument('--database', type=str, help='PostgreSQL database name')
    parser.add_argument('--table', type=str, help='PostgreSQL table name')
    parser.add_argument('--url', type=str, help='URL to download parquet file')
    args = parser.parse_args()
    main(args)
