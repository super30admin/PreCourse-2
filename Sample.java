// Time Complexity :
// Space Complexity :
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach

/*
Exercise 1 ->
For recursive binary search, we set the basecase as l>r, which means the element does not exist and we return -1. This case works because Binary
Search operates by halving the search space at every step. By continually halving, at one point we will have covered the entire space. This happens
when we end up with a left pointer which is larger than the right pointer.
We calculate mid by doing l + (r-l)/2 to avoid integer overflow. Then we compare arr[mid] to x.
If arr[mid] > x, that means the element could be present in the left half. So we call the function again, with r = mid - 1, l remains same. 
If arr[mid] < x, that means the element could be present in the right half. So we call the function again, with l = mid + 1, r remains same.
If arr[mid] == x, we return mid, which is the position of the search element.
Iterative approach is similar, instead of calling the function recursively, we use a while loop with the appropriate conditions. This approach is
better as it improves the space complexity from O(log n) due to the recursion stack to O(1).
*/

/*
Exercise 2 ->
Quicksort is a divide-and-conquer algorithm, which breaks down a problem into smaller subproblems and builds the final solution by solving these smaller
subproblems. The main idea behind quicksort is a "pivot". The pivot is an element which is placed at the correct place in the array. The constraints are:
-> all elements < the pivot are placed to the left of the pivot
-> all elements >= the pivot are placed to the right of the pivot
Basically the array will look like -> [< elements | PIVOT | >= elements]
Once we achieve this structure, we can call the quicksort function again on the left half & the right half (excluding pivot, as it is already in the
sorted position). The constraint for valid recursion will be "atleast 2 elements should be present in the array", since 1 element by itself is 
considered to be already sorted. Since we are using low & high pointers, this condition will be -> if(low < high)
The flow of the quickSort() function will be ->
1. Check low/high condition
2. Find partition index for array between low...high
3. Recursively call quickSort() for low to partitionIndex - 1 & for partitionIndex + 1 to high.

The partition() function is where the core logic resides. We select the pivot as arr[high] always (last element of the array/subarray we are working on).
Then we define 2 pointers i & j which will be the iterators for the left part & right part respectively. The left part should contain elements < pivot
and the right part should contain elements >= pivot. So we run a while loop with the correct conditions to prevent access to invalid indices. Our aim 
is to find an element which is >= pivot in the left half as this violates our constraints. Once we find a problematic element in the left half, we break
the loop & i will contain the index to this element. We do the same thing for the right half (j). Once the second while loop breaks, j will contain the 
index of an element which is < pivot in the right half.
We then check if(i < j), because it could be possible that we have exceeded the partition and the i & j pointers have spilled into the wrong half. If 
i < j, that means both pointers are still in the correct half and we swap the problematic elements so that they can be in the correct halves. This whole
process continues till i < j. Once we break out of the main loop, we have successfully partitioned the elements into left and right halves according to 
our constraints. The only thing remaining now is to put the pivot in the correct position and then returning the correct index of pivot (partition index).
The correct index for the pivot will be the index where i spills over into the right half invalidating the i < j condition.
The final condition of the array after going through the partition function will be:
-> arr[low...i-1] = elements < pivot
-> arr[i] = pivot in correct position
-> arr[i+1...high] = elements >= pivot

Once the partition index is returned, the main quickSort() function continues recursively and we end up with a sorted array. TC/SC explained in the code.

The worst case TC of O(n^2) can be avoided with good pivot selection. A deterministic algorithm called 'median of medians' exists, which splits the array into 
groups of 5, sorts each group of 5 elements (O(1), since 5 is a constant). Then it finds the median of each group and puts these medians into an array of medians. 
Then the same process of splitting into groups and findind the median is done again, till we end up with one median. This final median is used as a pivot for the 
original array. Repeat this process during pivot selection for each subarray.
This is proven to avoid the O(n^2) worst case. In most cases, the overhead of finding the median of medians every time is not worth it. The randomized pivot 
selection process works well and picking the worst possible pivot has a very low probability.
In our logic (selecting last element as pivot), the worst case TC will be for a reverse sorted array & already sorted array. The already sorted array case is
handled in code.
*/

/* 
Exercise 3 ->
Brute force approach here would be to traverse the entire linked list and using an int to track the lenght of the list. Then we iterate again 
length/2 times and we reach the middle node. This requires 2 traversals but the time complexity would still be O(n), where n = length of linked list.
Optimized approach (only one traversal required):
Used the fast and slow pointer technique to print the middle of the linked list.
Both pointers start at head. Fast jumps 2 nodes (fast = fast->next->next) & slow jumps one node at a time.
We need to be careful about null pointer exceptions here. If size of the linkedlist is even, fast ptr will end up overshooting the last node and
point to null. If size is odd, then fast pointer will point to the last node at the end. So the while loop condition will be:
while(fast!=nullptr && fast->next!= nullptr)
The slow pointer will point to the middle of the linkedlist after the while loop completed execution.
This results in n/2 iterations, but that still ends up being O(n) time complexity asymptotically.
*/

/* 
Exercise 4 ->
The merge sort algorithm is also a divide-and-conquer algorithm like quick sort. The idea here is to continually split the array into halves. We keep 
splitting till we reach a subarray with only one element (already sorted). Then we merge the smaller sorted subarrays back together. This merge step
uses a temp array to compare elements from each half and place them in sorted order. After merging the parent array is updated with this sorted result.
We use a mid element to split the array into half everytime. We recursively call mergeSort on (low, mid) and (mid+1, r). The if condition in the 
mergeSort() function if(l < r) makes sure that there are atleast 2 elements in the array. Mid calculation is done as l + (r-l)/2 to avoid integer overflow.
In the merge function, we use 2 pointers i and j to act as iterators for the left & right subarrays respectively. We then merge the 2 subarrays into a 
temp array in sorted order. After that we handle the case where either the left or the right subarray has elements which havent been merged. After we construct
the merged array, we simply replace the elements between indices l & r in the original array, with the elements of this merged array.
TC, SC explained in the code file.
*/

/*
Exercise 5 ->
In the iterative approach, everything remains the same logically. The only change is replacing the recursive quickSort() function with a stack approach.
If we observe the previous recursive approach, we tweak the low/high pointers based on the partition index and call the function again. We do the same 
thing here, except we push these new low/high pointers onto a stack and pop them in a LIFO manner inside a loop to mimic recursion.
The advantage of this approach is:
- There is no recursion limit/stack overflow errors.
- It limits the recursive call overhead.
*/