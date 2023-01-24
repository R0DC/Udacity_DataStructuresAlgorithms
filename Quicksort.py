"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    while True:
        last = array[len(array)]
        for i in array-1:
            if last > i:
                pass
            else:
                temp = array[0]
                array[0] = i
                i = last
                last = array[0]
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))