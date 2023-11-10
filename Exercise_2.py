# Python program for implementation of Quicksort Sort give you explanation for the approach

#Time complexity : O(nlog(n))
#Space complexity : O(nlog(n))

# Function to do Quick sort 
def quickSort(arr): 
    #write your code here
    n = len(arr)
    if n <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_great = []
    items_less = []

    for item in arr:
        if item > pivot:
            items_great.append(item)
        else:
            items_less.append(item)
    return quickSort(items_less) + [pivot] + quickSort(items_great)


# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
#n = len(arr) 
print(quickSort(arr) )

  
 
