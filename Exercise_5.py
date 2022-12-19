#Time Complexity :
# O(Log N)

#Space Complexity :
# O(N)

#Did this code successfully run on Leetcode :
#I got 11/18 test cases to pass and had TLE on the rest
#Any problem you faced while coding this :
#Workig on the time issue

# Python program for implementation of Quicksort

def swap(arr,i,pivot_pos):
    #Swapping 2 elements
    elem1 = arr[i]
    arr[i] = arr[pivot_pos]
    arr[pivot_pos] = elem1


# This function is same in both iterative and recursive
def partition(arr, low, high):
    #write your code here
    pivot = arr[high]
    pivot_pos = high

    less_count = 0
    #Find the number of elements smaller than the pivot
    for i,elem in enumerate( arr[low:high+1]):
        if elem < pivot :
            less_count += 1
            continue
            #swap(arr,i,pivot_pos)
            #pivot_pos = i

    pivot_pos = less_count + low
    swap(arr,high,pivot_pos)
    #print ("less count", less_count)
    #print ("pivot", pivot_pos)
    low_pos = low
    #Place all the elements smaller than the pivot on the left side of the pivot
    for i,elem in enumerate(arr[low:high+1]):
        if elem < pivot :
            swap(arr,low_pos,i+low)
            low_pos += 1

    return pivot_pos  

def quickSortIterative(arr, low, high):
    #write your code here
    #creating a stack
    #Top keeps count of how many elements are in stack
    if len(arr[low:high+1]) == 1:
        return
    #If 2 elements, put them in correct position and return
    if len(arr[low:high+1]) == 2 :
        if arr[low] <= arr[high]:
            return arr
        else :
            elem = arr[low]
            arr[low] = arr[high]
            arr[high] = elem
            return arr
    stack = [0] * len(arr)
    top = 0
    #Adding initial elements in stack
    stack[top] = low
    top += 1
    stack[top] = high
    
    while top >= 0 :
        #Popping elements from stack (hence reducing count of top)
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        #Partitioning with a pivot value
        pivot_pos = partition(arr,low,high)
        
        #Checking if the pivot position has reached the leftmost point, then we are done processing this side
        if pivot_pos - 1 >low:
            top += 1
            stack[top] = low
            top+= 1
            stack[top] = pivot_pos -1

        #Checking if the pivot position has reached the rightmost point, then we are done processing this side
        if pivot_pos + 1 <high:
            top += 1
            stack[top] = pivot_pos+1
            top+= 1
            stack[top] = high

# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5,39,5,5,23] 
n = len(arr) 
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:",arr) 
