import java.util.Stack;

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
       int pivot = high;
       int small = low;
       for (int i = low; i <= high;i++){
           if (arr[i] <  arr[pivot]){
               swap(arr, small, i);
               small++;
           } 
           
       }
       swap(arr, small, pivot);
       return small;
    } 
    
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while(! stack.isEmpty()){
            int h0=stack.pop();
            int l0= stack.pop();
            

            int part = partition(arr, l0, h0);
            if(part -1 > l0){
                stack.push(l0);
                stack.push(part-1);
            }
            if(part+1 < h0){
                stack.push(part+1);
                stack.push(h0);
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
        Exercise_5 ob = new Exercise_5(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 