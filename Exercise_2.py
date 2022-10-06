# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot=arr[high]

    i=low-1
    #write your code here
    for a in range(low,high):
        if arr[a]<=pivot:

            i=i+1
            arr[i],arr[a]=arr[a],arr[i]
    
    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    #write your code here
    if low<high:
        new=partition(arr,low,high)

        quickSort(arr,low,new-1)

        quickSort(arr,new+1,high)
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)
#for i in range(n): 
 #   print ("%d" %arr[i]), 
  
 