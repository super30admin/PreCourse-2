# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr, low, high):
    i = low - 1  # index of smaler element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        # chceking if current element is smaller if yes then increase smaller elemnt index by 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swapping in python in place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# SECONDARY WAY OF WRITING PARTION CODE
#    pivot = arr[l]
#   i= l+1
#   j = h
#   while True:
#       while i<=j and arr[i]<=pivot:
#           i=i+1
#       while i<=j and arr[j]>pivot:
#           j = j-1
#       if i<=j:
#           arr[i],arr[j]=arr[j].arr[i]
#       else:
#           break
#   arr[l],arr[j]=arr[j],arr[l]
#   return j

# write your code here

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        pindex = partition(arr, low, high)
        quickSort(arr, low, pindex - 1)
        quickSort(arr, pindex + 1, high)

    # write your code here


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

