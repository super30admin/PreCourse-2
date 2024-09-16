# Python program for implementation of Quicksort Sort
  # give you explanation for the approach
def partition(arr,low,high):

    pivot=arr[high]
    pindex=low

    for i in range(low,high,1):
        if arr[i]<pivot:
            temp=arr[pindex]
            arr[pindex]=arr[i]
            arr[i]=temp
            pindex+=1

    arr[pindex],arr[high]=arr[high],arr[pindex]

    return pindex

# Function to do Quick sort
def quickSort(arr,low,high):

    if low<high:

        index=partition(arr,low,high)
        print(index,low,high)
        quickSort(arr,low,index-1)
        quickSort(arr,index+1,high)

# Driver code to test above
arr = [10,9,8,5,3,100]
n = len(arr)
quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),
