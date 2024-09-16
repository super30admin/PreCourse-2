def mergeSort(arr):
    #write your code here
    if len(arr)>1:
        mid=len(arr)//2
        leftlist=arr[:mid]
        rightlist=arr[mid:]
        mergeSort(leftlist)
        mergeSort(rightlist)

        i=j=k=0

        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<rightlist[j]:
                arr[k]=leftlist[i]
                i+=1
            else:
                arr[k]=rightlist[j]
                j+=1
            k+=1
        while i<len(leftlist):
            arr[k]=leftlist[i]
            i+=1
            k+=1

        while j<len(rightlist):
            arr[k]=rightlist[j]
            j+=1
            k+=1
# Code to print the list 
def printList(arr): 
    
    #write your code here
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print()
    
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
