def can_form_palindrome(s: str) -> bool:
    # Normalize the string: remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Count the frequency of each character
    odd_count = 0
    for char in set(s):
        if s.count(char) % 2 != 0:
            odd_count += 1

    # A string can form a palindrome if there's at most one odd count
    return odd_count <= 1

# Example usage
print(can_form_palindrome("civic"))  # True
print(can_form_palindrome("ivicc"))  # True
print(can_form_palindrome("hello"))  # False
print(can_form_palindrome("A man a plan a canal Panama"))  # True
