# Time Complexity: O(nlog(n))
# Space Complexity: O(nlog(n))
def partition(arr,low,high):
  pivot=arr[high]
  i=low-1
  j=low
  while(j<high):
    if arr[j]<=pivot:
        i=i+1
        (arr[i], arr[j]) = (arr[j], arr[i])
    j=j+1
  (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
  return i+1
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
   if low<high:
    pivot=partition(arr,low,high)
    quickSort(arr,low,pivot-1)
    quickSort(arr,pivot+1,high)
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
