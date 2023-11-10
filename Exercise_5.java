// Iterative QuickSort
// Time Complexity : O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : Little bit

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    	arr[i] = arr[i] + arr[j];
    	arr[j] = arr[i] - arr[j];
    	arr[i] = arr[i] - arr[j];
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
    	
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
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
    	int[] stk = new int[1 + h - l];
        int top = -1;
        
        stk[0] = l;
        stk[1] = h;
        top=1;
        
        while (top >= 0) {
            h = stk[top--];
            l = stk[top--];
 
            int pivot = partition(arr, l, h);
 
            if (pivot - 1 > l) {
            	stk[++top] = l;
            	stk[++top] = pivot - 1;
            }
 
            if (pivot + 1 < h) {
            	stk[++top] = pivot + 1;
            	stk[++top] = h;
            }
        }
        
        //Try using Stack Data Structure to remove recursion.
    	
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