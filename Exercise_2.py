# Time Complexity : O(NlogN)
# Space Complexity : O(1), but will have more space complexity due to recusion stack O(logN)
# Did this code successfully run on Leetcode :

# Any problem you faced while coding this :

# Your code here along with comments explaining your approach
def partition(arr,low,high):
    p=arr[high]
    temp=low-1
    def swap(arr, a, b):
        t=arr[a]
        arr[a]=arr[b]
        arr[b]=t
    for i in range(low, high):
        if(arr[i]<=p):
            temp+=1
            swap(arr, i, temp)
    swap(arr,high, temp+1)
    return temp+1

# Function to do Quick sort 
def quickSort(arr,low,high): 
    if(low<high):
        p= partition(arr, low, high)

        quickSort(arr,low, p-1)
        quickSort(arr, p+1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5, 1, 1] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
