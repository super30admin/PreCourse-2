# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    # select the pivot as the last element
    pivot = arr[ high  ]
    i = low

    for j in range( low, high ):
        # j scans the array and i keeps track of elements less than pivot
        if ( arr[j] < pivot ):
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1

    # Now the position of i is the correct position for the pivot
    arr[i], arr[high] = arr[high], arr[i]
    return i

def partition1(arr,low,high):
    #write your code here
    pivot = arr[ ( low + high ) // 2 ]

    while ( low < high ):
        while ( arr[low] < pivot ):
            low += 1
        while ( arr[high] > pivot ):
            high -= 1
        if ( low < high ):
            arr[low], arr[high] = arr[high], arr[low]

    return low

# Function to do Quick sort
def quickSort(arr,low,high):
    #write your code here
    if ( low < high ):
        pivot = partition( arr, low, high )
        print ( arr )
        quickSort( arr, low, pivot - 1 )
        quickSort( arr, pivot + 1, high )

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
