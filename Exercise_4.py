# Python program for implementation of MergeSort 
def mergeSort(arr):
    #assign two pointers to divide the given array
    l = 0
    r = len(arr)-1
    if len(arr) > 1:
        mid=len(arr)//2 #to get the quotient
        #store the two new found arrays in new temp arrays t1 and t2
        t1 = arr[:mid] 
        t2 = arr[mid:] #will include the mid index
        
        mergeSort(t1)
        mergeSort(t2)
        
        #i is the index value for t1 and j is index value for t2 and k is index value for arr
        i=j=k=0
        
        while i < len(t1) and j < len(t2):
            if t1[i] < t2[j]:
                arr[k] = t1[i]
                i +=1
                k +=1
            else:
                arr[k] = t2[j]  
                j +=1
                k +=1
        while i < len(t1):
            arr[k] = t1[i]
            k +=1
            i +=1
        while j < len(t2):
            arr[k] = t2[j]
            k +=1
            j +=1
    
  
# Code to print the list 
def printList(arr):
    for item in range (len(arr)):
        print (arr[item])
        
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr)
