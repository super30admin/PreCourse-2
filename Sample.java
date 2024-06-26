// Time Complexity : O(log n)
// Space Complexity : O(1) as we are not using any extra variable or array.
// Did this code successfully run on Leetcode : Did not run on leetcode but ran this problem locally on laptop
// Any problem you faced while coding this : Solved problems related to this concept in class already. So, did not face that many issues.

// Your code here along with comments explaining your approach
// Main idea behind binary search is reducing the search space by half. So, we find the middle in sorted array.
// If we find the element in middle itself we return from the function.
// We compare middle element with our target and if the target is low then we search in left half otherwise in right half. 
// We do this until low and high pointers cross each other and if element not found we return -1.



// Time Complexity : O(n^2)
// Space Complexity : O(1) as we are not using any extra variable or array.
// Did this code successfully run on Leetcode : Did not run on leetcode but ran this problem locally on laptop
// Any problem you faced while coding this : Initially I forgot about all the different sorting techniques we have. So, I went through geeksforgeeks explantion to complete these questions.

// Your code here along with comments explaining your approach
// The main idea in quick sort it we select the pivot and place all the smaller elements on left side and all greater elements on right side.
// Then we partition on each side once the pivot is placed at it's right position.
// In this algorithm what we are doing it if the current pointer element is less than pivot assumed then we will swap the starting elements.
// For example - 10, 20, 70, 80, 40, 50. Now low = 10, high = 50 pivot = 50, i = -1.
// First 10 < 50 -> swap 10 with 10, 20 < 50 -> swap 20 with 20, 70 > 50 -> no swap, 80 > 50 -> no swap, 40 < 50 -> swapn 70 with 40, then at the end swap 
// (i+1) = 80 with high = 50. So, now 50 found it's right position. We can do same for all the elements on both sides. 



// Time Complexity : O(n)
// Space Complexity : O(1) as we are not using any extra variable or array.
// Did this code successfully run on Leetcode : Did not run on leetcode but ran this problem locally on laptop
// Any problem you faced while coding this : Initially I forgot about all the different sorting techniques we have. So, I went through geeksforgeeks explantion to complete these questions.

// Your code here along with comments explaining your approach
// The main idea here is we will keep 2 pointers slow and fast. The slow pointer will move one element at a time while fast pointer will move 2 elements at a time.
// So, by the time fast pointer will reach the end, slow pointer will be exactly at the middle. Both will start at the head itself.
// This is what we are doing in printMiddle -> iterating through whole list using fastPtr till either fastPtr is completely null or last element 
// where (fastPtr.next -> null).



// Time Complexity : O(nlog n)
// Space Complexity : O(n) as we are creating two half arrays and storing them in a variable.
// Did this code successfully run on Leetcode : Did not run on leetcode but ran this problem locally on laptop
// Any problem you faced while coding this : Initially I forgot about all the different sorting techniques we have. So, I went through geeksforgeeks explantion to complete these questions.

// Your code here along with comments explaining your approach
// Basically, in this process we are using divide and conquer mechanism. We are diving the array into two subarrays recursively and sort each half array.
// We recursively can call sort and sort it till we have array of each element. While merging we will have left subarray and right subarray.
// While merging we start from the begining of both subarrays and compare the the current element of both subarrays and place smaller element into original array.
// Then we move to the next element in the subarray from which the element was taken.



// Time Complexity : O(n log n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : Did not run on leetcode but ran this problem locally on laptop
// Any problem you faced while coding this : Initially I forgot about all the different sorting techniques we have. So, I went through geeksforgeeks explantion to complete these questions.


// Your code here along with comments explaining your approach
// The approach will be same for quicksort - highest index element will be pivot and in each iteration that element will be placed at it's right position.
// We can do it using stacks. After partitioning, if there are elements to the left of pivot it pushes indices of left subarray onto stack.
// If there are elements to the righ of the pivot it pushes indices of the right subarray into the stack. This process continues iteratively until all 
// subarrays have been partitioned and sorted. Here, each partitioned subarray is pushed into the stack for further processing until the entire array is sorted. 