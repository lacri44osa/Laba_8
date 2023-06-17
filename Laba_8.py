from datetime import datetime

def taxi(price):
    def wrapper(distance):
        result = price(distance)
        current_time = datetime.now().time()

        print("Input distance:", distance, "km")
        print('Total price: ',(round(price, 2)))
        print("Execution time:", current_time, "seconds")

        return result
    return wrapper

@taxi
def taxi(distance):
    base_tariff = 4.00
    per_distance_tariff = 0.25
    distance_in_meters = distance * 1000
    price = base_tariff + (distance_in_meters / 140) * per_distance_tariff
    return price

distance = 0.140
price = taxi(distance)