# Time complexity O(nlogn)
# Space complexity O(n)

# Python program for implementation of MergeSort 
def mergeSort(arr):
  length = len(arr)
  if length > 1:
    mid_pt = len(arr)//2

    left_half = arr[ :mid_pt]
    right_half = arr[mid_pt: ]
    mergeSort(left_half) # recursive call
    mergeSort(right_half) # recursive call

    p1 = 0 # left half index
    p2 = 0 # right half index
    p3 = 0 # new array index 

    while p1 < len(left_half) and p2 < len(right_half):
            if left_half[p1] < right_half[p2]:
                arr[p3] = left_half[p1]
                p1 += 1
            else:
                arr[p3] = right_half[p2]
                p2 += 1
            p3 += 1

    while p1 < len(left_half):
            arr[p3] = left_half[p1]
            p1 += 1
            p3 += 1
  
    while p2 < len(right_half):
            arr[p3] = right_half[p2]
            p2 += 1
            p3 += 1

# Code to print the list 

def printList(arr): 
    #write your code here
    for i in arr:
      print(i,end=' ')
    print()

# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end = "\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end = "\n") 
    printList(arr) 
