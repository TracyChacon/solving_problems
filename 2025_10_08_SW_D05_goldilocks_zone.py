# Space Week Day 5: Goldilocks Zone
# For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

# Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

# To calculate the Goldilocks Zone:

# Find the luminosity of the star by raising its mass to the power of 3.5.
# The start of the zone is 0.95 times the square root of its luminosity.
# The end of the zone is 1.37 times the square root of its luminosity.
# Return the distances rounded to two decimal places.
# For example, given 1 as a mass, return [0.95, 1.37].


def goldilocks_zone(mass: float) -> list[float]:
    MIN_STELLER_FLUX_VALUE = 0.95
    MAX_STELLER_FLUX_VALUE = 1.37
    luminosity = mass**3.5
    sqrt_luminosity = luminosity**(1/2)

    habitable_zone_start = MIN_STELLER_FLUX_VALUE * sqrt_luminosity
    habitable_zone_end = MAX_STELLER_FLUX_VALUE * sqrt_luminosity
    
    habitable_zone_distances = [round(habitable_zone_start, 2), round(habitable_zone_end, 2)]
    
    return habitable_zone_distances
    
    
if __name__ == "__main__":
    # should return [0.95, 1.37]
    print(goldilocks_zone(1))
    # should return [0.28, 0.41]
    # print(goldilocks_zone(0.5))
