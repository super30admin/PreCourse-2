//Complexity
//Time: O(n log n)
//Space: 
//Approach: Use the same partition as example 2, pushed values of s in stack until s!= high or stack empty.

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i] = (arr[i] + arr[j]) - (arr[j] = arr[i]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int p = arr[h];
        int s = h;

        for(int i = h-1; i>=0; i--) {
            if(arr[i] >= p) {
                s--;
                swap(arr, i, s);
            }
        }
        swap(arr, h, s);
        return s;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> st = new Stack<>();
        st.add(partition(arr, l, h));
        while(!st.empty()) {
            int s = st.pop();
            if(s==h){
                return;
            } else {
                st.add(partition(arr, s+1, h));
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