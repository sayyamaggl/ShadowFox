def pond_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

def total_water(area, water_per_sqm):
    total_water = area * water_per_sqm
    return total_water  


radius = 84  
water_per_square_meter = 1.4  

area = pond_area(radius)

total_water_in_pond = total_water(area, water_per_square_meter)

print(total_water_in_pond)
