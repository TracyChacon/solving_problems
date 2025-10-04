def is_perfect_square(n: int) -> bool:
    return n >= 0 and int(n**(1/2))**2 == n
       


print(is_perfect_square(0))