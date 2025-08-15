// Time Complexity :
//   partition() -> O(r - l)
//   QuickSort() -> Average O(n log n), Worst O(n^2) when partitions are very unbalanced
// Space Complexity :
//   O(log n) to O(n) for the manual stack in worst case (no recursion is used)
// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this :
//   - Off-by-one mistakes with l, h, i, j in partition.
//   - Iterative version needs an explicit stack for (l, h) ranges.
//   - Swapping without a temp variable: XOR-swap must guard against i == j.
// Your code here along with comments explaining your approach:
//   - Use Lomuto partition with the last element as pivot.
//   - Implement iterative QuickSort using an int[] stack to store subarray bounds.
//   - Swap via XOR (no extra variable), but skip when i == j to avoid zeroing.
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
    if (i == j) return;            // important: XOR-swap on same index would zero it
        arr[i] ^= arr[j];
        arr[j] ^= arr[i];
        arr[i] ^= arr[j]; 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];            // last element as pivot (Lomuto scheme)
        int i = l - 1;                 // boundary of "≤ pivot" region
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);           // place pivot in correct spot
        return i + 1;                  // return pivot index
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if (l >= h) return;

        // Stack to store subarray bounds (l, h) pairs
        int[] stack = new int[h - l + 1]; 
        int top = -1;

        // push initial bounds
        stack[++top] = l;
        stack[++top] = h;

        // Process while there are subarrays to sort
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];

            int p = partition(arr, l, h);

            // If left side has >1 element, push its bounds
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }
            // If right side has >1 element, push its bounds
            if (p + 1 < h) {
                stack[++top] = p + 1;
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