def find_position(num_list, number, first, last):
    """
    Perform recursive binary search to find the position of a number in a sorted list.

    Parameters:
    - num_list: The sorted list of numbers.
    - number: The number to find in the list.
    - first: The starting index of the search range.
    - last: The ending index of the search range.

    Returns:
    - The index of the number if found, otherwise -1.
    """
    if last >= first:
        middle = first + (last - first) // 2

        # Check if the middle element is the target number
        if num_list[middle] == number:
            return middle

        # If the target is greater, search the right half
        elif num_list[middle] < number:
            return find_position(num_list, number, middle + 1, last)

        # If the target is smaller, search the left half
        else:
            return find_position(num_list, number, first, middle - 1)

    # Return -1 if the number is not found
    return -1


# Example usage
if __name__ == "__main__":
    num_list = sorted([5, 8, 9, 1, 23, 7, 3, 0, 15])
    number = 9

    result = find_position(num_list, number, 0, len(num_list) - 1)

    if result != -1:
        print(f"Number {number} found at index {result}.")
    else:
        print(f"Number {number} not found in the list.")
