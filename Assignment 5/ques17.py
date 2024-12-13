
set1 = {'red', 'green', 'blue'}
set2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

is_subset = set1 <= set2  # Subset
is_superset = set1 >= set2  # Superset
is_proper_subset = set1 < set2  # Proper Subset
is_proper_superset = set1 > set2  # Proper Superset
are_equal = set1 == set2  # Equality

# b) Combine sets using mathematical set operators
union = set1 | set2
intersection = set1 & set2
difference_set1_set2 = set1 - set2
difference_set2_set1 = set2 - set1
symmetric_difference = set1 ^ set2

comparison_results = {
    "is_subset": is_subset,
    "is_superset": is_superset,
    "is_proper_subset": is_proper_subset,
    "is_proper_superset": is_proper_superset,
    "are_equal": are_equal
}

set_operations_results = {
    "union": union,
    "intersection": intersection,
    "difference_set1_set2": difference_set1_set2,
    "difference_set2_set1": difference_set2_set1,
    "symmetric_difference": symmetric_difference
}

print(comparison_results,"\n",set_operations_results)
