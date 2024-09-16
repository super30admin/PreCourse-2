def partition(arr, low, high):
 print("sample=", arr)
 pivot = arr[high]
 index = low
 current = low
 while (current < high):
  if( arr[current] <= pivot):
   arr[index], arr[current] = arr[current], arr[index]
   index += 1
  current += 1
 arr[high], arr[index] = arr[index], arr[high]
 print("partitioned=", arr)
 return index


# Function to do Quick sort 
def quickSort(arr,low,high):

    if low<high:
        index=partition(sample,low,high)
        quickSort(sample,low,index-1)
        quickSort(sample,index+1,high)
    
    #write your code here
  
# Driver code to test above 
sample = [10,7,8,9,1,5] 
n = len(sample) 
quickSort(sample,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %sample[i]), 
