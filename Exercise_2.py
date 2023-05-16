#In case of time complexity, for average case it is O(nlogn), for worst case it is O(n^2)
#Space complexity is O(logn)
#Code ran successfully in leetcode terminal
#I faced no problems while implementing this code

#Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):


    #write your code here
    #here I am considering pivot as the left most value
    pivot=arr[low]
    #I am taking low into i
    i=low
    #I am taking high into j
    j=high
    #Here I am keeping a condition such that while loop should run only if i is less than j
    while(i<j):
        #here I am implementing 'do while' 
        #i will be incremented until value of arr[i] is greater than pivot
        while True:
            i+=1
            #here I included another condition because if there is no value greater than pivot, it should break at the end
            if(i==high or arr[i]>pivot):
                break
        #here I am implementing 'do while' 
        #j will be decremented until value of arr[j] is less than or equal to pivot
        while True:
            j-=1
            #here I inlcuded another condition because if there is no value <= pivot, it should stop before pivot
            if(j<low+1 or arr[j]<=pivot):
                break
        #only if i is less than j, swapping of values needs to be done
        if(i<j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #after the while loop, finally we need to swap pivot with arr[j] value and return the value of j        
    temp=arr[j]
    arr[j]=arr[low]
    arr[low]=temp
    return j

# Function to do Quick sort 
def quickSort(arr,low,high): 

    #write your code here
    #Here I included condition in if to make sure that atleast one value is there in the array
    if(low<high):
        #partitioning of array
        j=partition(arr,low,high)
        #first part of partition will undergo same process recursively
        quickSort(arr,low,j)
        #second part of partition will undergo same process recursively
        quickSort(arr,j+1,high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
#here I am sending n directly as we will be doing decrement for j using do while in partitioning
quickSort(arr,0,n) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
