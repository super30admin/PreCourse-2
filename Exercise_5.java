import java.util.Stack;

// TimeComplexity :O(n log n)
// SpaceComplexity :O(log n)
class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    {
        if (i != j) {
            arr[i] = arr[i] ^ arr[j];
            arr[j] = arr[i] ^ arr[j];
            arr[i] = arr[i] ^ arr[j];
        }    }
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        int i = (l - 1);

        for (int j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        // Create a stack for indices
        Stack<Integer> stack = new Stack<>();

        // Push initial values of l and h to stack
        stack.push(l);
        stack.push(h);

        // Keep popping from stack while it is not empty
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();

            int p = partition(arr, l, h);

            // If there are elements on the left side of pivot,
            // then push left side to stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If there are elements on the right side of pivot,
            // then push right side to stack
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