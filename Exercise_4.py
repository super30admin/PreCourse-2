# # Python program for implementation of MergeSort 
# // Time Complexity : O(nLogn)
# // Space Complexity : O(n)
# // Did this code successfully run on Leetcode :Yes
# // Any problem you faced while coding this : Had to visit youtube tutorial for understanding the concepts 


# // Your code here along with comments explaining your approach
# divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. merge() for merging two halves.
def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def printList(arr):
    # write your code here
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    # driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
