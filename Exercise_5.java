// Time Complexity : O(n log n) on average, O(n^2) in the worst case
// Space Complexity : O(log n) due to recursive stack calls
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : No

import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if (i != j) 
        { 
            arr[i] = arr[i] +arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
       int pivot = arr[l];
       int i = l;
       int j = h;
       while(i<j)
       {
           while(i <h && arr[i]<=pivot)
           {
               i++;
           }
           while(j>= l+1 && arr[j]>pivot)
           {
               j--;
           }
           if(i<j)
           {
             swap(arr,i,j);
           }
       }
       swap(arr,j,l);
       return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> st  = new Stack<>();
        int[] p = {l,h};
        st.push(p);
        while(!st.isEmpty())
        {
            int[] pdup = st.pop();
            int ldup = pdup[0];
            int hdup = pdup[1];
            if(ldup < hdup)
            {
                int par =  partition(arr,ldup,hdup);
                int[] add1 = {ldup,par-1};
                int[] add2 = {par+1,hdup};
                st.push(add1);
                st.push(add2);
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