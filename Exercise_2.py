# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while True:
        while True:
            if arr[i] > pivot or i>= high:
                break
            i = i+1
        while True :
            
            if arr[j] < pivot or j <=0 :
                break
            j = j-1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print(arr)
        
            
        if i >= j:
            print(i, "i")
            print(j, "j")

            temp = arr[low]
            arr[low] = arr[j]
            arr[j] = temp
            print(arr[low], arr[j], arr)

            return j

        
        

        
        
        
    
   
    
    
    #
    #
         
#write your code here
  

# Function to do Quick sort 

def quickSort(arr,low,high): 
    if low < high : 

        part = partition(arr, low, high)
        if part >= high:

            quickSort(arr,low,part-1)
        if part< high:

            quickSort(arr, part+1,high)

        

        



        
 
    #write your code here
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
#quickSort(arr,0,n-1)

quickSort(arr, 0, n-1)
 

print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),