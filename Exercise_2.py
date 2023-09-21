# Python program for implementation of Quicksort Sort   
# give you explanation for the approach
#time complexity: N(log(N))
#space complexity : O(N)


def partition(arr,low,high):
  swap = low                                    #taking swap position and pivot position as the leftmost
  for i in range(low+1, high+1):
    if arr[i] < arr[low]:                       #finding the smaller element and swaping it with pivot till pivot reaches partition position
      swap+=1
      (arr[i],arr[swap]) = (arr[swap],arr[i])
    (arr[low],arr[swap]) = (arr[swap], arr[low])  #swap pivot with the smaller element
    return swap
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
      pivot_index = partition(arr,low,high)   #returns index of pivot number 
      quickSort(arr,low,pivot_index+1)        #recursive sorting on left side of pivot
      quickSort(arr,pivot_index+1,high)       #recursive sorting on right side of pivot
    return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
sorted_arr=quickSort(arr,0,n-1) 
print (f"Sorted array is:{sorted_arr}") 
 
