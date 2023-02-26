# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    # selecting last element as pivot
    pivot = arr[high]
    i = low-1 
    for j in range(low,high): 
         # If the current element is smaller than or equal to the pivot,
        # swapping with the element at partition index and incrementing the index
        if arr[j] <= pivot: 
             i +=1 
             arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1 
           
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high: 

        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot-1)
        quickSort(arr,pivot+1,high)
   

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
