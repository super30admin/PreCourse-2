# Python program for implementation of MergeSort
from math import  inf as infinity
def merge(a,l,m,r):
    n1=m-l+1
    n2=r-m
    left=[]
    right=[]
    for i in range(n1):
        left.append(a[l+i])
    for i in range(n2):
        right.append(a[m+1+i])
    left.append(infinity)
    right.append(infinity)

    i=j=0
    for k in range(l,r+1,1):
        if(left[i]<right[j]):
            a[k]=left[i]
            i=i+1
        else:
            a[k]=right[j]
            j+=1
        k+=1

def mergeSort(a,l,r):
    if(l<r):
        m=(l+r)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)
  
# Code to print the list 
def printList(arr):
    print(arr)

    
    #write your code here
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)-1)
    print("Sorted array is: ", end="\n") 
    printList(arr) 
