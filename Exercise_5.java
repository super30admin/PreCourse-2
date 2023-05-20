// Time Complexity : O(N^2)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : ran it successfully on local machine
/* Any problem you faced while coding this : Had to read about the steps of the algo and also about recursion and 
found it bit uncomfortable to calculate the time and space complexity of any algo*/

/*
-- Choose the last element of the array as the pivot. Now start traversing the array from the start.
-- As soon as we encounter element which is greater than the pivot assign it as the leftpointer.
-- Then continue traversing the array till we get an element smaller than the pivot. Now swap this smaller element with the leftpointer.
-- Now increment the leftpointer by one and again continue traversing the array and repeat this swapping process whenever we encounter an element smaller than the pivot element.
-- Once we reach the second last element swap the pivot element with the leftpointer.
-- Repeat all the above steps for elements on the left and right of the leftpointer iteratively using stack and repeat this till we further cannot partition the array.
-- To swap without making use of extra variable used exor operator
*/ 

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(i!=j){  // as when we perform exor on same values we get 0 which hampers our output
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
        int leftPointer = l;
        for(int i=l;i<h;i++){
            if(arr[i]<=arr[h]){
                swap(arr,i,leftPointer);
                leftPointer++;
            }    
        }
        swap(arr, leftPointer, h);
        return leftPointer;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int size = h-l+1;
        int[] myStack = new int[size];
        int top = -1;
        myStack[++top] = l;
        myStack[++top] = h;
        while(top>=0){
            h = myStack[top--];
            l = myStack[top--];

            int partIndex = partition(arr, l, h);

            if(partIndex-1 > l){
                myStack[++top] = l;
                myStack[++top] = partIndex - 1;
            }

            if(partIndex+1 < h){
                myStack[++top] = partIndex + 1;
                myStack[++top] = h;
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