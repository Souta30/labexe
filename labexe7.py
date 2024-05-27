def reverse_string(s):
    # Base case: If the string is empty or contains only one character
    if len(s) <= 1:
        return s
    
    # Recursive case: Call reverse_string with the remaining characters
    # and append the first character to the end of the reversed string
    return reverse_string(s[1:]) + s[0]

# Test cases
print(reverse_string("hello"))   # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string(""))        # Output: ""
print(reverse_string("a"))       # Output: "a"
