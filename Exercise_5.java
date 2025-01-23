import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h]; // Choosing the last element as pivot
        int i = l - 1; // Index of smaller element

        for (int j = l; j < h; j++) {
            // If current element is smaller than or equal to pivot
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        // Swap the pivot element with the element at i+1
        swap(arr, i + 1, h);
        return i + 1; // Return the partition index
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.

        Stack<int[]> stack = new Stack<>();

        // Push initial values of l and h to the stack
        stack.push(new int[] { l, h });

        while (!stack.isEmpty()) {
            // Pop h and l
            int[] range = stack.pop();
            l = range[0];
            h = range[1];

            // Set pivot element at its correct position
            int p = partition(arr, l, h);

            // If there are elements on the left side of pivot, push left side to stack
            if (p - 1 > l) {
                stack.push(new int[] { l, p - 1 });
            }

            // If there are elements on the right side of pivot, push right side to stack
            if (p + 1 < h) {
                stack.push(new int[] { p + 1, h });
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
//        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        int arr[] = { 5, 4, 3, 2, 1 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length); 
    } 
} 