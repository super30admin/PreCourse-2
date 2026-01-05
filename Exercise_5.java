import java.util.Stack;
import java.util.Arrays;
// Time Complexity : o(logn)
// Space Complexity :o(logn)
// Did this code successfully run on Leetcode :no
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
// //Create an empty stack and push first and last element.

// interate over stack and while iterating perform below action:
// 1. Find pivot
// 2. push left subarray from first element till pivot
// 3. push right subarray from next element of pivot till last element.



class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {
        int pivot = arr[h];
        int i = l-1;
        for(int j = l; j<h;j++){

            if(arr[j]<=pivot){
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i+1];
        arr[i+1] = arr[h];
        arr[h] = temp;
        return i+1; 
        //Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //create stack to store lower and upper bound of subarrays
       Stack<Integer> stack = new Stack();

       //push initial bound to the stack
       stack.push(l);
       stack.push(h);

       //keep popping from stack while it is not empty
       while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();
        if(l < h){
            int pivotIndex = partition(arr, l, h);
            //If there are elements on left side of the pivot , push their indices to stack
            if(pivotIndex-1>l){
                stack.push(l);
                stack.push(pivotIndex-1);
            }
            if(pivotIndex + 1 < h){
                stack.push(pivotIndex+1);
                stack.push(h);
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
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 