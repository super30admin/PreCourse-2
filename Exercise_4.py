# Python program for implementation of MergeSort 
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]  #left of partition
        Right = arr[mid:]  #right of partition
        
        mergeSort(Left)
        mergeSort(Right)
        
        
        i = j = k = 0       #i to traverse Left, j to traverse right, k to traverse arr
        
        while i < len(Left) and j < len(Right):
           # print(i,j,Left,Right)
            if Left[i] < Right[j]: #if left is smaller, put that in arr
                #print(Left,"left")
#                print(arr)
                arr[k] = Left[i]
                i +=1  #increase index in left since we used its element
            else: 
                #print(Right,"right")
#                print(arr)
                arr[k] = Right[j]  
                j +=1 #increase index in right since we used its element
            k +=1
            
            #now since one of the list usually would have a element remaining, as we used an AND above, we check each list and add that element to the arr
            
        while i <len(Left):
                arr[k] = Left[i]
                i+=1
                k+=1
                
        while j < len(Right):
                arr[k] = Right[j]
                j+=1
                k+=1
                
      #  print("arr ",arr)			
       
  
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
