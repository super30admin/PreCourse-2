#Time Complexity : O(N*logN)
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
  
#explanation : We find an element and then partition the list into smaller or higer and then fix the postion of the element.
def partition(arr,low,high):
    '''
    this takes one element and then place it to the correct location 
    '''
    i  = (low-1) #index of small element
    pivot = arr[high]
    for j in range(low, high) :
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[high]  = arr[high], arr[i+1]
    return (i+1)

  


# Function to do Quick sort 
def quickSort(arr,low,high): 
    if len(arr) ==1:
        return arr
    if low<high :
        part = partition(arr, low,high)
        #sorting element before and after part
        quickSort(arr,low,part-1)
        quickSort(arr,part+1,high)    
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
