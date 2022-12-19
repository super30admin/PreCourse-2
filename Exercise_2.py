#Time Complexity :
# O(Log N)

#Space Complexity :
# O(N)

#Did this code successfully run on Leetcode :
#I got 11/18 test cases to pass and had TLE on the rest

#Any problem you faced while coding this :
#Workig on the time issue

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
import random

def swap(arr,i,pivot_pos):
    #Swapping 2 elements
    elem1 = arr[i]
    arr[i] = arr[pivot_pos]
    arr[pivot_pos] = elem1
    
#This function takes last element as pivot, places  
#the pivot element at its correct position in sorted  
#array, and places all smaller (smaller than pivot)  
#to left of pivot and all greater elements to right  
#of pivot
def partition(arr,low,high):
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

# Function to do Quick sort 
# The main function that implements QuickSort  
#arr[] --> Array to be sorted,  
#low --> Starting index,  
#high --> Ending index 
def quickSort(arr,low,high): 
    #write your code here
    if high <= low :
        return arr
    
    #If single element, return it
    if len(arr[low:high+1]) == 1:
        return arr
    #If 2 elements, put them in correct position and return
    if len(arr[low:high+1]) == 2 :
        if arr[low] <= arr[high]:
            return arr
        else :
            elem = arr[low]
            arr[low] = arr[high]
            arr[high] = elem
            return arr
    #Partition the list based on the last element as the pivot
    pivot_pos = partition(arr,low,high)
    print (arr,low,high)
    print (pivot_pos)
    #Sort the left half
    quickSort(arr,low,pivot_pos-1)
    #Sort the Right half
    quickSort(arr,pivot_pos+1,high)  
    return
  
# Driver code to test above 
#arr = [10, 7, 8, 9, 1, 5,23] 
arr = [5,2,3,1]
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:",arr) 
