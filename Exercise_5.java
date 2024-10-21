/*
Time Complexity : O(n log n) best case and O(n^2) worst case, same as recursive approach

Space Complexity:
    Best case: O(log n) This is due to the depth of the stack when the partitions are balanced.
    The space used for the stack grows logarithmically with the number of elements in the array.
    
    Worst case: O(n) due to unbalanced partitions
 */
import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        if (i != j)
        {
            /*
                X= 10 , Y= 15

                X = X + Y = 10 + 15 = 25
                Y = X - Y = 25 - 15 = 10
                X = X - Y = 25 - 10 = 15
             */
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
        /*
            Taking the last element as pivot, and here we will be using two pointers which will traverse as we compare it with the pivot
        */
        int pivot = arr[h];
        int leftPointer = l;
        int rightPointer = h;

        while (leftPointer < rightPointer)
        {
            /*
                The first while loop is for checking the left element in the array is less than or equal to pivot
                eg: 1, 90, 87, 6, 110, 100
                    pivot = 100, leftPointer = 0, rightPointer = 4
                    arr[0] = 1
                    1 <= 100 {true} && 0 < 4 {true}
                    leftPointer++ => leftPointer = 1

                The second while loop is for checking the right element in the array is greater than or equal to pivot
                    In above example, pivot = 100, leftPointer = 1, rightPointer = 4
                    arr[4] = 110
                    110 >= 100 {true} && 1 < 4 {true}
                    rightPointer-- => rightPointer = 3
             */
            while (arr[leftPointer] <= pivot && leftPointer < rightPointer)
                leftPointer++;

            while (arr[rightPointer] >= pivot && leftPointer < rightPointer)
                rightPointer--;

            // The check before swapping (if (leftPointer < rightPointer)) prevents unnecessary swaps when the pointers meet
            if (leftPointer < rightPointer) {
                swap(arr, leftPointer, rightPointer);
            }
        }

        // After one iteration with the pivot, it swaps the pivot with the position where leftPointer == rightPointer
        swap(arr, leftPointer, h);

        return leftPointer;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h)
    { 
        //Try using Stack Data Structure to remove recursion.

        /*
               eg: Initial Array: [4, 3, 5, 2, 1, 3, 2, 3]
               First Iteration
               ---------------
               1. Stack: [(0, 7)]
               2. stack not empty
               3. pop => l=0, h=7
               4. partition => after result => [2, 1, 3, 4, 5, 3, 2, 3], pivot 3 at index 2
               5. push indices of left sub arr (0, 1)
               6. push indices of right sub arr (3, 7)
               Stack: [(0, 1), (3, 7)]
         */
        // Create a stack to hold the start and end indices of sub-arrays
        Stack<Integer> stack = new Stack<>();

        // 1. Push the initial indices of the array
        stack.push(l);
        stack.push(h);

        // 2. Keep processing until the stack is empty
        while (!stack.isEmpty()) {
            // 3. Pop the high and low indices
            h = stack.pop();
            l = stack.pop();

            // 4. Partition the array and get the pivot index
            int p = partition(arr, l, h);

            // 5. Push the indices of the left sub-array onto the stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // 6. Push the indices of the right sub-array onto the stack
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
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