// Time Complexity : O(N log N)
// Space Complexity : Worst Case is O(N) for the stack - for each pivot element( which is always the last element), we push two indices.
// Average case O(log N). 
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this : -

import java.util.Stack;

class IterativeQuickSort { 

    Stack<Integer> s= new Stack<Integer>();
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        s.push(arr[i]);
        arr[i]= arr[j];
        arr[j]= s.pop();
        /*int temp = arr[i];
        arr[i]= arr[j];
        arr[j]= temp;*/
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i= l-1; 
        for(int j=l; j < h; j++)
        {
            if(arr[j] <= pivot )
            {
                i++;
               swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);
        return i+1;


    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        
        s.push(l);
        s.push(h);

        while(!s.isEmpty())
        {
            h = (int)s.pop();
            l = (int)s.pop();

            //call partition
            if(l<h)
            {
            int pivot = partition(arr, l, h);
            s.push(l);
            s.push(pivot-1);
            s.push(pivot+1);
            s.push(h);
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