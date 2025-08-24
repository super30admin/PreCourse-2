# Python program for implementation of Quicksort Sort 
# what's a quick sort : quick sort is an divide and conquer method, so we first set a pivot it can be anything i will chose last element, and then we do partitions
# we split the array into 2 partitions, left partition elements which are less or equal to the pivot and the right where elements are greater than the pivot
# recursively do the same for the left and right arrays ( why?? why is it not enough if we do once, lets go through the following eample)
# in the given example the last element is 5 so we sort it as follows 
# 10 > 5 so it will be right side same as 7,8 ,9 also so now the final array will be [1,5,10,7,8,9], is the right array sorted ?? no , that's why recursively do quick sort for left and right arrays
# then when do we stop ?  the stop condition is low< high untill then we will do once low=high the array has be sorted 

# // Time Complexity : O(nlogn) best complexity, O(n2) worst complexity
# // Space Complexity : O(logn)  though the sorting happens in place, we use recrussion and recurrison is last in first out, underneath uses stack, 
#  the depth = number of divisions, in best case depth = logn O(logn), worst case depth = n O(n)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Need to revise quicksort concept
  
# give you explanation for the approach
def partition(arr,low,high):
  
  
    #write your code here
    pivot = arr[high]
    i = low -1 
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j] , arr[i] # we are swaping so basically the value less then the pivot will in moved to the left side of the array 
            # so at thsi point lets say low is at index 2, then i wil be index 1, and j in ist iteration will be 2, and arr[2] < pivot, so we swap arr[2], arr[1]
            # and we move i from 1 to 2 i+=1 is for that, so in next iteration i = 2, j = 3 and if arr[j]< pivot again swap swap until the arr[j] < pivot so 
            # elemets less than the pivot are in left side of the array.
            # we no need to write code to handle elements greater then pivot 
            # why ? because when we iterativly do , we put the elemenst which are less than pivot in the front, thus pusing the elemenst greater than pivot to the end of the array
            # next we have to put our pivot value right after the smaller than pivot elements so in the whole loop until i we have found the elemnst less the pivot

        # once the for loop is done, i is the index of the element found in the array which is less than pivot so the 
        # pivot postion is next to the ith index so swap it
    arr[i+1], arr[high] = arr[high], arr[i+1] # pivot it kept in its correct position

    return i+1 # partition index, so left of this index have values less than pivot and right greater then pivot
    

  

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    if low < high:
        pi = partition(arr,low,high) # gives us the parttion index (if pivot is always smallest or largest then the worst complexity is o(n2))
        # so if the pivot is the largest then in fist go only all the elements left are small than pivot but those elemenst migth not be sorted so have to keep sortign again and again same with the pivot being smallest too 
        # in general case, pivot splits the array into 2 almsot equal parts , each partition takes O(n) to scan through the array, rearrange them takes O(n) 
        # each recrussion takes O(logn), totol complexity O(nlogn)
        quickSort(arr,low,pi-1) # sort the left array of the partition
        quickSort(arr,pi+1,high) # sort the right array of the partion 
 

        
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
