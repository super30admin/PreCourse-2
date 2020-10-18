# PreCourse_2: Exercise_2: Python program for implementation of Quicksort Sort(Recursive approach)

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        splitpoint = partition(arr, low, high)
        quickSort(arr, low, splitpoint-1)
        quickSort(arr, splitpoint+1, high)


# give you explanation for the approach
def partition(arr,low,high):

    pivotvalue = arr[low]
    leftmark = low+1
    rightmark = high
    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark += 1

        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[low]
    arr[low] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr, 0, n-1) 
print ("Sorted array is:", end =" ") 
for i in range(n): 
    print ("%d" %arr[i], end=" ")
print ("\n")

  
 
