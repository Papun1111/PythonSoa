import copy

def demo_copy():
    # Original list
    original_list = [['Shallow', 2, 3], [4, 5, 6]]
    
    # Shallow copy of the original list
    shallow_copied_list = copy.copy(original_list)
    
    # Deep copy of the original list
    deep_copied_list = copy.deepcopy(original_list)
    
    # Modify the shallow copied list
    shallow_copied_list[0][0] = 1  # Changes the first item in the first sub-list
    
    # Modify the deep copied list
    deep_copied_list[1][0] = 'Deep'  # Changes the first item in the second sub-list
    
    # Print the results
    print("Original List:", original_list)
    print("Shallow Copy:", shallow_copied_list)
    print("Deep Copy:", deep_copied_list)

demo_copy()
