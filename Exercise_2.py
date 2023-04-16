# Python program for implementation of Quicksort Sort 
  
#Time complexity
# O(log n)
#Space complexity
#O(1)

# give you explanation for the approach
def quickSort(arr):

    less = []
    equals = []
    greater = []
    if len(arr) > 1:
        pivot = arr[0]

        for x in arr:
            if x < pivot:
                less.append(x)
            
            elif x == pivot:
                equals.append(x)

            else:
                greater.append(x)

        return quickSort(less) + equals + quickSort(greater)

    else:
        return arr
    
    

arr = [6, 9, 4, 3, 1, 2]
res = quickSort(arr)
print(res)
 
