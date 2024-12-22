# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #selecting highest element as pivot
    pivot= arr[high]
    # print('printing the pivot element',pivot)
    #initial index
    i= low-1

    for j in range(low,high):
        if(arr[j]<pivot):
            # initial index of i
            i+=1
            arr[i], arr[j]=arr[j], arr[i]

    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1
  

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if(low<high):
        pivot_index= partition(arr,low,high)
        quickSort(arr, low,pivot_index-1)
        quickSort(arr, pivot_index+1, high)

    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
