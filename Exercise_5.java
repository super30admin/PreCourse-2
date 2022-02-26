/*Time Complexity : 
Best: O(nlog(n))
Worst: O(n^2)
Space Complexity : O(n)
Did this code successfully run on Leetcode : yes
Any problem you faced while coding this : swapping without extra variable was giving an incorrect output
*/
import java.util.Stack;
class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int x = arr[h];
        int i = (l - 1);

        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= x) {
                i++;
                // swap arr[i] and arr[j]
                swap(arr, i, j);
            }
        }
        // swap arr[i+1] and arr[h]
        swap(arr, i + 1, h);
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        // initial values in the stack as low and high
        Stack<Integer> st = new Stack<>();
        st.push(l);
        st.push(h);

        // popping out the values out of stack till we have empty stack
        while(!st.isEmpty()){
            h = st.pop();
            l = st.pop();
            // getting pivot
            int pivot = partition(arr, l, h);

            // if there are elements on left side of the pivot, pushing them  to stack
            if(pivot-1 > l){
                st.push(l);
                st.push(pivot-1);
            }
            // if right side elements are there pushing them to stack
            if(pivot+1 < h){
                st.push(pivot+1);
                st.push(h);
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