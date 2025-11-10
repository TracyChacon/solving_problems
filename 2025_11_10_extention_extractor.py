# Extension Extractor

# Given a string representing a filename, return the extension of the file.

#     The extension is the part of the filename that comes after the last period (.).
#     If the filename does not contain a period or ends with a period, return "none".
#     The extension should be returned as-is, preserving case.

# def get_extension(filename: str) -> str:
#     if '.' not in filename or filename[-1] == '.':
#         return 'none'
    
#     filename_tokens = filename.split('.')

#     return f"{filename_tokens[-1]}"

def get_extension(filename: str) -> str:
    # Guard clause, check for two invalid states
    #   a) The filename does not contain a period
    #   b) The filename ends with a period 
    if '.' not in filename or filename[-1] == '.':
        return 'none'

    # Find the last index of the last period `.` 
    # and slice the string starting one character after it
    return filename[filename.rfind(".") + 1: ]

# Tests

# Test 1 should return "txt".
print(get_extension("document.txt"))
# Test 2 should return "none".
print(get_extension("README"))
# Test 3 should return "PNG".
print(get_extension("image.PNG"))
# Test 4 should return "gitignore".
print(get_extension(".gitignore"))
# Test 5 should return "gz".
print(get_extension("archive.tar.gz"))
# Test 6 should return "none".
print(get_extension("final.draft."))