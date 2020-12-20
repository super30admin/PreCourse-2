#Time complexity = O(nlogn) expected case
#space complexity= O(logn) 



# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr):
  
  
    #write your code here
    if(len(arr)<=1):
        return arr
    else:
        l=[] #values less than pivot are stored here
        r=[] #values greater than pivot are stored in r
        p=arr[0]#pivot
        count=0 #count of the pivot 
        for i in arr:
            if(i>p):
                r.append(i)
            elif(i<p):
                l.append(i)
            else:
                count+=1
 
        b=partition(l)# recursively calling the left sub partition
        c=partition(r)# recursively calling the right sub partition
        m=[p for i in range(count)] # storing the equal elements
        
        return b+m+c

# Function to do Quick sort 
def quickSort(arr,low,high): 
    
    #write your code here
    return partition(arr)
    
    
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
arr=quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 