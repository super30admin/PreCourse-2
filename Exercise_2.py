# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    
    #write your code here
    i=0
    j=high-1
    pivot = arr[high]

    #find proper place for i and j and swap them at required places
    while i < j: 
        #to find largest number from left
        while i < high and arr[i]<pivot:
            i+=1
        #to find smallest numer from right
        while j > low and arr[j]>=pivot:
            j-=1

        #swap largest i and smallest j 
        if i<j:
            arr[i],arr[j]==arr[j],arr[i]

        return i
    
    #if it is out of while means ---> either i==j or j<i, then swap i and pivot
    if arr[i]>pivot:
        arr[i],arr[high]=arr[high],arr[i]
   

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        #find pivot and it's proper place
        pivot_pos = partition(arr,low,high)
        #sort left of pivot
        quickSort(arr,low, pivot_pos - 1)
        #sort left of pivot
        quickSort(arr,pivot_pos + 1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print("Sorted array is: ", arr) 

  
 
