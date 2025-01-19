def find_position(num_list, number):
    """
    Perform binary search to find the position of a number in a sorted list.

    :param num_list: List of numbers (must be sorted before calling this function)
    :param number: Number to find
    :return: Index of the number in the list if found, otherwise -1
    """
    first = 0
    last = len(num_list) - 1

    while first <= last:
        middle = first + (last - first) // 2
        if num_list[middle] == number:
            return middle
        elif num_list[middle] < number:
            first = middle + 1
        else:
            last = middle - 1

    return -1


# Example usage
if __name__ == "__main__":
    num_list = sorted([5, 8, 9, 1, 23, 7, 3, 0, 15])  # Sort the list
    number = 3  # Number to find
    result = find_position(num_list, number)

    if result != -1:
        print(f"Number {number} found at index {result}.")
    else:
        print(f"Number {number} not found in the list.")
