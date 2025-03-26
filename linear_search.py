def search(lst, n):
    """
    Searches for an element 'n' in the given list 'lst'.
    Returns the position (1-based index) if found, otherwise returns -1.
    """
    try:
        for i in range(len(lst)):
            if lst[i] == n:
                return i + 1  # Returning 1-based index
        return -1  # Not found
    except Exception as e:
        print("Error during search:", e)
        return -1

if __name__ == "__main__":
    lst = [5, 7, 8, 2, 5, 9, 0]
    try:
        n = int(input("Which element do you want to find? "))
        pos = search(lst, n)
        if pos != -1:
            print(f"Element found at position {pos}")
        else:
            print("Element not found")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
