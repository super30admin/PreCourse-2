# Python program for implementation of Quicksort Sort
import numpy.random as random
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    '''
    :param arr: a list or segment of list
    :param low: start index
    :param high: end index
    :return: left,pivot,right
    '''
    pivot=random.randint(low,high+1)
    left=[]
    right=[]
    for i in range(low,high+1):
        if i != pivot:
            if arr[i]<=arr[pivot]:
                left.append(arr[i])
            else:
                right.append(arr[i])
    return left,[arr[pivot]],right

  

# Function to do Quick sort 
def quickSort(arr,low,high):
    #write your code here
    if low < high:
        left,value,right = partition(arr,low,high)
        return  quickSort(left,0,len(left)-1)+value+quickSort(right,0,len(right)-1)
    else:
        return arr
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
arr=quickSort(arr,0,n-1)
print ("Sorted array is:")
for i in range(n): 
    print ("%d" %arr[i])
  
 
