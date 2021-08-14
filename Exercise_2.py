# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):

    #write your code here

    pass
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if(len(arr)<2):
    
        return arr

    else:

        queue_left = []
        queue_right = []
        pivot = arr[0]

        for i in range(1,len(arr)):
            if(arr[i] < pivot):
                queue_left.append(arr[i])
            else:
                queue_right.append(arr[i])

        queue_left = quickSort(queue_left, 0 , len(queue_left))
        queue_right = quickSort(queue_right, 0 , len(queue_right))

        arr = queue_left+[pivot]+queue_right    
        return arr


        
  
# Driver code to test above 
arr = [6, 7, 8, 9, 10, 5] 
n = len(arr) 
arr = quickSort(arr,0,n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
