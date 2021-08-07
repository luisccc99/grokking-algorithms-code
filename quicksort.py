import random

# TODO: finish description of how quicksort works
def quicksort(arr):
    """select random pivot, partition the array where
    elements less than the pivot stay in the left
    and in the right put elements greater than the pivot"""
    if (len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def _shuffle(arr):
    """helper method to shuffle the array
    fisher-yates algorithm shuffle the array in linear time"""
    for i, _ in enumerate(arr):
        randomIndex = random.randint(0, i)
        swap = arr[i]
        arr[i] = arr[randomIndex]
        arr[randomIndex] = swap

if __name__ == "__main__":
    randomarr = [random.randint(0, 100) for _ in range(10)]
    print("input array:")
    print(randomarr)
    _shuffle(randomarr)
    print()
    print("shuffle array:")
    print(randomarr)
    print()
    print("sorted array:")
    print(quicksort(randomarr))