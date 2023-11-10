# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    # here I use first elem as my pivot
    # and sort until I find the correct position of pivot
    # then I take the 2 sets of arrays, elements before pivot and other set elements after pivot and sort them again
    # use a recursive call to sort on these 2 small arrays again.

    pivot = arr[low]

    left = low+1
    right = high

    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left+=1
        while arr[right] >= pivot and right >= left:
            right -=1

        if right<left:
            done = True
        else:
            temp = arr[left]
            arr[left]= arr[right]
            arr[right] = temp

    temp = arr[low]
    arr[low] = arr[right]
    arr[right] = temp
    return right


  
  
    #write your code here

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        split = partition(arr,low,high)
        quickSort(arr,low,split-1)
        quickSort(arr,split+1,high)
    
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 #time complexity - O(nLog(n))
