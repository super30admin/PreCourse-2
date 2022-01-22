# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
#time complexity O(nlog n)
#space complexity:O(1)

def partition(arr,low,high):
    l= low
    r= high - 1
    pivot=arr[high]

    while l < r:
     # All the elements less than to the
    # pivot go before or at l
        while l< high and arr[l]< pivot:
            #l moves to the right
            l += 1
        while r > low and arr[r] >= pivot:
            #r moves to the left 
            r -= 1
        
        if l < r:
            #swap the positions
            arr[l],arr[r]=arr[r],arr[l]

    #if l and r crossed each other
    if arr[l]> pivot:
        #swap
        arr[l],arr[high] = arr[high],arr[l]
#partion function returns the index of the pivot elemenet #after the first step of quick sort
    return l
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
#if sub array contains atleast 2 elements
    if low < high:
        partion_position=partition(arr,low,high)
        #recursively call to quick sort on elemets less than to pivot element
        quickSort(arr,low,partion_position- 1)
        #call to the elemts greater to pivot
        quickSort(arr,partion_position+ 1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5, 4] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
