# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#The below quick sort divides the array recursively at a partition index 
# such that all the elements before our partition index are smaller than our pivot and after pIndex are greater.
#it consider the last elem of the array to be the pivot every time. Ideally the median of 
# the elements in array would be a good choice to avoid worst case running TC
def partition(arr,low,high):
    pivot = arr[high]
    pIndex = low
    for i in range(low,high):
        if arr[i]<=pivot:
            swap(arr,i,pIndex)
            pIndex+=1
    swap(arr,pIndex,high)
    return pIndex

def swap(arr,x,y):
   arr[x],arr[y] = arr[y],arr[x]
 
# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:#condition to check for avoiding the infinite loop 
        pivot = partition(arr,low,high)
        quickSort(arr,low,pivot-1) # here we are not considering the element for which we have already found its place 
        quickSort(arr,pivot+1,high)

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 

#TC: O(nlogn) - Best case and O(n2) worst case
#SC: O(1) - inplace calculations ##best part of this algorithm is it probably still runs faster even with its worst case TC using randomized version of QS.
  
 
