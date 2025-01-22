select
    zld."Zone",
    sum(total_amount) as total_amount
from
    green_trip_data as frm
    inner join zone_lookup_data as zld on frm."PULocationID" = zld."LocationID"
where
    1 = 1
    and date_trunc ('day', lpep_pickup_datetime) = '2019-10-18'
group by
    1
having
    sum(total_amount) > 13000
