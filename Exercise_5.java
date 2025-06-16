// Time Complexity : Avg: O(n log n), Worst: O(n^2) [When we pick the smallest or largest element as the pivot]
// Space Complexity : Avg: O(log n), Worst: O(n) [Due to stack space]
// Did this code successfully run on Leetcode: Yes
// Any problem you faced while coding this: I was not able to swap without using an extra variable. I had to look it up. Sorry!

/* Approach:
 * 1.QuickSort is a divide-and-conquer sorting algorithm where we pick an element as the pivot,
 *   and rearrange the array so that all elements to the left of the pivot are smaller, and
 *   all elements to the right are greater.
 *
 * 2. In the iterative QuickSort function, we use a stack to simulate recursion. We store
 *    pairs of (low, high) indices on the stack to represent subarrays that need to be sorted.
 *
 * 3. Initially, we push the entire array’s range (l to h) onto the stack.
 *    While the stack is not empty, we pop a subarray range (l to h),
 *    partition it using the partition function, and get the pivot index.
 *
 * 4. If the subarray to the left of the pivot has more than one element (pi-1 > l),
 *    we push (l, pi-1) to the stack. Similarly, if the right side (pi+1 < h) has
 *    more than one element, we push (pi+1, h).
 *
 * 5. The partition function selects arr[high] as the pivot and places it in its correct
 *    sorted position, such that elements to the left are smaller and elements to the right are larger.
 *
 * 6. The swap function swaps elements at i and j indices using XOR (to avoid using an extra variable).
 */

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l-1;

        for(int j=l; j<h; j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;

        while(top >= 0){
            h = stack[top--];
            l = stack[top--];

            int pi = partition(arr, l, h);

            if (pi - 1 > l) {
                stack[++top] = l;
                stack[++top] = pi - 1;
            }
            
            if (pi + 1 < h) {
                stack[++top] = pi + 1;
                stack[++top] = h;
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 