def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)/2 
        first_half = arr[:mid] 
        second_half = arr[mid:]
  
        mergeSort(first_half)  
        mergeSort(second_half) 
  
        i = j = k = 0
          
        while i < len(first_half) and j < len(second_half): 
            if first_half[i] < second_half[j]: 
                arr[k] = first_half[i] 
                i+=1
            else: 
                arr[k] = second_half[j] 
                j+=1
            k+=1

        while i < len(first_half): 
            arr[k] = first_half[i] 
            i+=1
            k+=1
          
        while j < len(second_half): 
            arr[k] = second_half[j] 
            j+=1
            k+=1

def printList(arr): 
    for i in range(len(arr)):
        print(arr[i]) 
    print("") 
  
arr = [23, 41, 2, 4, 96, 67, 334, 57, 90, 800]  
print ("Array is:")
printList(arr)
mergeSort(arr)
print("Array after mergeSort is: ")
printList(arr)