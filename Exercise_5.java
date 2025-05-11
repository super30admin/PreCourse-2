import java.util.Stack;
class IterativeQuickSort { 
    
    // Time Complexity : O(nlogn) -> most of the cases (O(n^2) in worst cases like wrong pivot chosen)
    // Space Complexity : O(log n) -> recursive calls stack (O(n) if worst pivot chosen)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : took time to understand it and brush up again properly
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
	// need to apply this logic otherwise it can lead to zero
	if (i != j) {
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int idx = l-1;
        int pivot = arr[h];
        for(int j = l;j<h;j++){
            if(arr[j]<=pivot){
                idx++;
                swap(arr, j, idx);
            }
        }
        idx++;
        swap(arr, h, idx);
        return idx;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       Stack<Integer> stck = new Stack<>();
       //initial push
       stck.push(l);
       stck.push(h);
       while(!stck.isEmpty()){
           //popping stack high and low
           h = stck.pop();
           l = stck.pop();
           int pivotIdx = partition(arr, l, h);
           //pushing to stack if anything remaining to partition in left side
           if(pivotIdx-1 > l){
               stck.push(l);
               stck.push(pivotIdx-1);
           }
           //pushing to stack if anything remaining to partition in right side
           if(pivotIdx+1 < h){
               stck.push(pivotIdx+1);
               stck.push(h);
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
