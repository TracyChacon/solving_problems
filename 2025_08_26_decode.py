def decode(s):
    open_p = []
    close_p = []

    for i in range(len(s)):
        if s[i] == '(':
            open_p.insert(0, i)
            
        elif s[i] == ')':
            close_p.append(i)
    

    print ("open_p", open_p, "close_p", close_p)
    for j in range(len(open_p)):
        
        prefix = s[:open_p[j] + 1 ]

        sub_str = s[open_p[j] + 1:close_p[j]]

        reverse_str = sub_str[::-1]

        suffix = s[close_p[j]:]

        s = prefix + reverse_str + suffix

    return s.replace("(", "").replace(")", "")

def decode_001(s):
    open_p = []
    close_p = []

    for i in range(len(s)):
        if s[i] == '(':
            open_p.insert(0, i)
            
        elif s[i] == ')':
            close_p.append(i)
    

    print ("open_p", open_p, "close_p", close_p)
    for j in range(len(open_p)):
        
        prefix = s[:open_p[j] + 1 ]

        sub_str = s[open_p[j] + 1:close_p[j]]

        reverse_str = sub_str[::-1]

        suffix = s[close_p[j]:]

        s = prefix + reverse_str + suffix

    return s.replace("(", "").replace(")", "")
# type hint and return type hint
def reverse_parentheses(s: str) -> str:
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # Reverse the content of the innermost parentheses
            current_substring = ""
            while stack and stack[-1] != '(':
                current_substring += stack.pop()
            
            # Pop the opening parenthesis
            if stack:
                stack.pop()
            
            # Add the reversed substring back to the stack
            for reversed_char in current_substring:
                stack.append(reversed_char)
        else:
            stack.append(char)
    
    return "".join(stack)

# Example Usage:
print(reverse_parentheses("(f(b(dc)e)a)"))
print(reverse_parentheses("((is?)(a(t d)h)e(n y( uo)r)aC)"))
print(reverse_parentheses("(ab(cd)ef)"))
print(reverse_parentheses("(hello(world))"))
print(reverse_parentheses("a(bc)de"))
print(reverse_parentheses("a(bcdef)gh"))
print(reverse_parentheses("(u(love)i)"))


print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
 

