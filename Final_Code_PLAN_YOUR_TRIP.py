
# this code will calculate the final cost of a trip based on location, nights stayed at a hotel, the days for rental car service (including its discounts), and any spending money.


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

def nights(days):
    if days<=1:
        1
    else: 
        days-1

def spending_money():
    return spending_money

def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money

print(trip_cost('Los Angeles', 5, 600))

print("END OF CODE")