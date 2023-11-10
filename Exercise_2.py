# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

# Time Complexity :Best Case and Average Case - O(n log n), Worst Case -O(n^2)
# Space Complexity :Best Case and Average Case - O(log n), Worst Case- O(n)
def partition(arr,low,high):
    pivot=arr[high]
    print("pivot",pivot)
    i=low-1

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

    temp=arr[i+1]
    arr[i+1]=arr[high]
    arr[high]=temp

    print("-->",arr)
    return i+1
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low>=high:
        return
    p=partition(arr,low,high)
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
  
 
