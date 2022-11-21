# Python program for implementation of MergeSort
#Time Complexity O(n*log n)
#Space Complexity O(n)
def mergeSort(a):
    if len(a) == 1:
        return a
    else:
        l = 0
        h = len(a)
        m = (l + h) // 2
        x = mergeSort(a[l:m])
        y = mergeSort(a[m:h])
        i = 0
        j = 0
        xl = len(x)
        yl = len(y)
        list1 = []
        while (i < xl and j < yl):
            if x[i] <= y[j]:
                list1.append(x[i])
                i += 1
            else:
                list1.append(y[j])
                j += 1
        if i < xl:
            while (i < xl):
                list1.append(x[i])
                i += 1
        if j < yl:
            while (j < yl):
                list1.append(y[j])
                j += 1
        # print('test',list1,l,h-1)
        return list1
  
# Code to print the list 
def printList(arr): 
    
    print(arr)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    arr=mergeSort(arr)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
