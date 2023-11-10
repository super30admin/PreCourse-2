# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  i = low-1
  pivot = arr[high]
  for j in range(low,high):

      if arr[j]<pivot:
          i= i +1
          arr[i], arr[j] = arr[j], arr[i]
  arr[i+1], arr[high]  = arr[high], arr[i+1]     
      #write your code here
  return i+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    # if low<=high:
    #     partition_index = partition(arr, low, high)
    #     stack = []
    #     quickSort(arr, low, partition_index-1)
    #     quickSort(arr, partition_index+1, high)
    stack = []
    stack.append(low)
    stack.append(high)
    while(len(stack)!=0):
      high = stack.pop()
      low = stack.pop()
      partition_index = partition(arr, low, high)
      if partition_index -1 > low:

        stack.append(low)
        stack.append(partition_index-1)
      if partition_index +1 < high:
        stack.append(low)
        stack.append(partition_index+1)
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print("Sorted array ", arr)

