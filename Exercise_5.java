//TC - O(nlogn), SC - O(log n)
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
        //Compare elements and swap.
        int i = l-1;
        int pivot = arr[h];
        for(int j=l; j<h; j++){
            if(arr[j]<pivot){
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
        if(l>=h)
            return;

        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        //Try using Stack Data Structure to remove recursion.

        while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();
            int idx = partition(arr, l, h);

            if(idx+1<h){
                stack.push(idx+1);
                stack.push(h);
            }
            if(idx-1>l){
                stack.push(l);
                stack.push(idx-1);
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