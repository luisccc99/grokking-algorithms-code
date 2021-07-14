def binary_search(arr, key):
    """binary search function takes a sorted array and a key,
    if the key is in the array, the function returns its index"""
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        guess = arr[mid]
        if guess < key:
            low = mid + 1
        elif guess > key:
            high = mid - 1
        else:
            return mid
    return None


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9]
    print(binary_search(nums, 3)) # > 1
    print(binary_search(nums, -1)) # > None