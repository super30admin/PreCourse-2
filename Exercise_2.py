# Python program for implementation of Quicksort [RECURSIVE]
# Time Complexity: O(n^2)
# Space complexity : O(n)


# give you explanation for the approach
def partition(arr,low,high):    #arr, 0, last index
    pivot = arr[low]
    i= low
    j= high-1                   #j pointing to second last index

    while i<j:
        while i< high and arr[i]< pivot:                #maintaining numbers smaller than pivot at left side
            i+=1

        while j> low and arr[j] >= pivot:               #maintaining numbers greater than pivot at right side
            j-=1

        if i< j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i]> pivot:                                   #swap positions bringing pivot at it's sorted position
        arr[i], arr[high] = arr[high], arr[i]
    return i

# Function to do Quick sort 
def quickSort(arr,low,high): 

    if low< high:
        j= partition(arr, low, high)
        quickSort(arr, low, j-1)        #recursive function for left side of array
        quickSort(arr, j+1, high)       #recursive function for right side of array

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)-1
quickSort(arr, 0, n)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i])
  
 
