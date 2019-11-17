'''
1-- Brute force-- searching for item in array and returning corresponding index if found, else return -1 after exiting the loop

for i in range(r+1):
    if(arr[i]==x):
        return i
    else:
        continue
return -1

'''

def binarySearch(arr, l, r, x):
    '''
    2-- eliminate half elements
    '''
    if(r>l):
        mid_index = int(l + (r - l)/2)

        if(arr[mid_index]==x):
            return mid_index

        elif(arr[mid_index]<x):
            return binarySearch(arr,mid_index+1,r,x)

        elif(arr[mid_index]>x):
            return binarySearch(arr,0,mid_index,x)

        else:
            return -1

arr = [ 2, 3, 4, 10, 40 ,50,123]
x = 40
result = binarySearch(sorted(arr), 0, len(arr)-1, x)
if result != -1:
    print ("Element ",x,"is present at index: ",result )
else:
    print ("Element ",x," is not present in array")

y = 1245
result = binarySearch(sorted(arr), 0, len(arr)-1, y)
if result != -1:
    print ("Element ",y,"is present at index: ",result )
else:
    print ("Element ",y," is not present in array")


'''
#output
Element  40 is present at index:  4
Element  1245 is present at index:  None
'''
