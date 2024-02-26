import java.util.Stack;

class IterativeQuickSort {
    // Time Complexity : O(n * log n)
    // Space Complexity : O(log n)
    // Did this code successfully run on Leetcode : NA
    // Any problem you faced while coding this : Had to understand/learn to implement this. Recursive was easy
    void swap(int arr[], int i, int j) {
	    //Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) {
        //Compare elements and swap.
        int pivot = arr[high];
        int i = low - 1; // assuming all elements are greater than pivot

        // iterate through array to find elements smaller than pivot and place them in correct position
        //  loop will run through last-1 element as last element is pivot
        for(int j = low; j < high; j++){
            // element at j is smaller than pivot, swap with i
            if(pivot > arr[j]) {
                // increment i so we can swap
                i++;
                swap(arr, i, j);
            }
        }
        i++; // increment i, to swap with pivot. As i is the correct index for pivot
        swap(arr, i, high);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) {
        //Try using Stack Data Structure to remove recursion.
//        create stack
        Stack<Integer> stack = new Stack<>();
        // push low and high into it
        stack.push(low);
        stack.push(high);

        // do push and pop until stack is empty
        while(!stack.isEmpty()){
            high = stack.pop();
            low = stack.pop();

            // calculate partition, by passing low and high we popped from stack
            int pivotIndex = partition(arr, low, high);

            // check if pivotIndex is first index or low of an array or not,
            // if not push to stack because there are more elements which need to be sorted in array

            if(pivotIndex - 1 > low) {
                stack.push(low); // if so then again push low to stack, say left side sub-array of pivotIndex
                stack.push(pivotIndex -1 ); // push high of left side sub-array
            }

            // check if pivotIndex+1 is smaller than high, if so then there are more elements after pivotIndex,
            // push them to stack
            if(high > pivotIndex + 1){
                stack.push(pivotIndex + 1); // if so then again push low to stack, say right side sub-array of pivotIndex
                stack.push(high); // push high of right side sub-array
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) {
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 