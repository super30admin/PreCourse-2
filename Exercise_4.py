# Time Complexity: O(nlogn)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        mergeSort(arr1)
        mergeSort(arr2)

        # merging
        index1 = 0
        index2 = 0
        idx = 0
        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] < arr2[index2]:
                arr[idx] = arr1[index1]
                index1 += 1
            elif arr1[index1] > arr2[index2]:
                arr[idx] = arr2[index2]
                index2 += 1
            idx += 1
        while index1 < len(arr1):
            arr[idx] = arr1[index1]
            index1 += 1
            idx += 1
        while index2 < len(arr2):
            arr[idx] = arr2[index2]
            index2 += 1
            idx += 1

def printList(arr):
    for i in range(len(arr)):
        print(f'{arr[i]} ')
    

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
