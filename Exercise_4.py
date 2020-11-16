# Python program for implementation of MergeSort 

def mergeSort(arr):
      n=len(arr)
      if n<=1:
            return arr
      else:
            middle_element=n//2 # finding middle element of list
            left_half=arr[ : middle_element]
            right_half=arr[middle_element : ] # Dividing the array elements into left and right halves
            mergeSort(left_half) # Sorting the first half and second half 
            mergeSort(right_half)
            i=0
            j=0
            k=0 #initial indexes
             # Copy data to temporary arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
              if left_half[i] < right_half[j]:
                  arr[k] = left_half[i] 
                  i=i+1
              else:
                  arr[k] = right_half[j]
                  j=j+1
              k =k+1
 
        # To check if any element still remains
            while i < len(left_half):
                arr[k] = left_half[i]
                i=i+1 
                k=k+1
 
            while j < len(right_half):
                arr[k] = right_half[j]
                j=j+1
                k=k+1
  
  #write your code here
  
# Code to print the list 
def printList(arr): 
    
    #write your code here
     for i in range(len(arr)):
            print(arr[i])
     print()

  
# driver code to test the above code 

if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
    
