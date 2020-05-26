// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach


//Problem 1: Binary Search

//   Time Complexity : The time complexity for this problem is O(log n) as we divide the list of elements by 2 until we reach the index.
//   Space Complexity : Space complexity would be O(1) as we did not use any extra memory aprt from input array
//   Any problem you faced while coding this : No


//Problem 2: Quick Sort

//   Time Complexity : The worst time complexity for this problem is O(n^2) if the elements are already in sorted order and it would be O(n log n)
//                      n times for partinioning and log n times for recursion.
//   Space Complexity : Space complexity would be O(log n)
//   Any problem you faced while coding this : Stack tracing during recursion was difficult to keep track while debugging


//Problem 3: Mid point of Singly Linked list

//   Time Complexity : The worst time complexity for this problem is O(n/2) As we use double pointer, we can find the mid element in n/2 traversal
//   Space Complexity : The space complexity for this problem would be O(n+n) as we have 2 pointers
//   Any problem you faced while coding this : No


//Problem 4: Merge Sort
//   Time Complexity : The worst time complexity for this problem is O(n log n) n times for merging and log n times for recursion.
//   Space Complexity : Space complexity would be O(n + n) as we used two temp array during merge
//   Any problem you faced while coding this : Trying to understand how merging was bit tricky


//Problem 5: Iterative Quick Sort

//   Time Complexity : I think it has same time complexity as recursive approach with worst time complexity as O(n^2) if the elements are already in sorted order
//                      and it would be O(n log n) n times for partinioning and log n times for recursion.
//   Space Complexity : The space complexity would be O (n + log n) we use n space for the stack.
//   Any problem you faced while coding this : Was not able to achieve swapping without extra variable as difference between two values was throwing zero