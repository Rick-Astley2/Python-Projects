from collections import deque
from queue import PriorityQueue, Queue
import bisect

# Linear search not good for long lists

"""
def main():
   array = [9, 7, 3, 2, 1, 4, 5, 8, 6]

   index = linear_search(array, 10)

    if index != -1:
        print(f"Element found at idex {index}: {array[index]}")

    else:
        print("Element not found")

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

if __name__ == "__main__":
    main()
"""

# binary search not usefull for short lists

"""
def main():
    array = [0] * 10000000

    for i in range(len(array)):
        array[i] = i
    
    target = 777777
    index = binary_search_(array, target)
    

    if index != -1:
        print(f"Found target at index {index}")
    else:
        print("target not found")
# made with library
def binary_search(array, target):
    index = bisect.bisect_left(array, target)
    if index != len(array) and array[index] == target:
        return index
    else: 
        return -1

# not made with the library
def binary_search_(array, target):
    low = 0
    high = len(array) - 1

    while(low <= high):
        middle = (low + high) // 2
        value = array[middle]

        print(f"middle {value}")

        if value < target:
            low = middle + 1
        elif value > target: high = middle - 1
        else: return middle
    
    return -1
if __name__ == "__main__":
    main()
"""
# interpolation_search best used for uniformlu distributed data quesses where a value might be base on calculated probe results if probe is incorrect, search areaa is narrowed, and a new probe is calculated.

        #average case: O(log(log(n)))
        #worst case: O(n) [values increase exponentially] 
"""
def main():
    array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    index = interpolation_search(array, 256)

    if index != -1:
        print(f"Element found at idex {index}")
    else:
        print("Element not found")

def interpolation_search(array, value):
    high = len(array) - 1
    low = 0

    while value >= array[low] and value <= array[high] and low <= high:

        probe = int(low + ((high - low) * (value - array[low]) / (array[high] - array[low])))

        print(f"probe: {probe}")

        if (array[probe] == value):
                    return probe
        elif array[probe] < value:
                    low = probe + 1
                
        else:
            high = probe
            
    return -1


if __name__ == "__main__":
    main()
"""
# bubble sort 
# O(n^2)
# easy to make
"""
def main():
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5,]
    
    bubble_sort(array)

    for i in array:
        print(i)

    

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
if __name__ == "__main__":
    main()
"""

# Selection sort
# O(n^2)
# bad for long data sets
# okay for short data sets
"""
def main():
    array = [8, 7, 9, 2, 3, 1, 5, 4, 6]
    
    selection_sort(array)
    
    for i in array:
        print(i)

def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j

        temp = array[i]
        array[i] = array[min]
        array[min] = temp

if __name__ == "__main__":
    main()
"""

# recursion
# calling a definition inside a definition
# easy to read and wright
"""
def main():

    print(power(2, 8))

def power(base, exponent):

    if exponent < 1:
        return 1
    return base * power(base, exponent -1)
    
if __name__ == "__main__":
    main()
"""

# Instertion sort
# O(n^2)
# small data sets decent
# large bad
"""
def main():
    array = [6, 1, 4, 2, 7, 5, 8, 9, 3]

    insertion_sort(array)

    for i in array:
        print(i)

def insertion_sort(array):
    for i in range(1, (len(array))):
        temp = array[i]
        j = i - 1

        while(j >= 0 and array[j] > temp):
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp

if __name__ == "__main__":
    main()
"""
# Merge Sort
# run time complexity O(n log n)
# space complexity O(n^2)
# better than alout of things that are good at big data sets
"""
def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    array = [8, 2, 5, 3, 4, 7, 6, 1]
    sorted_array = merge_sort(array)

    for num in sorted_array:
        print(num)

if __name__ == "__main__":
    main()
"""

# quick sort
# best case O(n log(n))
# worst case O(n^2)
# space complexity O(log(n))
"""
def main():
    array = [8, 2, 5, 3, 9, 4, 7, 6, 1]

    quick_sort(array, 0, len(array) - 1)

    for i in array:
        print(i, end=" ")

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot_index = partition(array, start, end)
    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, end)

def partition(array, start, end):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[end] = array[end], array[i]

    return i

if __name__ == "__main__":
    main()
"""
def main():
    pass


if __name__ == "__main__":
    main()



# put, appened, pop, poleft, get. 
# dynamic array is just a list

# don't really need to use linked_lists because arrays are already super powerful in python

# I didn't realize that I've learned a lot of the algorithms

# Stacks are like a stack of books you can't the bottom one or it falls over so you to take the ones on top of it off

# Queue are like a line the first come first serve.