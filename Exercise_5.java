//time complexity = O(nlogn)
//space complexity = O(n)

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
	    arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
	    int pivot = arr[h];  // Take the last element as pivot
        int i = (l - 1);  // Index of the smaller element
        
        // Traverse through all elements to put smaller elements on the left of pivot
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++;  // Increment the index of smaller element
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);  // Swap the pivot element with the element at index i+1
        return i + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
	    Stack<Integer> stack = new Stack<>();
        
        // Push initial values to the stack
        stack.push(l);
        stack.push(h);
        
        // Pop elements from the stack until the stack is empty
        while (!stack.isEmpty()) {
            h = stack.pop();  // Pop high index
            l = stack.pop();  // Pop low index

            // Partition the array and get the pivot index
            int p = partition(arr, l, h);

            // If there are elements on the left side of the pivot, push them to the stack
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }

            // If there are elements on the right side of the pivot, push them to the stack
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
