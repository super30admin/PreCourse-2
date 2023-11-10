# Python program for implementation of MergeSort
"""
Time Complexity: O(n * logn) - logn for diividing elements and n for merging(traversal)
Space Complexity: Not able to figure out, i have issues in predicting space complexity
Ran in Leetcode: Yes
Explanation: We will take the middle index and make two lists- one left list and one right list, and we will divide the
left and right lists till there's a single element in every list. Once divided, we will merge the corresponding two lists in pair
and sort them while merging. The sorting will be based on the fact if the element into consideration of left list is smaller than right list
then we will merge the lists such that the smaller element gets appended in the list and we increase the current pointer of the smaller element
if the rightlist element is smaller then we will append it in the array and increase the pointer of the current element of the right list.
if merging has taken place but there's some element left in either of the list we will just append it to the array
"""


def mergeSort(arr):
    if len(arr)>1:
        midIndex=len(arr)//2
        leftList=arr[:midIndex] ##notation to return the slice of an array till mid point(excluding it)
        rightList=arr[midIndex:] ##notation to return the slice of an array from mid point till the end point(including it)
        mergeSort(leftList)##apply merge sort recursively
        mergeSort(rightList)

        ##Now partition has been done and we have single elements
        ###We will be merging them back in the sorted order
        i=0
        j=0
        k=0
        while i < len(leftList) and j< len(rightList):
            if leftList[i]<rightList[j]:
                arr[k]=leftList[i]
                i+=1
            else:
                arr[k]=rightList[j]
                j+=1
            k+=1

        ##if one list is bigger than other list

        while i<len(leftList):
            arr[k]=leftList[i]
            i+=1
            k+=1

        while j<len(rightList):
            arr[k]=rightList[j]
            j+=1
            k+=1


  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):
        print(arr[i])

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]
    # size=len(arr)
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
