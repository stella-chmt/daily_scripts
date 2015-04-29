__author__ = 'mengting.chen'

def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return -1

def rental_car_cost(days):
    if days >= 3 and days < 7:
        return 40 * days - 20
    elif days >= 7:
        return 40 * days - 50
    else :
        return 40 * days

def trip_cost(city, days, spending_money):
    if plane_ride_cost(city) == -1:
        print "Error, get the wrong city"
        return -1
    else :
        return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

# You were planning on taking a trip to LA
# for five days with $600 of spending money.
print trip_cost("Los Angeles", 5, 600)

print 2734.23 - trip_cost("Los Angeles", 5, 600)