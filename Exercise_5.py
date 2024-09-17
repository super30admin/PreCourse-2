# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
     pivot=l
     L=l+1
     while(L<=h):
         if (arr[L]>arr[pivot]) and (arr[h]<arr[pivot]) :
             arr[L],arr[h]=arr[h],arr[L]
             L+=1
             h-=1
         elif (arr[L]<=arr[pivot]):   
             L+=1
         elif (arr[h]>=arr[pivot]):

            h-=1
     arr[pivot],arr[h]=arr[h],arr[pivot]
     return h

def quickSortIterative(arr, l, h):
     s=h-l+1
     stack=[0]*s
     top=-1
     
     top+=1
     stack[top]=l
     top+=1
     stack[top]=h
     while(top>=0):
         h=stack[top]
         top-=1
         l=stack[top]
         top-=1

         p=partition(arr,l,h)
         if (p-1)>l:
             top+=1
             stack[top]=l
             top+=1
             stack[top]=p-1
             
         if (p+1<h):
             top+=1
             stack[top]=p+1
             top+=1
             stack[top]=h
             
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr)
print(arr)
quickSortIterative(arr,0,n-1) 
print ("Sorted array is:") 
print(arr)
"""
Please note I checked on google to understand the concept as I didn't knew iterative Quicksort
TimeComplexity: O(n^2)-worst  case, best case- O(nlogn)
Space Compexity: O(n)-worst case
"""
