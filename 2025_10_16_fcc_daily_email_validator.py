# Email Validator
# Given a string, determine if it is a valid email address using the following constraints:

# It must contain exactly one @ symbol.
#
#  The local part (before the @):
# Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
# Cannot start or end with a dot.
#
# The domain part (after the @):
# Must contain at least one dot.
# Must end with a dot followed by at least two letters.
# Neither the local or domain part can have two dots in a row.

import re


local_regex = r'[\w\-]+(\.[\w\-]+)*'
at_sign = '@'
domain_regex = r'[\w\!\-]+(\.[\w\-])*'
tld_regex = r'\.[a-zA-Z]{2,}'

email_pattern = re.compile(local_regex + at_sign + domain_regex + tld_regex)


def validate(email: str) -> bool:
    if email.count('@') != 1:
        return False
    
    local, domain = email.split('@')

    if '..' in email:
        return False

    if local.startswith('.') or local.endswith('.'):
        return False

    return bool(email_pattern.fullmatch(email))

if __name__ == "__main__":
    # True
    # print(validate("a@b.cd"))
    # True
    # print(validate("develop.ment_user@c0D!N.G.R.CKS"))
    # False
    # print(validate(".b@sh.rc"))
    # print(validate("git@commit@push.io"))
    print(validate("X...junk@domain.com"))
