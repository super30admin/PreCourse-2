import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        if(i !=j){
            arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] -arr[j];
        arr[i] = arr[i] -arr[j];
        }
        
       
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        // System.out.println("lh: "+ l +h);
        int partition_index = l-1;
        for(int i =l ; i<h; i++){
            if(arr[i] <= pivot){
                partition_index++;
               // System.out.println("i: "+ i+ " "+ partition_index + " ai "+ arr[i] + " arr[par] "+arr[partition_index]  );
                swap(arr, i, partition_index);
            }
        }
        
        swap(arr, partition_index + 1, h);
        return partition_index + 1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        
        Stack<Integer> functionStack = new Stack<Integer>();
        functionStack.push(l);
        functionStack.push(h);

        while(!functionStack.empty()){
            
            int high = (Integer) functionStack.pop();
            int low = (Integer) functionStack.pop();
            int pi = partition(arr, low, high);

            if(pi+1 < high){
                functionStack.push(pi+1);
                functionStack.push(high);
            }
            if(pi-1 > low){
                functionStack.push(low);
                functionStack.push(pi -1);
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 , 7,4,6,23,12,34,23,43}; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 