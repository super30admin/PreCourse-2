# Python program for implementation of Quicksort Sort 

# give you explanation for the approach

# // Time Complexity : O(nlogn) for best and avg and O(n^2) for worst case
# // Space Complexity : O(logn)



def partition(arr,low,high):
   #write your code here
    pivotIndex = low
    pivot = arr[pivotIndex]

    while low < high:
        while low < len(arr) and arr[low] <= pivot:
            low+=1

        while arr[high] > pivot:
            high-=1

        if low < high:
          tmp = arr[low]
          arr[low] = arr[high]
          arr[high] = tmp

           

    
    tmp = arr[pivotIndex]
    arr[pivotIndex] = arr[high]
    arr[high] = tmp

    return high


    

   

# Function to do Quick sort 
def quickSort(arr,low,high): 
  #write your code here
   if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

   

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 