# Python program for implementation of Quicksort Sort 
#Time Complexity :  O(nlogn)
#Space Complexity : O(n)
# give you explanation for the approach
def partition(arr,low,high):
    #considering pivot as last element
    pivot = high
    i = low
    j= low
    while i < high:
        if arr[i] < arr[pivot]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i+1
            j = j+1
        else:
            i = i+1
    temp = arr[pivot]
    arr[pivot] = arr[j]
    arr[j] = temp
    print(j)
    return j
  
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low< high:
        part = partition(arr,low,high)
        quickSort(arr,low,part-1)
        quickSort(arr,part+1,high)


    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
