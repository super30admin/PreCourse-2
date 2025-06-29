'''
MergeSort 
'''

# Time Complexity : O(n log n) for the merge sort algorithm, the merge operation takes O(n) time, and the depth of the recursion tree is log n.
# Space Complexity : O(n) for the merge sort algorithm, as it requires additional space for the temporary arrays used during the merge operation.
# Did this code successfully run on Leetcode : Yes, the code runs successfully on Leetcode and passes all test cases.
# Any problem you faced while coding this : Yes, understanding the merge operation and how to split the array into halves was a bit challenging initially, but it became clearer with practice.

# Python program for implementation of MergeSort 
def mergeSort(arr): # humne function ko mergeSort naam diya hai jo array ko sort karega (We have named the function mergeSort which will sort the array)
    #write your code here
    if len(arr) > 1: # Yeh base case hai, agar array ki length 1 se zyada hai toh hum merge sort karenge (This is the base case, if the length of the array is greater than 1, we will perform merge sort)
        mid = len(arr) // 2  # array ke beech ka index nikalna (Finding the middle index of the array)
        L = arr[:mid]        # Left half of the array jismain starting se lekar mid tak ke elements hain (Left half of the array which contains elements from the start to mid)
        R = arr[mid:]        # Right half of the array jismain mid se lekar end tak ke elements hain (Right half of the array which contains elements from mid to end)

        mergeSort(L)         # humne recursive call kiya hai left half ke liye jo ki merge sort karega (We have made a recursive call for the left half which will perform merge sort)
        mergeSort(R)         # humne recursive call kiya hai right half ke liye jo ki merge sort karega (We have made a recursive call for the right half which will perform merge sort)

        i = j = k = 0        # i, j, k ko 0 se initialize kiya hai kyunki humne arrays L aur R ke elements ko compare karna hai (Initialized i, j, k to 0 because we will compare the elements of arrays L and R)
        # i is the index for L[], j is the index for R[] and k is the index for arr[]

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R): # Yeh loop tab tak chalega jab tak L aur R ke elements khatam nahi ho jate (This loop will run until the elements of L and R are exhausted)
            if L[i] < R[j]: # Agar L ka element R se chhota hai toh hum L ka element arr mein daalenge (If the element of L is smaller than R, we will put the element of L in arr)
                arr[k] = L[i] # arr mein L ka element daalna (Putting the element of L in arr)
                i += 1 # L ka index badhana (Incrementing the index of L)
            else: # Agar R ka element L se chhota hai toh hum R ka element arr mein daalenge (If the element of R is smaller than L, we will put the element of R in arr)
                arr[k] = R[j] # arr mein R ka element daalna (Putting the element of R in arr)
                j += 1 # R ka index badhana (Incrementing the index of R)
            k += 1 # arr ka index badhana (Incrementing the index of arr)

        # Checking if any element was left in L[] or R[]
        # Agar L ya R mein koi element bacha hai toh hum usse arr mein daalenge (If there are any elements left in L or R, we will put them in arr
        while i < len(L): # Agar L mein koi element bacha hai toh hum usse arr mein daalenge (If there are any elements left in L, we will put them in arr)
            arr[k] = L[i] # arr mein L ka element daalna (Putting the element of L in arr)
            i += 1 # L ka index badhana (Incrementing the index of L)
            k += 1 # arr ka index badhana (Incrementing the index of arr)

        while j < len(R): # Agar R mein koi element bacha hai toh hum usse arr mein daalenge (If there are any elements left in R, we will put them in arr)
            arr[k] = R[j] # arr mein R ka element daalna (Putting the element of R in arr)
            j += 1 # R ka index badhana (Incrementing the index of R)
            k += 1 # arr ka index badhana (Incrementing the index of arr)

# Code to print the list
def printList(arr):
    for i in arr:
        print(i, end=" ")
    print()


# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
