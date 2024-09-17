# Python program for implementation of Quicksort Sort

# give you explanation for the approach
def partition(arr,low,high):
    i = low
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
    arr[i],arr[high]=arr[high],arr[i]
    return i



    #write your code here


# Function to do Quick sort
def quickSort(arr,low,high):
    if low>=high:
        return arr
    p = partition(arr,low,high)
    quickSort(arr,low,p-1)
    quickSort(arr,p+1,high)

    #write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
