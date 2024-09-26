import java.util.*;

class Exercise_5 { 
    void swap(int arr[],int i,int j){
        //Your code here   
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    int partition(int arr[], int low, int high) 
    { 
   	//Write code here for Partition and Swap 
       int pivot = arr[high];
       int pivot_index = low;
       for(int i=low;i<high;i++){
           if(arr[i]<=pivot){
               swap(arr,i,pivot_index);
               pivot_index++;
           }
       } 
      swap(arr,pivot_index,high);
      return pivot_index;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()){
            int high = stack.pop();
            int low = stack.pop();
            int part_index = partition(arr,low,high);
            if(part_index-low>1){ //more than 1 element keep pushing high,low into stack
              stack.push(low);
              stack.push(part_index-1);
            }
            if(high-part_index > 1){
                stack.push(part_index+1);
                stack.push(high);
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