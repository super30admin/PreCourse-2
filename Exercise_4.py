# Python program for implementation of MergeSort 
def mergeSort(arr):
  
    #write your code here
    # base case for recursion
    if (len(arr) > 1):

        mid = len(arr)//2
        # divide the arr into two halves
        left = arr[0:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        p1 = 0
        p2 = 0
        p3 = 0
        # save the smaller of the two arrays
        while(p1 <= len(left) -1 and p2 <= len(right) -1):
            if left[p1] < right[p2]:
                arr[p3] = left[p1]
                p1 += 1
                p3 += 1
            else:
                arr[p3] = right[p2]
                p2 += 1
                p3 += 1

        # copy the remainder array in case the left or right arrays are not fully traversed
        # as the earlier while loop had an "and" operation to check both the lengths
        while(p1 < len(left)):
            arr[p3] = left[p1]
            p1 += 1
            p3 += 1

        while(p2 < len(right)):
            arr[p3] = right[p2]
            p2 += 1
            p3 += 1




        # Code to print the list
def printList(arr): 
    
    #write your code here
    for i in range(0, len(arr)):
        print (arr[i])
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is",)
    print(" ")
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ")
    print(" ")
    printList(arr) 

'''
Output- 
('Given array is',)
 
12
11
13
5
6
7
Sorted array is: 
 
5
6
7
11
12
13

'''