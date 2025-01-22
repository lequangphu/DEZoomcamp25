select
    doz."Zone"
from
    green_trip_data as frm
    left join zone_lookup_data as puz on frm."PULocationID" = puz."LocationID"
    left join zone_lookup_data as doz on frm."DOLocationID" = doz."LocationID"
where
    1 = 1
    and date_trunc ('month', lpep_pickup_datetime) = '2019-10-01'
    and puz."Zone" = 'East Harlem North'
order by
    tip_amount desc
limit
    1
