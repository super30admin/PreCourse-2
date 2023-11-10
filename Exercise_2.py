# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

def partition(arr,low,high):
    '''
    time complexity: O(nlog)
    space complexity: O(n)
    '''
    #write your code here
    #assign last element as pivot
    pivot = arr[high]
    #this index will hold the highest number while itterating
    i = low-1

    for j in range(low,high):
        if(arr[j]<= pivot):
            #if greater element is found shift the pointer
            i+=1

            #swapping element at i with element at j
            #this will keep smaller elemnts on left side and greater element on right side
            (arr[i],arr[j]) = (arr[j],arr[i])

        
    #swapping the pivot, such that all elements smaller then pivot would be on left and other on right
    (arr[i+1],arr[high]) = (arr[high],arr[i+1])

    #return pivot
    return i+1 
    



# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if(low<high):
        #find the pivot element
        pi = partition(arr,low,high)

        #recusive call on left
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
