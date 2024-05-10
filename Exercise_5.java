//Time Complexity: O(nlogn)
//Space Complexity: O(1)  
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : NO

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//swapping without extra variable 
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
        int pivot = arr[h];
        int i = (l - 1); // smaller element index is calculated
        for (int j = l; j < h; j++) {
            // Check if current element is <= to pivot 
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
        // Create an auxiliary stack
        int[] stack = new int[h - l + 1];

        // Initialized the top of stack
        int top = -1;

        // we push the initial values to stack. Increment top pointer and then push the element. 
        stack[++top] = l;
        stack[++top] = h;

        // Pop elements until stack is not empty
        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];

            // Set pivot element at its correct position
            int p = partition(arr, l, h);

            // If there are elements on the left side array (left to pivot),then push that to the stack
            if (p - 1 > l) {
                stack[++top] = l;
                stack[++top] = p - 1;
            }

            // If there are elements on the right side array (right to pivot),then push that to the stack
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