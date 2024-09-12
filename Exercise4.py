def merge_list(a,b):
    result = []
    l, r = len(a), len(b)
    i = j =0
    while(i<l and j<r):
        if(a[i]<b[j]):
            result.append(a[i])
            i = i+1
        else:
            result.append(b[j])
            j = j+1
    return result + a[i:] + b[j:]

def mergeSort(arr):
    length = len(arr)
    if(length==2):
        if(arr[0]<arr[1]):
            return arr
        else:
            return arr[::-1]
    elif(length==1):
        return arr
    left = mergeSort(arr[:int(length/2)])
    right = mergeSort(arr[int(length/2):])
    if(left is not None or right is not None):
        a = merge_list(left,right)
        return a

arr = [12, 11, 13, 5, 6, 7, 1,3,6,8,0,345,234,65,-1,-2345]
print ("Given array is", end="\n")
print(arr)
print("Sorted array is: ", end="\n")
print(mergeSort(arr))


'''
#output

Given array is
[12, 11, 13, 5, 6, 7, 1, 3, 6, 8, 0, 345, 234, 65, -1, -2345]
Sorted array is:
[-2345, -1, 0, 1, 3, 5, 6, 6, 7, 8, 11, 12, 13, 65, 234, 345]
'''
