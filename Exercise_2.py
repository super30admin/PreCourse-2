#Time Complexity :O(n²)
#Space Complexity :O(log n)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : syntax issues 

  
# give you explanation for the approach
#partition based on pivot selected
def partition(arr,low,high):
    pivot=arr[high]               # the last element is choosen as the pivot 
    i=low-1
    for j in range (low,high):
        if pivot>arr[j]:          # check if the element is less than the pivot then it needs to be in the left 
            i=i+1                 
            arr[i],arr[j]=arr[j],arr[i] #swap the elements such that smaller element comes at the beginning
    arr[i+1],arr[high]=arr[high],arr[i+1] # placement of the pivot element correctly
    return i + 1                          # return the index

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:                    # sanity check to see if there ares still elements to consider 
        index=partition(arr,low,high) # get the index of the partition
        quickSort(arr,low,index-1)    #sort the left of the index
        quickSort(arr,index+1,high)   # sort the right of the index 
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
