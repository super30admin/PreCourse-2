# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach


# Time Complexity - Best case: O(n log n) - Even partion 
                    # Worst  - O(n^2) — Pivot ends up at the extreme 

#  Space Complexity - Best case - O(log n) -  Recursion stack for balanced partition 
                    # Worst - O(n) - Too much recursion 


def partition(arr,low,high): # To arrange elements as per pivot

    #write your code here

    pivot = arr[high]  # Last element as pivot
    i = low - 1        # Index for  smaller element


    for j in range(low,high):
        if arr[j] < pivot: # Current element is smaller than pivot, swap
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1] , arr[high] = arr[high] , arr[i+1] # Put pivot at the correct position
    return i + 1 # Return pivot index
  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here

    if low < high:
        part_index = partition(arr,low,high) # Find the partition index

        # Sort elements before and after partition 
        quickSort(arr,low,(part_index-1))
        quickSort(arr,part_index+1,high)
  
if __name__=="__main__":
    # Driver code to test above 
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSort(arr,0,n-1) 
    print ("Sorted array is:") 
    for i in range(n): 
        print ("%d" %arr[i]), 
  
 
