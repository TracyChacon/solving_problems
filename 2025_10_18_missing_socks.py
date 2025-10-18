# Missing Socks
# Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

# Every 2 wash cycles, you lose a single sock.
# Every 3 wash cycles, you find a single missing sock.
# Every 5 wash cycles, a single sock is worn out and must be thrown away.
# Every 10 wash cycles, you buy a pair of socks.
# You can never have less than zero total socks.
# Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
# Return the number of complete pairs of socks.
def sock_pairs(pairs: int, cycles: int) -> int:
    socks = pairs * 2
    for cycle in range(1, cycles + 1):
        if cycle % 2 == 0:
            socks = max(0, socks - 1)
        if cycle % 3 == 0:
            socks += 1
        if cycle % 5 == 0:
            socks = max(0, socks - 1)
        if cycle % 10 == 0:
            socks += 2
    return socks // 2

# def sock_pairs(pairs, cycles):
#     socks = pairs * 2

#     sock_loss = (cycles // 2) + (cycles // 5)
#     sock_gain = (cycles // 3) + (cycles // 10) * 2
#     total_pairs =  (socks - sock_loss + sock_gain) // 2

#     if total_pairs <= 0:
#         return 0
#     else:
#         return total_pairs


if __name__ == "__main__":
    # should return 1
    # print(sock_pairs(2, 5))
    # should return 0
    # print(sock_pairs(1, 2))
    # should return 4
    # print(sock_pairs(5, 11))
    # should return 3
    # print(sock_pairs(6, 25))
    # should return 0
    print(sock_pairs(1, 8))
