def print_character_indices(s):
    for index, char in enumerate(s):
        if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
            print(f"Character: '{char}' at Index: {index}")


inputs = "papun"
inputs=inputs.lower()
print_character_indices(inputs)
