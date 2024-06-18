# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach

def swap(arr, i,j) :
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr,low,high) :


    i,j = low, high
    pivot = high


    while i < j:

        # print(arr[i])
        # print(arr[pivot])

        while (arr[i] < arr[pivot]) :
            i += 1

        print(i)


        while (arr[j] > arr[pivot]):
            j -= 1

        if (i<j) :

            arr = swap(arr, i, j)


    swap(arr, i, high)

    return i




    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if (low < high) :

        i = partition(arr, low, high)

        quickSort(arr, low, i)
        quickSort(arr, i+1, high)


  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
