import random

TOTAL_RANDOM_NUMS = 20

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    sorted_list = []
    for _ in range(len(arr)):
        smallest_index = find_smallest(arr)
        sorted_list.append(arr.pop(smallest_index))
    return sorted_list


if __name__== "__main__":
    nums = [random.randint(0, 100) for _ in range(TOTAL_RANDOM_NUMS)]
    print(str(selection_sort(nums)))