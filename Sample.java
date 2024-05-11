Exercise 1

Binary Search.

Time Complexity :  

O(LOG N)


Space Complexity :  O(1)


Any problem you faced while coding this : No


Your code here along with comments explaining your approach: 

Code :

def binarySearch(arr, l, r, x):

    flag = 0
    # write your code here
    while (l <= r):
        mid = (l+r)//2
        if (arr[mid] == x):
            flag = 1
            return mid
        if (arr[mid] > x):
            r = mid-1
        if (arr[mid] < x):
            l = mid+1
    if (flag == 0):
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 2

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")



Approach :

Finding the middle element of the array
Comparing the middle element with the target element to be seached
If the target element is lesser than the middle element, the right index is reduced to mid-1
If the target element is greater than the middle element, the left index is increased to mid+1
If the element found after updating the middle element, it is returned else if the left index is greater than the right index and element is not found, the search is complete and element is not found during the search

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Exercise 2

Quick sort ( Recursive )

Time Complexity :  

O(N LOGN)


Space Complexity :  O(1)


Any problem you faced while coding this : No


Your code here along with comments explaining your approach: 

def partition(arr,low,high):
    i=low
    j=high
    t=0
    v=0
    pivotElement=arr[low]

    while(i<j):
        while(arr[i]<= pivotElement and i<=high -1):
            i=i+1
        while(arr[j] > pivotElement and j>=low + 1):
            j=j-1
        
        if (i < j):
            t=arr[i]
            arr[i]=arr[j]
            arr[j]=t
    
    v=arr[low]
    arr[low]=arr[j]
    arr[j]=v
    
    return j


  # Function to do Quick sort 
def quickSort(arr,low,high): 
    if(low<high):
        pivotIndex=partition(arr,low,high)
        quickSort(arr,low,pivotIndex-1)
        quickSort(arr,pivotIndex+1,high)
   
  
# Driver code to test above 

arr = [10,7,8,9,1,5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i],end=" "), 

Approach :

We take a pivotElement which is the first element of the array
We compare the pivotElement to the rest of the array
The partition swaps the element when compare to the pivotElement, and based on this comparion,two partitions are created, one being all elements smaller or equal to the pivotelement and the being all elements greater than the pivotElement
This process keeps contiuning till the low index is smaller than the high index
The partition function keeps returning the pivotIndex to find the new pivotElement at each step




-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Exercise 3

Find Mid Point of a Singly Linked List.

Time Complexity :  

O(n)


Space Complexity :  O(1)

Any problem you faced while coding this : No


Your code here along with comments explaining your approach: 


Code:

class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def getLength(self):
        if self.head == None:
            return 0

        else:
            count = 0
            moverNode = self.head
            while (moverNode):
                moverNode = moverNode.next
                count = count+1
        return count

    def push(self, new_data):

        if self.head == None:
            self.head = Node(new_data)

        else:
            tempNode = Node(new_data)
            tempNode.next = self.head
            self.head = tempNode

    def show(self):

        moverNode = self.head
        while (moverNode):
            print(moverNode.data)
            moverNode = moverNode.next

    # Function to get the middle of
    # the linked list
    def printMiddle(self):

        if self.getLength() == 0:
            return "List is Empty"
        else:
            if self.getLength() % 2 == 0:
                move = (self.getLength()//2)-1
                move1 = (self.getLength()//2)
                moverNode2 = self.head
            else:
                move = (self.getLength()//2)
            moverNode = self.head
            count = 0
            while (count < move):
                moverNode = moverNode.next
                count = count+1
            count = 0
            if self.getLength() % 2 == 0:
                while (count < move1):
                    moverNode2 = moverNode2.next
                    count = count+1

                print("Middle Element :", moverNode2.data)

            print("Middle Element :", moverNode.data)


# Driver code
list1 = LinkedList()
list1.push(5)
list1.push(4)
list1.push(2)
list1.push(3)
list1.show()
list1.printMiddle()



Approach :

Created a getLength function which will return the total number of nodes in the linked list 
Based on the length, there will be two cases, one is for even length and one for odd length
In case of even length, there will two elements returned namely, (low+high)/2 th index and (low+high)/2 -1 th index 
In case of odd length, there will be one element returned, (low+high)/2 th index

Based on the length a moverNode which initially points to the head Node of the linked List will keep traversing and a counter keeps incrementing till the mid length is reached
Upon reaching the mid length, the middle element/s are returned

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exercise 4

Merge Sort.

Time Complexity :  

O(n log n)


Space Complexity :  O(n)

Any problem you faced while coding this : No


Your code here along with comments explaining your approach: 


Code:

def merge(arr, low, midPosition, high):
    temp = []
    left = low
    right = midPosition+1

    while (left <= midPosition and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left = left+1
        else:
            temp.append(arr[right])
            right = right+1

    while (left <= midPosition):
        temp.append(arr[left])
        left = left+1

    while (right <= high):
        temp.append(arr[right])
        right = right+1

    for i in range(low, high+1):
        arr[i] = temp[i-low]


def mS(arr, low, high):

    if low == high:
        return
    else:
        midPosition = (low+high)//2
        mS(arr, low, midPosition)
        mS(arr, midPosition+1, high)
        merge(arr, low, midPosition, high)


def mergeSort(arr):

    low = 0
    high = len(arr)-1
    mS(arr, low, high)

  # write your code here

# Code to print the list


def printList(arr):

    # write your code here
    print(arr)


    # driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)



Approach :

First we find a middle index of the array to split it into two arrays
We make a recursive call to mergeSort function on two different parts of the array
One iterates from the low to mid th index of the array
Other iterates from the mid+1 th index to the end of the array
This continues till low and high th are equal
Then the merge function is called
Wherein it compares both the elements of the arrays and based on the equality
The new sorted elements are put in the new array
Then the elements are transfeered to the old array

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Exercise 5

Quick Sort (Iterative).

Time Complexity :  

O(n log n)


Space Complexity :  O(1)

Any problem you faced while coding this : No


Your code here along with comments explaining your approach: 


Code:

def partition(arr, l, h):
  # write your code here
    i = l
    j = h
    t = 0
    v = 0
    pivotElement = arr[l]

    while (i < j):
        while (arr[i] <= pivotElement and i <= h - 1):
            i = i+1
        while (arr[j] > pivotElement and j >= l + 1):
            j = j-1

        if (i < j):
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t

    v = arr[l]
    arr[l] = arr[j]
    arr[j] = v
    return j


def quickSortIterative(arr, l, h):
  # write your code here
    arr2 = []
    arr2.append((l, h))

    while arr2:
        low, high = arr2.pop()
        if (low < high):
            pivotIndex = partition(arr, low, high)
            arr2.append((low, pivotIndex-1))
            arr2.append((pivotIndex+1, high))


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSortIterative(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i], end=" "),



Approach :


We use a stack to hold the low andd high positions
We keep append and popping th stack with both the indexes while the stack has elements
While the stack is not empty, the partition function is called and the new indices are appended into the stack
The partition function is called till low < high index

