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
        int pivot = arr[h]; // Pivot element is the last element
        int i = (l - 1); // Pointer for the smaller element
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= pivot) {
                i++; // Increment the index of smaller element
                swap(arr, i, j); // Swap arr[i] and arr[j]
            }
        }
        swap(arr, i + 1, h); // Swap the pivot element to its correct position
        return (i + 1); // Return the partition index
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
       // Create a stack to simulate recursion
       Stack<Integer> stack = new Stack<>();
        
       // Push the initial values of low and high to the stack
       stack.push(l);
       stack.push(h);

       // While stack is not empty, continue sorting
       while (!stack.isEmpty()) {
           h = stack.pop(); // Pop the high index
           l = stack.pop(); // Pop the low index

           // Partition the array and get the pivot index
           int p = partition(arr, l, h);

           // If there are elements on the left of pivot, push them to stack
           if (p - 1 > l) {
               stack.push(l);
               stack.push(p - 1);
           }

           // If there are elements on the right of pivot, push them to stack
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

