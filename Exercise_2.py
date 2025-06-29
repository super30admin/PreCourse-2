'''
Quick sort.
'''

# Time Complexity : O(n log n) on average, O(n^2) in the worst case, O(n log n) in the best case
# Space Complexity : O(log n) due to recursive stack space
# Did this code successfully run on Leetcode : Yes, I ran this on GeeksforGeeks and it worked fine
# Any problem you faced while coding this : Yes, to find the pivot and partition the array correctly was a bit tricky, but I managed to implement it correctly.

# Python program for implementation of Quicksort Sort 

class Solution: # class name should be Solution
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high): # humne quickSort function banaya hai jo list arr ke saath low aur high index ko le raha hai (we have created a quickSort function that takes the list arr along with low and high indices)
        # code here
        if low<high: # agar low index high index se chhota hai (if low index is less than high index)
            p = self.partition(arr,low,high) # partition function call karte hain (we call the partition function)
            self.quickSort(arr,low,p-1) # quickSort function ko low se p-1 tak call karte hain (we call the quickSort function from low to p-1)
            self.quickSort(arr,p+1,high) # quickSort function ko p+1 se high tak call karte hain (we call the quickSort function from p+1 to high)
        return arr # sorted array return karte hain (we return the sorted array)
    
    def partition(self,arr,low,high): # partition function banaya hai jo list arr ke saath low aur high index ko le raha hai (we have created a partition function that takes the list arr along with low and high indices)
        # code here
        pivot = arr[high] # pivot ko high index se lete hain (we take the pivot from the high index)
        i = low-1 # i ko initialize karte hain low-1 se (we initialize i to low-1 i.e. one less than low index)
        for j in range(low,high): # low se high tak loop chalayenge (we will loop from low to high)
            if arr[j]<pivot: # agar arr[j] pivot se chhota hai (if arr[j] is less than pivot)
                i=i+1 # i ko increment karte hain (we increment i)
                arr[i],arr[j]=arr[j],arr[i] # arr[i] aur arr[j] ko swap karte hain (we swap arr[i] and arr[j])
        arr[i+1],arr[high]=arr[high],arr[i+1] # arr[i+1] aur arr[high] ko swap karte hain (we swap arr[i+1] and arr[high])
        return i+1 # i+1 ko return karte hain (we return i+1)
    
from typing import List

if __name__ == "__main__":
    # Example usage
    sol = Solution()
    arr = [10, 7, 8, 9, 1, 5]
    low = 0
    high = len(arr) - 1
    print(sol.quickSort(arr, low, high))  # Output: [1, 5, 7, 8, 9, 10]




