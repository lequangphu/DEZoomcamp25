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
    table1 = params.table1
    table2 = params.table2

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    # load green trip data from the first URL
    url_green_trip = params.url1
    df_green_trip = pd.read_csv(url_green_trip, compression='gzip')
    green_trip_data_csv = 'green_tripdata.csv'
    df_green_trip.to_csv(green_trip_data_csv, index=False)

    # read data input path and write to the database
    df_iter = pd.read_csv(green_trip_data_csv, chunksize=100000, iterator=True)

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
            df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])
            df.to_sql(table1, con=engine, if_exists='append', index=False)
            t_end = time()
            print(f'Processed 100k rows in {t_end - t_start:.2f} seconds.')
        except StopIteration:
            break

    # load zone lookup data from the second URL
    url_zone_lookup = params.url2
    df_zone_lookup = pd.read_csv(url_zone_lookup)
    df_zone_lookup.to_sql(table2, con=engine, if_exists='replace', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # add arguments of postgresql engine connection and csv file path
    parser.add_argument('--user', type=str, help='PostgreSQL username')
    parser.add_argument('--password', type=str, help='PostgreSQL password')
    parser.add_argument('--host', type=str, help='PostgreSQL host')
    parser.add_argument('--port', type=str, help='PostgreSQL port')
    parser.add_argument('--database', type=str, help='PostgreSQL database name')
    parser.add_argument('--table1', type=str, help='PostgreSQL table name of green trip data')
    parser.add_argument('--table2', type=str, help='PostgreSQL table name of zone lookup data')
    parser.add_argument('--url1', type=str, help='URL to download green trip data')
    parser.add_argument('--url2', type=str, help='URL to download zone lookup data')
    args = parser.parse_args()
    main(args)
