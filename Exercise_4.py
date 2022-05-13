# Python program for implementation of MergeSort
# // Time Complexity : O(log(N))
# // Space Complexity :  O(N)
# // Did this code successfully run on Leetcode :
# // Any problem you faced while coding this : Not able to figure out how to do in place merge Sort so for now did using extra space
# // Your code here along with comments explaining your approach
def mergeSort(arr):
  #write your code here
    return divide(arr)

def divide(arr):
    mid = (len(arr)) // 2
    if len(arr) == 1:
        return arr
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    return merge(left, right)

def merge(arrL , arrR):
    sortedArr = []
    l = 0
    r = 0
    while l < len(arrL) and r < len(arrR):
        if arrL[l] < arrR[r]:
            sortedArr.append(arrL[l])
            l += 1
        else:
            sortedArr.append(arrR[r])
            r += 1

    while l < len(arrL):
        sortedArr.append(arrL[l])
        l += 1
    while r < len(arrR):
        sortedArr.append(arrR[r])
        r += 1
    return sortedArr
# Code to print the list 
def printList(arr):
    #write your code here
    for i in arr:
        print(i)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr = mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
