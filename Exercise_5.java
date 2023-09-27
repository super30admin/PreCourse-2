/* TC:O(nlogn)   SC:O(1) */
import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    {   if(i!=j){
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];}
      
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        int ptr = l;
        for(int i = l; i < h; i++){
            if(arr[i] <= pivot){
                swap(arr,i,ptr);
                ptr++;
            }
        }
        swap(arr,ptr,h);
        return ptr;//Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
       Stack<Integer> stk = new Stack<Integer>();
       stk.push(-1);
       stk.push(l);
       stk.push(h);
       while(stk.peek() != -1){
        h = stk.pop();
        l = stk.pop();
        int pivot = partition(arr,l,h);
        if(pivot - 1 > l){
            stk.push(l);
            stk.push(pivot-1);
        }
        if(pivot+1 < h){
            stk.push(pivot+1);
            stk.push(h);
        }

       } //Try using Stack Data Structure to remove recursion.
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