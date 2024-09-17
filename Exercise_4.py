# Python program for implementation of MergeSort
def merge( arr1, arr2 ):

    merged_array = []
    i = 0
    j = 0
    while ( i < len( arr1) and j < len(arr2) ):
        if ( arr1[i] < arr2[j] ):
            merged_array.append( arr1[i] )
            i += 1
        elif ( arr2[j] < arr1[i] ):
            merged_array.append( arr2[j] )
            j += 1

    while ( i < len( arr1 ) ):
        merged_array.append( arr1[i] )
        i += 1

    while ( j < len( arr2 ) ):
        merged_array.append( arr2[j] )
        j += 1

    return merged_array

def mergeSort(arr):

    n = len( arr )
    #write your code here
    if len( arr ) <= 1:
        return arr
    else:
        return merge( mergeSort( arr[: n // 2] ), mergeSort( arr[n // 2:] ) )


# Code to print the list
def printList(arr):
    #write your code here
    print ( arr )

# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
