# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
     pivot=low
     L=low+1
     while(L<=high):
         if (arr[L]>arr[pivot]) and (arr[high]<arr[pivot]) :
             arr[L],arr[high]=arr[high],arr[L]
             L+=1
             high-=1
         elif (arr[L]<=arr[pivot]):
             
             L+=1
         elif (arr[high]>=arr[pivot]):
            
            high-=1
     arr[pivot],arr[high]=arr[high],arr[pivot]
     return high

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if (low<high):
        pElement=partition(arr,low,high)
        quickSort(arr,low,pElement-1)
        quickSort(arr,pElement+1,high)
    
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print("%d" %arr[i])
