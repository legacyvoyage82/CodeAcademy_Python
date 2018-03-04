# Below your existing code, define a function called rental_car_cost with an argument called days.

# Every day you rent the car costs $40.
# if you rent the car for 7 or more days, you get $50 off your total.
# Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total.
# You cannot get both of the above discounts.
# Return that cost.



#%%

def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if city == "Charlotte":
        return (183)
    elif city == "Tampa":
        return (220)
    elif city == "Pittsburgh":
        return (222)
    elif city == "Los Angeles":
        return (475)

def rental_car_cost(days):
    cost =  days*40
    if days >=7:
        cost -=50
    elif days >=3:
        cost -=20
    return cost

print (rental_car_cost(1))
print (rental_car_cost(3))
print (rental_car_cost(4))
print (rental_car_cost(16))