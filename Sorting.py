def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    """
    try:
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    except Exception as e:
        print("Error during Bubble Sort:", e)
        return arr

def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    """
    try:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    except Exception as e:
        print("Error during Insertion Sort:", e)
        return arr

def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.
    """
    try:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    except Exception as e:
        print("Error during Quick Sort:", e)
        return arr

def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    """
    try:
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort(L)
            merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    except Exception as e:
        print("Error during Merge Sort:", e)

def main():
    """
    Allows the user to choose a sorting algorithm and sorts the provided list.
    """
    try:
        arr = list(map(int, input("Enter numbers separated by space: ").split()))
        print("Choose sorting algorithm:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Quick Sort")
        print("4. Merge Sort")
        choice = int(input("Enter choice (1-4): "))

        if choice == 1:
            print("Sorted array:", bubble_sort(arr))
        elif choice == 2:
            print("Sorted array:", insertion_sort(arr))
        elif choice == 3:
            print("Sorted array:", quick_sort(arr))
        elif choice == 4:
            merge_sort(arr)
            print("Sorted array:", arr)
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
