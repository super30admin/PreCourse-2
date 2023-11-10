"""
Runtime Complexity:
1)O(log n)- mergesort algorithm partitions the given list into two halves and calls it recursively, compares with other elements and arranges themselves.
2) It goes through all the elements and compare each other with pointers. Therefore the overall runtime complexity is O(log n). O(log n) is dominated by the recursion depth. 
Height of the recurion depth tree is log 'n' levels where n is the number of nodes.

-Yes, the code worked on leetcode.
- Split the list into two halves with mid pointer. Call it recursively and further divide the subarrays. i and j pointers are used to traverse the first half and second half of the 
list respectively. k pointer is used to store the elements into the resultant sorted array.
"""# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k =0
        while i<len(left) and j<len(right):
            if left[i]< right[j]:
                arr[k] = left[i]
                i+=1

            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        

  #write your code here
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i])
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
