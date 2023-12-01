import java.util.Stack;

// Time Complexity: O(n * log n)
// Space Compelxity: O(n)
class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high)
    { 
        //Compare elements and swap.
        int v = arr[low];
        int k = low;

        while(true){
            while(low < high && arr[++low] < v);

            while(high >= low && arr[high] > v)
                high--;
            if(low >= high) break;

            int temp = arr[low];
            arr[low] = arr[high];
            arr[high] = temp;
        }

        int temp = arr[k];
        arr[k] = arr[high];
        arr[high] = temp;

        return high;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high)
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();

        stack.push(low);
        stack.push(high);

        while(stack.size() != 0){
            int h = stack.pop();
            int l = stack.pop();
            int mid = partition(arr, l, h);
            if(l < mid-1){
                stack.push(l);
                stack.push(mid-1);

            }
            if(mid+1 < h){
                stack.push(mid+1);
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