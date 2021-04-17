// Time Complexity : O(nlog(n))
// Space Complexity : O(nlogn)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
import java.io.*;
import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(i!=j){
            arr[i] = arr[j] - arr[i];
            arr[j] = arr[j] - arr[i];
            arr[i] = arr[i] + arr[j];
        }
        
    } 
  
    /* This function is same in both iterative and 
       recursive*/
       int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = (l - 1);
    
        for(int j = l; j <= h - 1; j++)
        {
            if (arr[j] < pivot)
            {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, h);
        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        // Method 1: Using Stack
        Stack stack_store = new Stack();
        stack_store.push(l);
        stack_store.push(h);
        while(!stack_store.empty()){
            h=(int) stack_store.pop();
            l=(int) stack_store.pop();
            int p = partition(arr, l, h);
            if (p - 1 > l) {
                stack_store.push(l);
                stack_store.push((p - 1));
            }
            if (p + 1 < h) {
                stack_store.push((p + 1));
                stack_store.push(h);
            }            
        }

        /*
                //  // Method 2: Below method is in array way

                int[] stack = new int[h - l + 1];
                int top = -1;
                stack[++top] = l;
                stack[++top] = h;
                while (top >= 0) {
                    h = stack[top--];
                    l = stack[top--];

                    int p = partition(arr, l, h);
                    if (p - 1 > l) {
                        stack[++top] = l;
                        stack[++top] = p - 1;
                    }
                    if (p + 1 < h) {
                        stack[++top] = p + 1;
                        stack[++top] = h;
                    }
                }


        */

        /*
                //  // Method 3: This method is recursive approach 

                if (low < high)
                {
                    int pi = partition(arr, low, high);
                    sort(arr, low, pi - 1);
                    sort(arr, pi + 1, high);
                }

        */
    
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