# Speed Check

# Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

#     1 mile equals 1.60934 kilometers.
#     If you are travelling less than or equal to the speed limit, return "Not Speeding".
#     If you are travelling 5 KPH or less over the speed limit, return "Warning".
#     If you are travelling more than 5 KPH over the speed limit, return "Ticket".

from decimal import Decimal

def speed_check(speed_mph: int|float, speed_limit_kph: int|float) -> str:
    # => convert `speed_mph` var => m/hr -> k/hr
    # 
    print(f"speed_mph: {speed_mph}, speed_limit_kph: {speed_limit_kph}")
    miles_to_km_factor = Decimal('1.60934')
    speed_km = Decimal(speed_mph) * miles_to_km_factor
    print(f"speed_km: {speed_km}")

    pass
if __name__ == '__main__':
    # Tests

    # 1 should return "Not Speeding".
    print(speed_check(30, 70))
    # 2 should return "Warning".
    print(speed_check(40, 60))
    # 3 should return "Not Speeding".
    print(speed_check(40, 65))
    # 4 should return "Ticket".
    print(speed_check(60, 90))
    # 5 should return "Warning".
    print(speed_check(65, 100))
    # 6 should return "Ticket".
    print(speed_check(88, 40))