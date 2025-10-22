# Thermostat Adjuster 2
# Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

# Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
# Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
# Return "Hold" if the current temperature is equal to the target.
# To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).

def convert_temp_c_to_f(temp_c: float) -> float:
    return (temp_c * 1.8) + 32

def adjust_thermostat(current_f: float, target_c: float) -> str:
    target_f = convert_temp_c_to_f(target_c)
    
    diff = target_f - current_f

    if current_f < target_f:
        return f"Heat: {diff:.1f} degrees Fahrenheit"
    elif current_f > target_f:
        return f"Cool: {abs(diff):.1f} degrees Fahrenheit"
    else:
        return f"Hold"
     
if __name__ == "__main__":
    # should return "Hold".
    print(adjust_thermostat(32, 0)) 
    # should return "Heat: 7.0 degrees Fahrenheit".
    print(adjust_thermostat(70, 25)) 
    # should return "Cool: 7.6 degrees Fahrenheit".
    print(adjust_thermostat(72, 18)) 
    # should return "Hold".
    print(adjust_thermostat(212, 100)) 
    # should return "Heat: 12.6 degrees Fahrenheit".
    print(adjust_thermostat(59, 22)) 