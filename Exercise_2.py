# Python program for implementation of RECURSIVE QUICKSORT. 
  
# give you explanation for the approach
def partition(arr,low,high):
    #print(high)
    p= high # Pivot
    small= low
    for i in range(low, high+1):
       if arr[i] < arr[p]:
            arr[i], arr[small]= arr[small], arr[i]
            small+=1
    # Swap small and pivot.
    arr[small], arr[p]= arr[p], arr[small]
    return small

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
   if low <high:
      pivot= partition(arr, low, high)
      quickSort(arr, low, pivot-1)
      quickSort(arr, pivot+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
#arr = [10, 80, 30, 90, 40, 50, 70] 
n = len(arr) 
quickSort(arr,0, n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])
  
 