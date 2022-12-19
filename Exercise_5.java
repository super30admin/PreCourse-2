// Time Complexity : O(NlogN)
// Space Complexity : O(logN)
// Any problem you faced while coding this : No
import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if (arr[i] != arr[j]) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap
        int pivot = arr[h];
        int i = l, j = h;
        while (i < j) {

            // increment i till we find a value greater than pivot element
            while (arr[i] <= pivot && i < j) {
                i++;
            }

            // decrement j till we find value smaller than pivot element
            while (arr[j] >= pivot && i < j) {
                j--;
            }

            // swap element at index i and j
            swap(arr, i, j);
        }

        // swap element at i and high(pivot) to get the partition index
        swap(arr, i, h);

        return i;
        
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        // push l and h to the stack to find the initila partition index
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            int high = stack.pop();
            int low = stack.pop();
            int j = partition(arr, low, high);
            if (j - 1 > low) {
                stack.push(low);
                stack.push(j - 1);

            }
            if (j + 1 < high) {
                stack.push(j + 1);
                stack.push(high);
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