# Python program for implementation of MergeSort 
#Time Complexity: O(NlogN)  Each recursive call splits the list in half, which is N times
#Space Complexity: O(N)  We need to allocate space for another n elements
def merge(l, r):
    if len(l) == 0: return r
    if len(r) == 0: return l

    if l[0] < r[0]:
        return [l[0]] + merge(l[1:], r)
    else:
        return [r[0]] + merge(l, r[1:])

def split(arr):
    left = []
    right = []

    go_left = False
    for x in arr:
        if go_left:
            left.append(x)
        else:
            right.append(x)

        go_left = not go_left

    return (left, right)


def mergeSort(arr):
  if len(arr) < 2: return list(arr)
  ls = split(arr)

  l = mergeSort(ls[0])
  r = mergeSort(ls[1])

  return merge(l, r)

  
# Code to print the list 
def printList(arr): 
    print(arr)

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
     
    print("Sorted array is: ", end="\n") 
    print(mergeSort(arr))
