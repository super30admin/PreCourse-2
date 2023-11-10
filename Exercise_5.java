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
    int partition(int arr[], int low, int high) 
    { 
         // edge case : if length<3
         if ((high-low) <= 1) { 
            if (arr[high] < arr[low]) swap(arr, low, high);
            return low;
        } 

        int i = low;
        int j = high-1;
        int pivot = arr[high]; // last elment as pivot
        while(i<j) {
            while (i<j && arr[i]<= pivot) i++; // stops when arr[i]>pivot
            while (i<j && arr[j]> pivot) j--; // stops when arr[i]<pivot
            
            if (i<j){
                swap(arr, i, j);
            }
        }
        // swap 
        swap(arr, i, high);

        return i; 
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {
        Stack<Integer> visited = new Stack<>();
        
        visited.push(h);
        visited.push(l);

        while(!visited.isEmpty()){

            int low = visited.pop();
            int high = visited.pop();

            int idx = partition(arr, low, high);

            if (idx>low) {
                // there are elements on left to pivot
                visited.push(idx-1);
                visited.push(low); 
            }
            
            if (high>idx ) {
                // there are elements in right side to pivot
                visited.push(high);
                visited.push(idx+1);
            }

           
        }

    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        System.out.println("");
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        // int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        //  int arr[] = {10, 7, 8, 9, 1, 5};
        int arr[] = {10, 1, 5};
        // int arr[] = {10, 7};
        // int arr[] = {5,10};
        ob.printArr(arr, arr.length); 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 