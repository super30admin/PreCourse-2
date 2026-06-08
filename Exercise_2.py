# Time and Space Complexity
# Space Complexity: O(lon N) where N is the number of elements present
# Time Complexity: Average case is O(Nlog N) 
# partition function has time complexity of O(N) and space complexity of O(1)
# quickSort function has space complexity of O(N log N) and space complexity of O(log N)

# Python program for implementation of Quicksort Sort 
  

def partition(arr,low,high):
    #write your code here
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
  

def quickSort(arr,low,high): 
    if low<high:
        value=partition(arr,low,high)
        quickSort(arr,low,value-1)
        quickSort(arr,value+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
