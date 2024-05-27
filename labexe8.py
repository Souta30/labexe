def find_first_repeating_character(s):
    # Dictionary to store the count of each character
    char_count = {}
    
    # Iterate through the string
    for char in s:
        if char in char_count:
            # If character is already in the dictionary, it's repeating
            print(f"The first repeating character '{char}' has a memory address of: {id(char)}")
            return char
        else:
            # Otherwise, add the character to the dictionary with count 1
            char_count[char] = 1
    
    # If no repeating character is found, return None
    return None

# Test cases
print(find_first_repeating_character("hello"))   # Output: 'l' (with memory address)
print(find_first_repeating_character("python"))  # Output: None
print(find_first_repeating_character("abcabc"))  # Output: 'a' (with memory address)
print(find_first_repeating_character(""))        # Output: None
