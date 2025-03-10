import java.util.Stack;

class IterativeQuickSort {
    //Time Complexity: O(nlog(n))
//Space Complexity: O(n)

// Did this code successfully run on Leetcode :Yes
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
         arr[i]=arr[i]+arr[j];
         arr[j]=arr[i] - arr[j];
         arr[i]=arr[i]-arr[j];

    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.m
        int left=l;
        int right=h;
        int pivot=arr[l];
        while(left<right)
        {
            while(arr[left]<=pivot && left<=h-1)
                left++;
            while(arr[right]>pivot && right>=l+1)
                right--;

            if(left<right)
            {
                swap(arr,left,right);
            }
        }
        swap(arr,l,right);
        return right;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while (!stack.isEmpty()) {
            int high = stack.pop();
            int low = stack.pop();

            if (low < high) {
                int p = partition(arr, low, high);

                // Push right subarray
                stack.push(p + 1);
                stack.push(high);

                // Push left subarray
                stack.push(low);
                stack.push(p - 1);
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