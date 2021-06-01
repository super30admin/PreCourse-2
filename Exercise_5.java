// Time Complexity : O(n^2)
// Space Complexity : O(log n)

public class IterativeQuickSort {
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
        int high = arr[h];
        int low = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= high) {
                low++;
                swap(arr, low, j);
            }
        }
        swap(arr, low + 1, h);
        return (low + 1);

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //make a stack

        int mystack[] = new int[h - l + 1];
        // create a top for stack
        int top = -1;

        // intiialize the stack values.
        mystack[++top] = l;
        mystack[++top] = h;
        //pop while stack top >=0
        while (top >= 0) {
            // pop h and l
            h = mystack[top--];
            l = mystack[top--];
            // put pivot in correct position in stack
            int pivot = partition(arr, l, h);
            // push left side elements of pivot to stack
            if (pivot - 1 > l) {
                mystack[++top] = l;
                mystack[++top] = pivot - 1;
            }
            //push right side elements of pivot to stack
            if (pivot + 1 < h) {
                mystack[++top] = pivot + 1;
                mystack[++top] = h;
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