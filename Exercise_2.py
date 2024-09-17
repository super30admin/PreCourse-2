# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):  
    #write your code here
    curr,l = low,low
    while curr <= high:
        if arr[curr] < arr[high] or curr == high:
            arr[curr],arr[l] = arr[l],arr[curr]
            l += 1
        curr += 1
    return l-1  
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low >= high:
        return
    #write your code here
    p = partition(arr,low,high)
    quickSort(arr,low,p-1)
    quickSort(arr,p+1,high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
arr = [1,2,3,4,5]
arr = [3,2,1]
arr = [10,8,9,7,12,13,14,15,1,2,3,4,5]
#arr = [1,2]
n = len(arr) 
print(arr)
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
