import java.util.Stack;
// Time Complexity:
// partition(): O(N) in worst case, O(log N) in best case
// QuickSort(): O(N log N) on average due to partitioning
// Space Complexity: O(log N)
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
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
        int i = (l - 1);
        for (int j = l; j < h; j++) {
            if (arr[j] < pivot) {
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
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{l, h});

        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            l = range[0];
            h = range[1];

            if (l < h) {
                int p = partition(arr, l, h);
                stack.push(new int[]{l, p - 1});
                stack.push(new int[]{p + 1, h});
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