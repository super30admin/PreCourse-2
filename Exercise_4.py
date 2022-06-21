'''
Time complexity : O(NlogN)
Space Complexity : O(N)
'''
def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]

            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if r > l:
        m = (r + l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

# Code to print the list 
def printList(arr):
  for i in arr:
    print(i," ",end="")
  print("")
  print("-------------------")
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr,0,len(arr)) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
