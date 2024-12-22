# Python program for implementation of MergeSort 
# f= 0
def merge(arr, left, right, mid):
    # f=f+1
    # print("inside merge count")
    left_arr_len= mid - left +1
    right_arr_len = right -mid

    left_arr = [0] * left_arr_len
    right_arr= [0] * right_arr_len
    for i in range(left_arr_len):
        left_arr[i]= arr[left+i]
    for j in range(right_arr_len):
        right_arr[j]= arr[ mid + j+1]
      
    
    i=0
    j=0
    k= left
    while i < left_arr_len and j < right_arr_len:
        if (left_arr[i]< right_arr[j]):
            # print('element to be inserted from left array',left_arr[i] )
            arr[k]= left_arr[i]
            i=i+1
        else:
            # print('element to be inserted from right array',right_arr[j] )
            arr[k]= right_arr[j]
            j=j+1
        k=k+1
    
    while (i< left_arr_len):
        arr[k]= left_arr[i]
        k=k+1
        i=i+1

    while (j< right_arr_len):
        arr[k]= right_arr[j]
        k=k+1
        j=i+1

            
        
    

def mergeSort(arr, left, right):
    if left < right:
        mid = (right + left) //2
        mergeSort(arr,left,mid)
        mergeSort(arr, mid +1, right)
        merge(arr, left,right, mid)

        

    
  
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
    mergeSort(arr, 0, len(arr) - 1) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
