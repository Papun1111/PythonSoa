def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")


binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print(f"Decimal equivalent: {decimal_output}")

decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"Binary equivalent: {binary_output}")
