import java.util.Stack;



// Time Complexity : Best, Average case : O(N * Log N) -- Worse case : O(N ^ 2 )
// Space Complexity : O(N) for creating a Stack

// Did this code successfully run on Leetcode : NA
// Any problem you faced while coding this : Yes

/*
For swapping 2 variables, I was directly using the logic of addition-subtraction and getting 0 at some places in result of sorted array.
Then I tested that swapping is called for same index or what! and that problem resolve and got the correct sroted array
*/


// Your code here along with comments explaining your approach

/* Created one Stack using inBuilt Util library. Pushed the values of l and h. 
Using while loop, until stack not become empty 
--> poped  top most 2 values, first one will be upperBound and second one will be lowerBound
--> Called the partition method, for calculating index of pivot element in array. 
--> According to values of pivot we will push the new values of lowerBound and upperBound in the Stack.


*/

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(i != j){
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];    
        }
        //int a = arr[i]; arr[i] = arr[j]; arr[j] = a;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int c = l - 1;

        for(int i = l; i < h; i++){
            if(arr[i] <= pivot){
                c++;
                swap(arr, c, i);
            }
        }
        swap(arr, c+1, h);
        return c+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       
        Stack<Integer> s = new Stack<>();

        s.push(l); 
        s.push(h);

        while(!s.isEmpty()){
            h = s.pop(); l = s.pop();

            int pivot = partition(arr, l, h);

            if(l < pivot - 1){
                s.push(l); s.push(pivot - 1);
            }
            if(h > pivot + 1){
                s.push(pivot + 1); s.push(h);
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