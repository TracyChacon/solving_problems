

def get_laptop_cost(laptops:list, budget:int) -> int:
    ONLY_ONE_LAPTOP = True if (len(laptops) == 0) else False
    NO_LAPTOPS = True if (len(laptops) == 0) else False
    
    most_expensive = laptops[0]
    second_most_expensive = laptops[1]

    if NO_LAPTOPS:
        return 0
    
    if ONLY_ONE_LAPTOP:
        return 0 if (most_expensive > budget) else most_expensive

    laptops.sort(reverse=True)

    for i in range(1, len(laptops)):
        if laptops[i] <= budget:
            return laptops[i]
    
    return 0

print(get_laptop_cost([1500, 2000, 1800, 1400], 1900))