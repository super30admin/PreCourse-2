# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot :
            i += 1
            arr[i] , arr[j] = arr[j] , arr[i]
    i += 1
    arr[i] , arr[high] = arr[high],arr[i]
    print(arr)
    return i 




  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 

    if (low < high):
    
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  
 
