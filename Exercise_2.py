"""
Time Complexity - O(nlogn)
Space Complexity - O(n)

"""

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<=j:
        while i<=j and arr[i]<=pivot:
            i+=1
        while i<=j and arr[j]>pivot:
            j-=1
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    temp=arr[low]
    arr[low]=arr[j]
    arr[j]=temp
    return j
  
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        j=partition(arr,low,high)
        quickSort(arr,low,j)
        quickSort(arr,j+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])
  
 
