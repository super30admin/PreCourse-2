#Time complexity is O(n*logn)
#Space complexity is O(n)

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#write your code here
def partition(arr,low,high):
    #selecting right element as pivot
    pivot=arr[high]
    #pointer for the largest element
    i=low-1
    #Comparing each element with the pivot
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            #if found a element smaller than pivot swapping it with the greatest element pointed by i
            arr[i],arr[j]=arr[j],arr[i]
            #Swapping the pivot element with the element pointed by i
    arr[i+1],arr[high]=arr[high],arr[i+1]
    #Returning the position from where the partition starts
    return i+1
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
  if low<high:
      #Finding pivot element such that we get all the elements smaller than the pivot to the left of it and elements larger than pivot to the right of it
      p=partition(arr,low,high)
      #Recursive call
      quickSort(arr.low,p-1)
      quickSort(arr,p+1,high)
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
