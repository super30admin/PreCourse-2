// Time Complexity : O(nlog(n))
// Space Complexity : O(1) // No recursion calls.
// Did this code successfully run on Leetcode : NO
// Any problem you faced while coding this : Unable to solve the iterative part of the function.
//Need help with that . I am getting stack overflow error.


// Your code here along with comments explaining your approach
//Quick sort is basically finding out the pivot element using the partition function,
// so that at each pass the pivot element is fixed.

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
    // eg = (x, y) = (10, 5 )
    // first pass => x= x+y = 15
    // second pass => y = x-y = 15-5 = 10 // previous value of x
    // third pass => x = x-y = 15-10 = 5 // previous value of y. 
    // strike #1 -> x = x+y; y = x-y; x = x-y;
    // condition to check whether both the nos are the same.
    if(arr[i]== arr[j]) {
        return;
    }        
    arr[i]  = arr[i] + arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        // Same as normal quick sort.
        int pivot = arr[h];
        int j = l;
        while(l<h)  {// compare till second last element. why do i need to compare the last element, lol.
            if(arr[l]<= pivot) {
                swap(arr, l, j);
                j++;
            }            
            l++;
        }
        swap(arr, j, h);
        return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(0);
        stack.push(h);
        while(!stack.empty()) {
            int end = stack.pop();// 7
            int start = stack.pop(); // 0
            System.out.println("start is "+ start);
            System.out.println("end is "+ end);
            if (start< end) {

                // 7<=0 false.
                int pivot = partition(arr, l, h);

                System.out.println("pivot is "+ pivot);
                if (pivot + 1 < h) {
                    stack.push(pivot+1);
                    stack.push(h);            
                }
                if (l < pivot - 1) {
                    stack.push(l);
                    stack.push(pivot-1);
                }

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
        //int[] arr = { 10, 7, 8, 9, 1, 5 };
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 