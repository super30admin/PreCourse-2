# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 
        Leftarray = arr[0:mid]
        Rightarray = arr[mid:]
        
        mergeSort(Leftarray)
        mergeSort(Rightarray)
        
        i = 0
        j = 0
        k = 0
        
        while(i < len(Leftarray) and j < len(Rightarray)):
            if Leftarray[i] < Rightarray[j]:
                arr[k] = Leftarray[i]
                i += 1
            else:
                arr[k] = Rightarray[j]
                j += 1
            k += 1
        
        while i < len(Leftarray):
            arr[k] = Leftarray[i]
            i+=1
            k+=1
        while j < len(Rightarray):
            arr[k] = Rightarray[j]
            j+=1
            k+=1
  #write your code here
# Code to print the list
            

def printList(arr):
    
    for i in arr:
        print(i)
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
