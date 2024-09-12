// Time Complexity : Average Case : O(Nlog(N)), Worst Case: O(N^2)->When array is sorted in ascending or descending order
// Space Complexity : O(1) constant space because quick sort does sorting in place
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this :  No


/**** Steps ****/
/*
  For Iterative Quick Sort
  1) Create A Stack for storing low and high indexes. I created a class "LowHighPair" for storing low high indexes in a single object for each iteration
  2) Pop the low, high indexes and pass them into the partition function as done earlier for recursive code
  3) For partitioning the array into left and right, I followed the below steps
       a) For left partition, push low and high indexes in stack only when lower index is less than the partition index - 1. This means if there will be more than one element then it will be pushed to the stack.
       b) For right partition, push low and high indexes in stack only when higher index is greater than the partition index + 1. This means if there will be more than one element then it will be pushed to the stack.
   5) Repeat Steps 2 and 3 until stack is empty
   
   In case of iterative quick sort, here right partition will be sorted first then left because Stack uses concept of "LIFO".

   For Swaping two variables without third variable, I used addition and subtraction methodology.
*/


import java.util.*;
class IterativeQuickSort { 

    class LowHighPair{
         
        int low;
        int high;

        LowHighPair(int low, int high){
          this.low = low;
          this.high = high;
        }

    }

    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable
       
    //Because if i and j indexes are same then, they cannot be swaped with the below approach because subtracting the values of same indexes will retuen 0, as well as no need to swap them thats why return from here.

       if(arr[i] == arr[j]){
           return;
       }

        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
        
    } 
    
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int partIdx = l;
        int pivotIdx = h;

        for(int i=l;i<=h-1;i++){
            if(arr[i]<arr[pivotIdx]){
                swap(arr,i,partIdx);
                partIdx++;
            }
        }

        swap(arr,partIdx,pivotIdx);
        
        return partIdx;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        
        //LowHighPair Class so that low and high indexes can be saved in a single object in a Stack for each iteration. If I have not created the class then I have to push and pop twice for storing low and high indexes.
        Stack<LowHighPair> stack =new Stack<>();

        //pushed initial l and h
        stack.push(new LowHighPair(l, h));

        while(!stack.isEmpty()){
            //popped the l and h values;
            LowHighPair lHP = stack.pop();

            //Finding the partitioning index
            int partIdx = partition(arr, lHP.low, lHP.high);

            //Pushing in stack if more than 1 element-> It will work for left partitioning
            if(lHP.low<partIdx-1)
                stack.push(new LowHighPair(lHP.low, partIdx-1));

            //Pushing in stack if more than 1 element -> It will work for right partitioning    
            if(partIdx+1<lHP.high)   
            stack.push(new LowHighPair(partIdx+1, lHP.high));           

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