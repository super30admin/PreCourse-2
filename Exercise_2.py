# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
'''
// Time Complexity : Worst O(N^2) BEST & AVG = O(N Log(N))
// Space Complexity :   O(Log(N)) As recursion adds a disk per recursive call
// Did this code successfully run on Leetcode : Time limit exceeds
// Any problem you faced while coding this : Code didn't handle duplicates
// Your code here along with comments explaining your approach

'''
'''
1. Take a pivot point , I took the first element
2. iterate left (after pivot) to right 
    if left is greater than pivot and right is less than pivot swap left and right
    if left is less than pivot increment left
    if right is greater than pivot decrement right
3. swap pivot and right
4. Two recursive calls 
    1: left to pivot sub array
    2: right to pivot sub array

'''

def partition(arr,start,end):
    if start>=end:
        return

    p=start
    left=start+1
    right=end

    while right>=left:
        if arr[left]>arr[p] and arr[right]<arr[p]:
            arr[left],arr[right]=arr[right],arr[left]
        if arr[left]<=arr[p]:
            left+=1
        if arr[right]>=arr[p]:
            right-=1
    
    arr[p],arr[right]=arr[right],arr[p]

    partition(arr,start,right-1)
    partition(arr,right+1,end)


# Function to do Quick sort 
def quickSort(arr,low,high): 
    partition(arr,low,high)
    return arr
    
    #write your code here
  
# Driver code to test above 
# arr = [10, 7, 8, 9, 1, 5] 
arr=[-4,0,7,4,9,-5,-1,0,-7,-1]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
