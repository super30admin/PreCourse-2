# Python program for implementation of Quicksort Sort 
#time complexity: O(n**2) for worst case
#space complexity: O(k)
#passed all cases on LeetCode:
#difficulty faced: didnt even know the QS algo and then how to implement
# comments: choosing the last elemet of the arr as pivot.
# elements less than pivot are to the left and gt pivot are on right


# give you explanation for the approach
def partition(arr,low,high):
  
    pivot = arr[high]

    #this is pointer to greater element used to swap with later
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

    #after the loop is done, swap pivot and greater element
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #we need to return the position of partition element
    return i+1
  

    
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    if low < high:

        #for every quicksort call we need to find partition element
        pe = partition(arr,low,high)

        #call for left of partition
        quickSort(arr,low,pe-1)

        #call for right to partition
        quickSort(arr,pe+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 