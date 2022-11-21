# Python program for implementation of Quicksort Sort 
#Time Complexity O(n*log n)
#Space Complexity O(n)
# give you explanation for the approach
def partition(arr,l,h):
    pivote=arr[h]
    i=l-1
    for j in range(l,h):
      if arr[j]<pivote:
          i+=1
          arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i], arr[h] = arr[h], arr[i]
    return i
  

# Function to do Quick sort 
def quickSort(arr,l,h):
    if l < h:
        # select the position to divide it
        # split the array around selected element by placing it exactly in it's by displacing the elements according to the inequality
        pivote = partition(arr, l, h)
        quickSort(arr,l,pivote-1)
        quickSort(arr,pivote+1,h)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=' '),
  
 
