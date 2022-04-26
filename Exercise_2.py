# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''Choose end element as pivot. We have to find appropriate index for the pivot. Put partition index 'pi' as low initially. Now loop i from low to high-1 as last element is pivot. Whenever arr[i]<pivot swap arr[i] with element at 'pi' and increment 'pi'. All the elements before pi will be less than pivot.
continue until i reaches high-1. Now swap pivot with element at pindex. Sorted position of pivot is found. Now repeat the same process on left of pi and right of pi, until all elements are sorted.

'''
def swap(a,b):
    temp = arr[a] 
    arr[a]=arr[b]
    arr[b]=temp


def partition(arr,low,high):

    pi = low
    pivot = arr[high]

    for i in range(low,high):
        if(arr[i]<= pivot):
            swap(i,pi)
            pi += 1
    swap(pi,high)
    return pi
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if(low>=high): return

    index = partition(arr,low,high)
    quickSort(arr,low,index-1)
    quickSort(arr,index+1,high)

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print(arr[i])
  
 
