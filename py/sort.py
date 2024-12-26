def sort_min_max(input_list):
    """Sorts a list from minimum to maximum without using the sort() method.

    Args:
        input_list: The list to be sorted.

    Returns:
        A new sorted list, or the original list if it's empty or contains only one element.
        Returns a string "List contains non-numeric values" if the list has non-numeric values.
    """

    if not input_list:
        print(input_list)
        return input_list
    
    if len(input_list) == 1:
        print(input_list)
        return input_list
    
    for e in input_list:
        if not isinstance(e,(int,float)):
            print(input_list)
            return "List contains non-numeric values"

my_list = [1,2,"a"]
sorted_list = sort_min_max(my_list)
print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")