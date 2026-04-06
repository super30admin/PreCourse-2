# Python program for implementation of MergeSort 


# [12, 11, 13, 5, 6, 7]  6
# left = [12, 11, 13]
# right= [5, 6, 7]
def mergeSort(arr):
  
    if len(nums) <= 1:
        return nums 

    mid = len(nums) // 2

    # left = [12, 11, 13]
    left = mergeSort(nums[:mid])
    # right= [5, 6, 7]
    right= mergeSort(nums[mid:])

    return merge(left, right)

# res = [11,12,13]
# left = [12]
#           l
# right =[11,13]
#             r
def merge(left,right):
    res = []
    l=r=0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l+=1
        else:
            res.append(right[r])
            r+=1

    res.extend(left[l:])
    res.extend(right[r:])
# Code to print the list 
def printList(arr): 
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
