# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #we set the pivot as the last element in the array
    #our goal is to bring all elements less than pivot to left and all elements greater than pivot to the right
    #in the end the pivot will be swapped to its correct position.
    #we start of with the left pointer at one less than low
    #we have a second pointer j that will loop through the entire array
    #for every element j we will check if arr[j] is less than pivot. If it is, we will increment i and swap arr[i] and arr[j].
    #This will bring the smaller numbers of the pivot to the left and numbers greater than the pivot to the right.
    #Once we have looped through all elements, i will be present at the position of the last swap. We know our pivot is at the end.
    #this means that i+1 is the position where the pivot must actually be there because the pivot is greater than arr[i]
    #so we swap arr[i+1] with arr[high]
    #in the end, now the pivot is in its correct position
    #later, we return the position of i + 1 because that is how the array will now be divided.


    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
        



# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
        p = partition(arr, low, high)
        #p returns the position of the partion
        #we perform quick sort on left side
        quickSort(arr, low, p - 1)

        #then we perform quick sort on right side
        quickSort(arr, p+1, high)
    
  
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
