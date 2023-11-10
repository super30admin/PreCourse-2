// Time Complexity : O(nlog n)
// Space Complexity : O(log n)

import java.util.*;
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
       int i = l, j = h, pivot = arr[l];  // setting the left most element as the pivot
        while(i<j){
            while(arr[i] <= pivot && i<h){ // increment i if the element is less than or equal to pivot
                i++;
            }

            while(arr[j] > pivot && j>l){ // decrement j if the element is greater than pivot
                j--; 
            }

            if(i<j){             // swap elements at position i and j if i<j
                swap(arr, i, j);
            }
        }

        swap(arr, l, j); // if i>=j, swap element at j with pivot
        return j; // j is the position where the pivot is fixed
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> itrQs = new Stack<>();             // itrQs stack is used to push the lower and upper bounds for each sub array
        itrQs.push(l);      // firstly the lower bound is pushed on to the stack
        itrQs.push(h);      // secondly the upper bound is pushed on to the stack

        while(!itrQs.isEmpty()){
             int up = itrQs.pop();       // pop the upper bound from the stack
             int low = itrQs.pop();      // pop the lower bound from the stack

            int pIndex = partition(arr, low, up);   // partition the array based on the pivot

            if(pIndex - 1 > low){      // push the upper and lower bounds for the left sub array
                itrQs.push(low);
                itrQs.push(pIndex-1);
            }
 
            if(pIndex+1 < up){          // push the upper and lower bounds for the right sub array
                itrQs.push(pIndex+1);
                itrQs.push(up);
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