/*
 Time complexity: O(NlogN) average and best case and O(N2) in worst case. It will depend on the selection of pivot.
 Scpace complexity: worst case O(N) and average case (logN) since we will roughly partition the array space into two parts
                    where N is size of Array
 Did this code successfully run on Leetcode : 
 Any problem you faced while coding this : My code was going into infinite loop because the stack size kept on increasing.
                     Then i added condition to check whether two elements are present in array space before inserting in stack
                     which solved the problem.
*/

import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int i = l, j = h;
        
        //after the loop breaks we have array arranged in such a way that all elements on left side is less than pivot 
        //and all elements which is greater than pivot is on right side.
        while(i < j){
            
            //till we find an element which is greater that pivot
            while(i < j && i <= h && arr[i] <= pivot){
                i++;
            }
            
            //till we find an element which is lesser than pivot
            while(i < j && j>=0 && arr[j] >= pivot){
                j--;
            }

            //swap to make larger element go to left side and smaller element go to right side
            if(i < j){
                swap(arr, i, j);
                
            }
        }
        //we found correct position of pivot element
        if(i <= h){
            swap(arr, h, i);
        }
        return i; // return position if the element which is at its correct position
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if(l < h){
            Stack<Pair> stack = new Stack<>();
            stack.add(new Pair(l, h));

            while(!stack.isEmpty()){
                Pair temp = stack.pop();
                int pivot = partition(arr, temp.low, temp.high);
                if(temp.low < pivot - 1){
                    stack.push(new Pair(temp.low, pivot - 1));
                }
                if(pivot + 1 < temp.high){
                    stack.push(new Pair(pivot + 1, temp.high));
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
        
        System.out.println();
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.printArr(arr, arr.length); 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 

    class Pair{
        int low;
        int high;
        public Pair(int low, int high){
            this.low = low;
            this.high = high;
        }
    }
} 