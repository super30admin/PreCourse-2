import java.util.Stack;
// Time Complexity : O(nlogn)
// Space Complexity : O(log n) instead of recursive stack space we are using the explicit stack to maintain the range of subarrays that needs to be processed.
// Did this code successfully run on Leetcode : n/a
// Any problem you faced while coding this : yes, few problems, regarding the algorithm but I found the detailed explanation in youtube, so I was able to code it out at last.


// Your code here along with comments explaining your approach

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
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
        int m = l + (h-l)/2;
        int pivot = arr[m];

        swap(arr, h, m);
        int i = l;
        int j = h-1;
        while(i<=j)
        {
            while(i<=j && pivot>arr[i])
                i++;
            while(j>=i && pivot<arr[j])
                j--;
            
            if(i<j)
                swap(arr, i, j);
                
        }
        swap(arr, h, i);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
       Stack<int[]> stk = new Stack<>();
       stk.push(new int[]{l, h});

       while(!stk.isEmpty())
       {
            int[] bounds = stk.pop();
            int low = bounds[0];
            int high = bounds[1];

            if(low<high)//i didn't put equal because what if there is only one element, which means we don't need to sort
            {
                int p = partition(arr, low, high);
                stk.push(new int[]{p+1, high});
                stk.push(new int[]{low, p-1});
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