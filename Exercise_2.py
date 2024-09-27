# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    pivotIndex=low #consider pivot element is at index low
    i=low
    j=high
    while i<j:
        while i<len(arr) and arr[i]<=arr[pivotIndex]: #increment i till we find element greater than pivot element
            i+=1
        while arr[j]>arr[pivotIndex]: #decrement j till we find element smaller than pivot element
            j-=1
    
        if i<j:
            arr[i],arr[j]=arr[j],arr[i] #swap the ith(greater than pivot) and jth(smaller than pivot) elements
    arr[j],arr[pivotIndex]=arr[pivotIndex],arr[j] #swap the pivot element with th j'th element as it will be a
                                                  # partition between smaller and larger numbers
    return j #partition index

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low<high:
        p=partition(arr,low,high)
        quickSort(arr,low,p-1)
        quickSort(arr,p+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
#Time Complexity: for sorting, O(n log n) where n is number of elements in the list.
#Space complexity: avg case O(log n)