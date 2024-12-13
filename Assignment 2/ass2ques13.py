
position = input("Enter the position (e.g., 'a1', 'h8'): ")

column = position[0].lower()  
row = int(position[1])        


if (ord(column) - ord('a') + row) % 2 != 0:
    color = "Black"
else:
    color = "White"

# Output the color of the square
print(f"The square {position} is {color}.")
