# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    #write your code here
    pivot = arr[l]
    while ( l < h ):
        if ( arr[l] < pivot ):
            l += 1
        elif ( arr[h] > pivot ):
            h -= 1
        if ( l < h ):
            arr[l], arr[h] = arr[h], arr[l]
    return l

def quickSortIterative(arr, l, h):
    #write your code here
    stack = []
    stack.append( l )
    stack.append( h )

    while ( stack ):
        high = stack.pop()
        low = stack.pop()

        if ( high - low < 2 ):
            continue
        else:
            pivot = partition( arr, low , high )
            # If there are elements on the left side of pivot push
            # low and pivot - 1 into stack
            if ( pivot - 1 > l ):
                stack.append( low )
                stack.append( pivot - 1 )

            # If there are elements on the right side of pivot push
            # pivot + 1 to high into stack
            if ( pivot + 1 < h ):
                stack.append( pivot + 1 )
                stack.append( high )

    return arr

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
