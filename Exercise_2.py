# Python program for implementation of Quicksort Sort 
#Time Complexity: O(NlogN)  tree height: log2(n) & n element swaps in array
#Space Complexity: O(N)  

def partition(arr,l,h):
    pivot = arr[l + ((h - l) // 2)] # finfing pivot so all smaller is in left of pivot & ViceVersa
    while True:
        while arr[l] < pivot: 
            l = l + 1

        while arr[h] > pivot:
            h = h - 1

        if l >= h: return h

        arr[l],arr[h] = arr[h], arr[l]

        # make sure the next round skips past these swapped values
        l = l + 1
        h = h - 1
    #write your code here
  

# Function to do Quick sort 
def quickSort(arr,l,h): 
    if l < 0 or h < 0 or l >= h: return
    p = partition(arr, l, h)
    quickSort(arr, l, p)
    quickSort(arr, p+1, h)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print (arr[i])
  
 
