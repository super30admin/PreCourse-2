// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : No only 15/21 test cases passed :: https://leetcode.com/problems/sort-an-array/description/

// Any problem you faced while coding this : Yes
/**
 * HIT TLE on leet Code
 */


// Your code here along with comments explaining your approach
/*
 * same as quick sort with reccursion
 * completed swap function
 * Done the partion Index function to get the pivot
 * And divided the arrays in two parts according to the pivot 
 * then used stack to store the high and low
 */

 /*
  * IT WOULD BE GOOD TO DISCUSS THIS PROBLEM IN CLASS
 */


class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if (arr[i] == arr[j]) {
            return;
        }
	    arr[i] = (arr[i] & arr[j]) + (arr[i] | arr[j]);
        arr[j] = arr[i] + ~arr[j] + 1;
        arr[i] = arr[i] + ~arr[j] + 1;

        // arr[i] = (arr[i] + arr[j]) - (arr[j] = arr[i]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = (l - 1);
        for(int j = l; j <= h - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);    
            }
        }

        swap(arr, i+1, h);
        return(i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        int [] stackArr = new int [h -l + 1];
        int top = -1;

        stackArr[++top] = l;
        stackArr[++top] = h;

        while(top >= 0) {
            h = stackArr[top--];
            l = stackArr[top--];

            int pi = partition(arr, l, h);

            if (pi - 1 > l) {
                stackArr[++top] = l;
                stackArr[++top] = pi - 1;
            }

            if(pi + 1 < h) {
                stackArr[++top] = pi + 1;
                stackArr[++top] = h;
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