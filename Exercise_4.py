#Time Complexity :O(nlogn)
#Space Complexity :O(n)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : none

# Python program for implementation of MergeSort 
def mergeSort(arr):
    # recursivly call the mergeSort function
    if len(arr)>1:
        midpoint=len(arr)//2
        Left_arr=arr[:midpoint]
        Right_arr=arr[midpoint:]
        mergeSort(Left_arr)
        mergeSort(Right_arr)

        i=0
        j=0
        k=0
        #merge the element from the left and right array based on which is smaller 
        while i<len(Left_arr) and j<len(Right_arr):
            if Left_arr[i]<Right_arr[j]:
                arr[k]=Left_arr[i]
                i=i+1
            else:
                arr[k]=Right_arr[j]
                j=j+1
            k=k+1
        # if there are still elements left in the left array merge it 
        while i<len(Left_arr):
            arr[k]=Left_arr[i]
            i=i+1
            k=k+1
        # if there are still elements left in the right array merge it 
        while j<len(Right_arr):
            arr[k]=Right_arr[j]
            j=j+1
            k=k+1
  
# Code to print the list 
def printList(arr): 
    for ele in arr:
        print(ele)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
