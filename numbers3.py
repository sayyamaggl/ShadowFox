def calculate_speed(distance, time_minutes):
    time_seconds = time_minutes * 60  
    speed = distance / time_seconds
    return int(speed)  

distance = 490 
time_minutes = 7 

speed_meters_per_second = calculate_speed(distance, time_minutes)

print(speed_meters_per_second)
