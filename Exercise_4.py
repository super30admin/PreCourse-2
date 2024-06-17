# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr)<= 1:
        return arr
    else:
        #[7,6,5,4,3,2,1]
        mid = len(arr)//2

        left_arr = arr[0:mid]
        right_arr = arr[mid::]

        left = mergeSort(left_arr)
        right = mergeSort(right_arr)
    arr[:] = merge(left,right)
    return arr

def merge(list1, list2): #([2,5],[1,2,3,6,7,8])
    op = []
    p1, p2 = 0,0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            op.append(list1[p1])
            p1 += 1
        else:
            op.append(list2[p2])
            p2 +=1
    
    while p1< len(list1):
        op.append(list1[p1])
        p1 += 1
    
    while p2 < len(list2):
        op.append(list2[p2])
        p2 += 1

    return op
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    print(arr)
    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
