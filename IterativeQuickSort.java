/** space complexity: O(1)
* time complexity: O(n^2)
* did this code successfully run on Leetcode: This is not a Leetcode problem
* any problem you faced while coding this:  Yes, the output isn't printed in my visual studio code until and unless I have the prinln statement. 
*/

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if (i != j) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;
        for (int j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
    /** The stack will hold the indices of the subarrays to be sorted (if both left and right subarrays haven't reached their base case yet then
    the stack would have the left and right indices of the subarrays i.e., total 4 indices in the stack)
    *  the stack would have the left and right indices of the subarrays i.e., total 4 indices in the stack)
    * when stack is not empty, we will pop the top two elements which will be the high and low indices of the subarray
    */
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();
            if (l < h) { // check to avoid invalid partitions
                int p = partition(arr, l, h);

                /** Push left subarray bounds 
                 * This if condition here corresponds to the base condition(l<h) in the recursive QuickSort to populate
                   i.e., here the stack is populated only when there is scope for further partitioning i.e., l<h condition can be met
                 */ 
                if (p - 1 > l) {
                    stack.push(l);
                    stack.push(p - 1);
                }
                 /* This if condition here corresponds to the base condition(l<h) in the recursive QuickSort to populate
                   i.e., here the stack is populated only when there is scope for further partitioning i.e., l<h condition can be met
                  * Push right subarray bounds
                  */
                if (p + 1 < h) {
                    stack.push(p + 1);
                    stack.push(h);
                }
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println();
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