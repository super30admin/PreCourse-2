// Time Complexity : O(NLogN) average case, O(N^2) worst case
// Space Complexity : O(N) in worst case(array is sorted in increasing order), O(log N) ideal case(pivot is the median), used by stack
// Did this code successfully run on Leetcode : Giving TLE at https://leetcode.com/problems/sort-an-array/description/
// Any problem you faced while coding this : 
// Understanding the pivot algorithm is tricky. Used this resource to understand https://www.youtube.com/watch?v=uXBnyYuwPe8 


// Your code here along with comments explaining your approach

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        // Swap using XOR, no extra variable
        if (i == j)
            return;
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }

    int partition(int arr[], int low, int high) {
        // i is the position before which all elements less than pivot are present
        // j is a pointer that traverses the array to find an element such that it is
        // less than the pivot
        // If it is, then we swap it with i and increment it

        int i = low;
        int j = low;
        for (; j < high; j++) {
            if (arr[j] < arr[high]) {
                swap(arr, i, j);
                i++;
            }
        }
        swap(arr, i, high);
        return i;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h) {
        // Try using Stack Data Structure to remove recursion.
        if(l==h)    return;
        Stack<int[]> st = new Stack<>();
        st.push(new int[] {l,h});
        int[] currCall = new int[2];

        while(!st.isEmpty()){
            currCall=st.pop();
            int currL=currCall[0], currH=currCall[1];
            if(currL==currH)    continue;
            int partInd=partition(arr, currL, currH);
            if(partInd>currL)   st.push(new int[] {currL, partInd-1});
            if(partInd<currH)   st.push(new int[] {partInd+1, currH});
        }
    }

    // A utility function to print contents of arr
    void printArr(int arr[], int n) {
        int i;
        for (i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
    }

    // Driver code to test above
    public static void main(String args[]) {
        IterativeQuickSort ob = new IterativeQuickSort();
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        ob.QuickSort(arr, 0, arr.length - 1);
        ob.printArr(arr, arr.length);
    }
}