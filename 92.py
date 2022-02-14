from numpy import greater


def quicksort (array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<pivot]
        greater = [i for i in array[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
li = [1, 34, 23, 45, 456, 2]
#print(type(li))
print (quicksort(li))
