# Python program for implementation of MergeSort 
def mergeSort(arr):
     if len(arr)>1:
         
         h=len(arr)
         mid=len(arr)//2
         L=arr[:mid]
         R=arr[mid:]
         mergeSort(L)
         mergeSort(R)
         merge(arr,L,R)
  
         
def merge(arr,L,R):
    i=0
    j=0
    k=0
    L1=L
    R1=R
    while(i<len(L1) and j<len(R1)):
        
        if L1[i]<R1[j]:
                arr[k]=L1[i]
                i+=1
        else:
                arr[k]=R1[j]
                j+=1
        k+=1
    
    while(i<len(L1)):
         arr[k]=L1[i]
         i+=1
         k+=1
    while(j<len(R1)):
         arr[k]=R1[j]
         j+=1
         k+=1

# Code to print the list 
def printList(arr): 
    for val in arr:
        print(val)
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
"""
TimeComplexity: O(n log n)-worstcase
Space Compexity: O(n)
"""
