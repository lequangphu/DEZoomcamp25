select
    lpep_pickup_datetime
from
    green_trip_data
where
    1 = 1
    and trip_distance = (
        select
            max(trip_distance)
        from
            green_trip_data
    )
