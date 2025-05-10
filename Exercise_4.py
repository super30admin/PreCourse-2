# // Time Complexity : O(n log n)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this :No


# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
        # TO get the index of mid value of an array
        mid = len(arr) // 2  
        # Diving array into half according to mid_index
        left = arr[:mid]     
        right = arr[mid:]

        # SOrting the halves
        mergeSort(left)      
        mergeSort(right)

        # Merging the sorted halves
        i = j = k = 0

        # Storing  data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copying rest of the elements to left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copying rest of the elements to right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Code to print the list 
def printList(arr): 
    
    #write your code here
    print (arr)
  
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
