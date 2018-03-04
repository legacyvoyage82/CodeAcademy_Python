# Below your existing code, define a function called trip_cost that takes two parameters, city and days and returns the sum of calling the rental_car_cost(days), hotel_cost(days - 1), and plane_ride_cost(city) functions.

# Notice that we changed the argument of hotel_costs() from nights to days - 1. Since we want trip-cost to only depend on two parameters, we have to convert the variable nights into days. If you are going to be staying somewhere, the number of nights you stay there is one less than the number of days you were there (imagine a weekend trip to visit family, you leave Saturday and return Sunday, so you visit for two days, but only stay for one night).

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
def trip_cost(city,days):
    return rental_car_cost(days)+hotel_cost(days-1)+plane_ride_cost(city)