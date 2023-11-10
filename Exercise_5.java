// Time Complexity : O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : no

// Your code here along with comments explaining your approach

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int p = arr[h];
       int k = l-1; 
       for (int i=l; i<h; i++)
       {
           if (arr[i] <= p)
           { k++;
            swap(arr,k,i);            
           }
       }
       swap(arr,k+1,h); 
       return k+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] st = new int[1 + h - l];
        int top = -1;
 
        st[0] = l;
        st[1] = h;
        top=1;
 
        
        while (top >= 0) {
            h = st[top--];
            l = st[top--];
 
            int pivot = partition(arr, l, h);
 
            if (pivot - 1 > l) {
                st[++top] = l;
                st[++top] = pivot - 1;
            }
 
            if (pivot + 1 < h) {
                st[++top] = pivot + 1;
                st[++top] = h;
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
