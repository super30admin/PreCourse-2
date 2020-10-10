# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr,low,high):
    #partiton the arr and return the pivot such that all elements to the
    #left of pivot are less than pivot and all elements to right are greater then pivot

    i=low-1 #pointer to keep track of smallest element from left
    pivot=high-1 # start with last element as pivot
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

# Function to do Quick sort
def quickSort(arr,low,high):
    #first find pivot.
    if low<high:
        pivot= partition(arr,low,high)

        #recursively call quickSort to partition left and right side of pivot
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),

#Time complexity:
#O(nlogn)- Best case
#Worst case: O(n^2)
