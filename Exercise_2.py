# Python program for implementation of Quicksort Sort 
#Time Complexity: O(n^2) worst case
#Space Complexity: O(1)


#Approach Used: Selected pivot element, and partitioned other elements into two 
#sub arrays i.e. one which is less than pivot and other which is greater than pivot.

def swap(arr,a,b):
    arr[a],arr[b] = arr[b], arr[a]

def partition(arr,low,high):
    index = low
    pivot = arr[index]
    while(low<high):
        while(low<len(arr) and arr[low]<=pivot):
            low+=1
        while(arr[high]>pivot):
            high-=1
        if low<high:
            swap(arr, low, high)
    
    swap(arr,index,high)
    
    return high
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low<high:
        index = partition(arr, low, high)
        quickSort(arr, low, index-1)
        quickSort(arr, index+1, high)
     
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
