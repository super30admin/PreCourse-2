# Python program for implementation of Quicksort Sort
def swap(arr,i,idx):
    temp=arr[i]
    arr[i]=arr[idx]
    arr[idx]=temp

def partition(arr, low, high):
    pivot=arr[high];
    i=low-1
    for idx in range(low,high):
        if arr[idx]<pivot:
            i+=1
            swap(arr,i,idx)
    swap(arr,i+1,high)
    return i+1
# write your code here


# Function to do Quick sort
def quickSort(arr, low, high):
    if(low<high):
        p=partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
# write your code here

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),


