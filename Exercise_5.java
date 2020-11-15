// Time Complexity :O(n^2)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :

import java.util.Stack;

public class IterativeQuickSort {
    void swap(int arr[], int i, int j) {
        //Try swapping without extra variable
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }

    /* This function is same in both iterative and
       recursive*/
    int partition(int arr[], int l, int h)
    {
        //Compare elements and swap.
        int pivot=arr[h];
        int index=l-1;
        for(int i=l;i<h;i++){
            if(arr[i]<pivot){
                index++;
                if(index!=i)
                swap(arr,index,i);
            }
        }
        if(index+1!=h)
        swap(arr, index+1,h );
        return index+1;
    }

    // Sorts arr[l..h] using iterative QuickSort
    void QuickSort(int arr[], int l, int h)
    {
        //Try using Stack Data Structure to remove recursion.

        Stack<int[]> st = new Stack();
        int partionIndex;

        st.push(new int[]{l,h});

        while(!st.empty()){
            l= st.peek()[0];
            h=st.pop()[1];

            partionIndex=partition(arr, l,h);
            if(l<partionIndex-1)
                st.push(new int[]{l,partionIndex-1});
            if(partionIndex+1<h)
                st.push(new int[]{partionIndex+1,h});

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