# SpOoKy~CaSe
# Given a string representing a variable name, convert it to "spooky case" using the following constraints:

# Replace all underscores (_), and hyphens (-) with a tilde (~).
# Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
# For example, given hello_world, return HeLlO~wOrLd.

def spookify(boo: str) -> str:
    boo_chars = boo.lower().replace('-', '~').replace('_', '~')
    count_alpha = 0
    output_boo = []

    for char in boo_chars:
        if char.isalpha():
            count_alpha += 1

            if count_alpha % 2 != 0:
               output_boo.append(char.upper())
            else:
                output_boo.append(char)
        else:
            output_boo.append(char)

    return ''.join(output_boo)


# Test 1 should return "HeLlO~wOrLd".
print(spookify("hello_world"))
# Test 2 should return "SpOoKy~CaSe".
print(spookify("Spooky_Case"))
# Test 3 should return "TrIcK~oR~tReAt".
print(spookify("TRICK-or-TREAT"))
# Test 4 should return "C~a~N~d~Y~~b~O~w~L".
print(spookify("c_a-n_d-y_-b-o_w_l"))
# Test 5 should return "ThE~hAuNtEd~HoUsE~iS~fUlL~oF~gHoStS".
print(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"))