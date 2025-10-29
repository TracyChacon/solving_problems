# Email Sorter
# On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

# In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

# Sorting should be case-insensitive.
# If more than one email has the same domain, sort them by their username.
# Return an array of the sorted addresses.
# Returned addresses should retain their original case.
# For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].

def sort(emails: list[str]) -> list[str]:
    return sorted(emails, key=lambda email: tuple(reversed(email.lower().split('@', 1))))
    
# Test 1 should return ["jane@example.com", "john@example.com", "jill@mail.com"].
print(sort(["jill@mail.com", "john@example.com", "jane@example.com"])) 
# Test 2 should return ["bob@mail.com", "carol@mail.com", "alice@zoo.com"].
print(sort(["bob@mail.com", "alice@zoo.com", "carol@mail.com"])) 
# Test 3 should return ["user@x.com", "user@y.com", "user@z.com"].
print(sort(["user@z.com", "user@y.com", "user@x.com"])) 
# Test 4 should return ["amy@mail.COM", "bob@Mail.com", "sam@MAIL.com"].
print(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"])) 
# Test 5 should return ["SAM@ALPHA.com", "sammy@alpha.com", "sara@alpha.com", "Sarah@Alpha.com", "simon@beta.com", "Simone@Beta.com"].
print(sort(["simon@beta.com", "sammy@alpha.com", "Sarah@Alpha.com", "SAM@ALPHA.com", "Simone@Beta.com", "sara@alpha.com"])) 