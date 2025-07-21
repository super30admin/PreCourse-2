//Time Complexity: Average case-> O(nlogn) , Worst Case->O(n^2)
//Space Complexity: O(n)
//Did the code successfully run on Leetcode: Yes
//Any problem faced while coding this: No

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
       if (i != j) {
        // 1) sum the two
        arr[i] = arr[i] + arr[j];
        // 2) extract original arr[i] into arr[j]
        arr[j] = arr[i] - arr[j];
        // 3) extract original arr[j] into arr[i]
        arr[i] = arr[i] - arr[j];
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = l - 1;                      // i tracks the end of "<= pivot" zone
        for (int j = l; j < h; ++j) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        // place pivot just after the "<= pivot" zone
        swap(arr, i + 1, h);
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        // Stack of (l, h) pairs:
        java.util.Deque<int[]> stack = new java.util.ArrayDeque<>();
        stack.push(new int[]{l, h});

        // Process until no more subarrays to sort
        while (!stack.isEmpty()) {
            int[] range = stack.pop();
            l = range[0];
            h = range[1];

            if (l < h) {
                // Partition and get pivot position
                int p = partition(arr, l, h);
                    // Push the two subranges that need sorting
                if (p - 1 - l > h - (p + 1)) {
                    stack.push(new int[]{l, p - 1});
                    stack.push(new int[]{p + 1, h});
                } else {
                    stack.push(new int[]{p + 1, h});
                    stack.push(new int[]{l, p - 1});
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