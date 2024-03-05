//Time Complexity:
// Worst case: O(n^2)
// Best and Average case: O(nlogn)
//Space Complexity:
// Worst case: O(n)
// Best and Average Case: O(logn)

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if (i != j) {
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int left = l;
        int right = h;
        
        while(left < right)
        {
            while(arr[left] <= pivot && left < right)
            {
                left = left+1;
            }
            while(arr[right] >= pivot && left < right)
            {
                right = right-1;
            }
            if(arr[left] > arr[right])
                swap(arr, left, right);
        }
        swap(arr, left, h);
        return left;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        if(l >= h)
        {
            return; // single element
        }
        //Try using Stack Data Structure to remove recursion.
        
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while(!stack.empty())
        {
            h = stack.pop();
            l = stack.pop();

            int left = partition(arr, l, h);

            if(left - 1 > l)
            {
                stack.push(l);
                stack.push(left-1);
            }
            if(left + 1 < h)
            {
                stack.push(left+1);
                stack.push(h);
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