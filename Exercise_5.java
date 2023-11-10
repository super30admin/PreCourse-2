import java.util.Stack;

// Time Complexity : O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

// Your code here along with comments explaining your approach
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    {
        if (arr[i] == arr[j]) {
            return;
        }
        arr[j] = arr[i] + arr[j];
        arr[i] = arr[j] - arr[i];
        arr[j] = arr[j] - arr[i];
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int ptr = l - 1;
        for(int j = l; j < h; j++) {
            if (arr[j] <= pivot) {
                ptr++;
                swap(arr, ptr, j);
            }
        }
        swap(arr, ptr + 1, h);
        return ptr + 1;
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        Stack<Integer> st = new Stack<>();
        st.push(l);
        st.push(h);

        while (!st.isEmpty()) {
            h = st.pop();
            l = st.pop();

            int p = partition(arr, l, h);

            if (p - 1 > l) {
                st.push(l);
                st.push(p - 1);
            }
            if (p + 1 < h) {
                st.push(p + 1);
                st.push(h);
            }
        }
        //Try using Stack Data Structure to remove recursion.
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