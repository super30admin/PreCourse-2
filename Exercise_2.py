# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''
partition function logic ->
Initialise pivot element = end of the array element
if arr[ele]<pivot, push them to the left of the pindex
At the end of the loop swap ele at pindex with arr end element
return pindex
  
'''

def partition(arr,low,high):
    #write your code here
    pivot = arr[high]
    pindex = low

    for i in range(low,high):
        if arr[i]<=pivot:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex=pindex+1
    
    arr[pindex],arr[high]=arr[high],arr[pindex]
    return pindex
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low>=high:                #base condition
        return
    p = partition(arr,low,high)  #p -> index of the pivot
    quickSort(arr,low,p-1)       #sort arr segment between start to p-1 
    quickSort(arr,p+1,high)      #sort arr segment between p+1 to high


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
