# Tire Pressure

# Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

#     1 bar equal 14.5038 psi.

# Return an array with the following values for each tire:

#     "Low" if the tire pressure is below the minimum allowed.
#     "Good" if it's between the minimum and maximum allowed.
#     "High" if it's above the maximum allowed.





###########################################################################################
# Initial Code
###########################################################################################

# def tire_status(pressures_psi: list[float | int], range_bar: float | int) -> list[str]:

#     BAR_TO_PSI_FACTOR = 14.5038
#     tire_status = []
#     status = ''
#     lower_bound_bar_pressure, upper_bound_bar_pressure = range_bar
#     lower_bound_psi = lower_bound_bar_pressure * BAR_TO_PSI_FACTOR
#     upper_bound_psi = upper_bound_bar_pressure * BAR_TO_PSI_FACTOR

#     for tire_pressure in pressures_psi:
#         if tire_pressure < lower_bound_psi:
#             status = 'Low'
#         elif tire_pressure <= upper_bound_psi:
#             status = 'Good'
#         else:
#             status = 'High'
            
#         tire_status.append(status)

#     return tire_status





###########################################################################################
# Refactored Code
###########################################################################################
def tire_status(pressures_psi: list[float], range_bar: list[float]) -> list[str]:
    BAR_TO_PSI_FACTOR = 14.5038
    lower_bound_psi = range_bar[0] * BAR_TO_PSI_FACTOR
    upper_bound_psi = range_bar[1] * BAR_TO_PSI_FACTOR

    def pressure_check_psi(psi: float) -> str:
        if psi < lower_bound_psi:
            return 'Low'
        elif psi <= upper_bound_psi:
            return 'Good'
        else:
            return 'High'
    
    return [pressure_check_psi(psi) for psi in pressures_psi]

if __name__ == '__main__':
    # Tests

    # Test 1 should return ["Good", "Low", "Good", "Low"].
    print(tire_status([32, 28, 35, 29], [2, 3]))
    # Test 2 should return ["Good", "Low", "High", "Good"].
    print(tire_status([32, 28, 35, 30], [2, 2.3]))
    # Test 3 should return ["Low", "Low", "Good", "Low"].
    print(tire_status([29, 26, 31, 28], [2.1, 2.5]))
    # Test 4 should return ["High", "High", "High", "Good"].
    print(tire_status([31, 31, 30, 29], [1.5, 2]))
    # Test 5 should return ["Good", "Good", "Good", "Good"].
    print(tire_status([30, 28, 30, 29], [1.9, 2.1]))