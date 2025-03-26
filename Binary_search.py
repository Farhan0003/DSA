def binary_search(lst, num):
    """
    Performs binary search on a sorted list 'lst' to find 'num'.
    Returns the position (0-based index) if found, otherwise returns -1.
    """
    try:
        lower = 0
        upper = len(lst) - 1

        while lower <= upper:
            mid = (lower + upper) // 2

            if num == lst[mid]:
                return mid  # Returning 0-based index
            elif num > lst[mid]:
                lower = mid + 1
            else:
                upper = mid - 1
        return -1  # Not found
    except Exception as e:
        print("Error during binary search:", e)
        return -1

if __name__ == "__main__":
    lst = [2, 4, 6, 8, 9]
    try:
        num = int(input("Enter the number you want to find: "))
        pos = binary_search(lst, num)
        if pos != -1:
            print(f"{num} found at position {pos}")
        else:
            print("Element not found")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
