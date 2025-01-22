select
    count(*) filter (
        where
            trip_distance <= 1
    ) as _1st,
    count(*) filter (
        where
            trip_distance > 1
            and trip_distance <= 3
    ) as _2nd,
    count(*) filter (
        where
            trip_distance > 3
            and trip_distance <= 7
    ) as _3rd,
    count(*) filter (
        where
            trip_distance > 7
            and trip_distance <= 10
    ) as _4th,
    count(*) filter (
        where
            trip_distance > 10
    ) as _5th
from
    green_trip_data
where
    1 = 1
    and (
        lpep_pickup_datetime >= '2019-10-01'
        and lpep_dropoff_datetime < '2019-11-01'
    )
