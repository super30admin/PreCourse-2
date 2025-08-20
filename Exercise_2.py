# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

#Time Complexity
#Best and AverageCase -> O(n log n) , Worst Case -> O(n²)
#Space Complexity -> O(log n)

def partition(arr,low,high):
  
  
    #write your code here
  pivot = arr[high] #choose the last element as pivot
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i] #swap

  arr[i+1], arr[high] = arr[high], arr[i+1] #place pivot in correct position
  return i + 1
  
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
  if low < high:
    pi = partition(arr, low, high) #Partition Index
    #Recursively sort elements before and after partition
    quickSort(arr, low, pi-1)
    quickSort(arr, pi+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
