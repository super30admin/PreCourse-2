import java.util.Stack;
/*
Time Complexity : O(nlogn) since everything is done after traversing the entire arraylist.
Space Complexity : O(n) since we create memory when array is generated

Did this code successfully run on Leetcode :
Finished in 90 ms
1 2 2 3 3 3 4 5 

Any problem you faced while coding this :
Not implementing swap without temp variable.
Its giving me 0s instead of 3s ie repetitive 3 is getting 0
Finished in 86 ms
1 2 2 3 0 0 4 5 

Your code here along with comments explaining your approach :
Straight forward approach.
*/
class IterativeQuickSort { 
    void swap(int[] arr, int i, int j) 
    { 
	    int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        // arr[i] = arr[i]+arr[j]; // 7 + 9 = 16
        // arr[j] = arr[i]-arr[j]; // 16 - 9 = 7
        // arr[i] = arr[i]-arr[j]; // 16 - 7 = 9
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int[] arr, int low, int high) 
    { 
        int pivot = arr[high];
        int i = (low - 1) ;
        for (int j = low; j < high; j++){
            if (arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, high);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int[] arr, int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            int end = stack.pop();
            int start = stack.pop();

            if (end - start < 2) continue;
            
            int p = partition(arr,start,end);
            if (p - 1 > l) {
                stack.push(start);
                stack.push(p-1);
            }
            if (p + 1 < h) {
                stack.push(p+1);
                stack.push(end);
            }
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int[] arr, int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int[] arr = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 