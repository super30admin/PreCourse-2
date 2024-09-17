# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left_array = arr[:mid]
    right_array = arr[mid:]
    return merge_helper(mergeSort(left_array), mergeSort(right_array))


def merge_helper(left, right):
    l = 0
    r = 0
    resultant = []
    # print("left array", left)
    # print("right array", right)
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            resultant.append(left[l])
            l+=1
        else:
            resultant.append(right[r])
            r+=1
    if l<len(left):
        resultant+=left[l:]
    else:
        resultant+=right[r:]
    # print("*******", resultant)
    return resultant
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    arr=mergeSort(arr)
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is")
    print(arr)
    printList(arr) 
