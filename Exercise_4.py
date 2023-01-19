# Time Complexity : O(NlogN), N begin the length of the array
# Space Complexity : O(N), N being the length of the array. 
# Did this code successfully run on Leetcode : Did not find the same
# problem on leetcode. 
# Any problem you faced while coding this : I had to redo and retest due
# to indices issues in merge and mergesort functions.  


# Your code here along with comments explaining your approach

# Python program for implementation of MergeSort 

# Function to merged two sorted arrays. 
def merge(arr1, arr2):
    arr_merged = []
    start1 = 0
    start2 = 0
    if len(arr1)==0:
        return arr2
    elif len(arr2)==0:
        return arr1
    else:
        #loop until one array is completely in arr_merged. 
        while(start1<len(arr1) and start2<len(arr2)):
            a1 = arr1[start1]
            a2 = arr2[start2]
            if a1<=a2:
                arr_merged.append(a1)
                start1 = start1+1
            else:
                arr_merged.append(a2)
                start2 = start2+1
        #placing remaining array into arr_merged.
        if start2<len(arr2):
            while(start2<len(arr2)):
                a2 = arr2[start2]
                arr_merged.append(a2)
                start2 = start2+1
        if start1<len(arr1):
            while(start1<len(arr1)):
                a1 = arr1[start1]
                arr_merged.append(a1)
                start1 = start1+1
        return arr_merged


def mergeSort(arr):
    #write your code here
    #Recursion for divide and conquer portion of mergesort. 
    if len(arr)<=1:
        return arr
    else:
        mid_index = int((0+len(arr))/2)
        arr1 = mergeSort(arr[0:mid_index])
        arr2 = mergeSort(arr[mid_index:len(arr)])
        #merging two arrays. 
        arr_final = merge(arr1, arr2)
        #copying array from merge back into arr. 
        for i in range(len(arr_final)):
            arr[i] = arr_final[i]
        return arr_final


  
# Code to print the list 
def printList(arr): 
    
    #write your code here
    print(arr)

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
