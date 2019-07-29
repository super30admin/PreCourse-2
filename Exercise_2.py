def partition(arr,low,high):
    i = ( low-1 )          
    pivot = arr[high]     
  
    for j in range(low , high): 
  

        if   arr[j] <= pivot: 
          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 


def quickSort(arr,low,high): 
	if low < high: 
		partition_index = partition(arr,low,high) 
		quickSort(arr, low, partition_index-1) 
		quickSort(arr, partition_index+1, high)
    
  
''' Driver Code'''

arr = [30, 44, 103, 10, 7, 8, 19, 9, 1, 5, 12, 72, 78] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
print (arr)