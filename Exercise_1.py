# Python code to implement iterative Binary  
# Search. 
  
# It returns location of x in given array arr  
# if present, else returns -1 
def binarysearch(arr,l,r,x):
    while(l<r):
        mid=(l+r)//2
#         mid=k/2
#         print(mid)
        if arr[mid]==x:
            return mid
        elif x>arr[mid]:
            l=mid+1
        else:
            r=mid-1
arr=[2,3,4,10,40]
x=10
result=binarysearch(arr,0,len(arr)-1,x)
if result!=-1:
    print("element is present at %d" %result)
else:
    print("Element is not present in the array")
    
changed excercise_1.py
