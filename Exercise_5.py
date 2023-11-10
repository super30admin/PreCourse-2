#Time Complexity: O(n^2)
#Space Complexity: O(n)
#This code runs fine
#It was hard to come up with the thought of doing it in iterative way,so I had to look for the solution online

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, low, high):
    pivot = arr[high]  # assigning the value at high index as pivot
    i = (low - 1)  # keeping the smaller element aside from the list
    for j in range(low, high):
        if arr[j] < pivot:  # if pivot is greater than the element then
            # reassign the smaller element and swap the smaller element with the current one
            i = i + 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    # swapping the smaller element pointer with the pivot
    # so that it create a partition in such a way that
    # all the elements smaller than the pivot stays on left side of it
    # and the rest on the right side of it
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    # return the partition index
    return i + 1


def quickSortIterative(arr, low, high):
    # if low<high:
    #     part = partition(arr,low,high) #get the partitioning index
    #     quickSort(arr,low,part-1) #recurssively sort the left hand side of the list
    #     quickSort(arr,part+1,high) #recurssively sort the right hand side of the list

    st = [0] * (high - low + 1) #initializing the stack
    top = 0
    st[top] = low #assigning the low index at the top of the stack
    top = top+1
    st[top] = high

    while top >= 0: #while stack is empty
        high = st[top] #taking the index of high and low to sort the elements in between
        top = top-1
        low = st[top]
        top = top-1

        pivot = partition(arr,low,high)

        if low < pivot-1: #checiing if there's any elements left on left side
            top = top+1
            st[top] = low
            top = top+1
            st[top] = pivot - 1

        if high > pivot+1: #checking if any elements left on right side
            top = top+1
            st[top] = pivot+1
            top = top+1
            st[top] = high


arr = [10,0,1,3,7,0,-1,8,-2]
print("Array before sorting : " , arr)
quickSortIterative(arr,0,len(arr)-1)
print("Array after sorting : " , arr)




