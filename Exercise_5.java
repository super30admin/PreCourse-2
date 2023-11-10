// Time Complexity : O(n*log(n)), worst case: O(n*n)
// Space Complexity :using only extra variables O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : unable to get proper output, have doubt in stack implementation
import java.util.*;


class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
         arr[i] = arr[i] + arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        //Compare elements and swap.
         int pivot = arr[high];
        int l = low-1;

        for(int i=low;i<high;i++){
            if(arr[i]<pivot){
                l = l+1;
                swap(arr,i,l);
            }
        }
        swap(arr,l+1,high);
        return l+1; 
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        
        Stack<Integer> st = new Stack<>();
        st.push(l);
        st.push(h);

        while(!st.isEmpty()){
            h = st.pop();
            l = st.pop();
            int pivot = partition(arr,l,h);
            if(pivot -1 >l){
                st.push(l);
                st.push(pivot -1);
            }
             if(pivot +1 <h){
                st.push(pivot +1);
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