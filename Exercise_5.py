# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(list_, low, high):
    ind = ( low - 1 )
    list_high = list_[high]
    for j in range(low , high):
        if list_[j] <= list_high:
            ind = ind+1
            list_[ind],list_[j] = list_[j],list_[ind]
    list_[ind+1],list_[high] = list_[high],list_[ind+1]
    return (ind+1)
  #write your code here


def quickSortIterative(list_, low, high):
  #write your code here
    size = high - low + 1
    list_s = [0] * (size)
    last = -1
    last = last + 1
    list_s[last] = low
    last = last + 1
    list_s[last] = high
    while last >= 0:
        high = list_s[last]
        last = last - 1
        low = list_s[last]
        last = last - 1
        pivot = partition( list_, low, high )
        if pivot-1 > low:
            last = last + 1
            list_s[last] = low
            last = last + 1
            list_s[last] = pivot - 1
        if pivot+1 < high:
            last = last + 1
            list_s[last] = pivot + 1
            last = last + 1
            list_s[last] = high

list_ = [4, 3, 5, 2, 1, 3, 2, 3]
quickSortIterative(list_, 0, len(list_)-1)
print ("Sorted array:",list_)
