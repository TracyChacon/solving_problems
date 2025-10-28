# Navigator
# On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

# Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

# You always start on the "Home" page, which will not be included in the commands array.
# Valid commands are:
# "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
# "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
# "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".

def navigate(commands: list[str]) -> str:
    back_history = ['Home']
    forward_history = []
    current_page = ''

    for command in commands:
        tokens = command.split(' ', 1)
        action = tokens[0].lower()

        if action =='visit' and len(tokens) > 1:
            current_page = tokens[1]
            back_history.append(current_page)
            forward_history = []
        elif action == 'back' and len(back_history) > 1:
            new_forward_page = back_history.pop()
            forward_history.append(new_forward_page)
        elif action == 'forward' and len(forward_history) > 0:
            new_back_page = forward_history.pop()
            back_history.append(new_back_page)

    current_page = back_history[-1]

    return current_page


if __name__ == "__main__":
    # Test 1 should return "About Us".
    print(navigate(["Visit About Us", "Back", "Forward"]))
    # Test 2 should return "Home".
    print(navigate(["Forward"]))
    # Test 3 should return "Home".
    print(navigate(["Back"]))
    # Test 4 should return "Gallery".
    print(navigate(["Visit About Us", "Visit Gallery"]))
    # Test 5 should return "Home".
    print(navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]))
    # Test 6 should return "Contact".
    print(navigate(["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]))
    # Test 7 should return "Visit Us".
    print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))