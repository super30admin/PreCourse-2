// Time Complexity : Best case O(n log n) and Worst case O(N^2)
// Space Complexity : O(N) where N is the size of the array
class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp = arr[i];
        arr[i]= arr[j];
        arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i= (l-1);

        for(int j =l;j< h;j++){
            if(arr[j] <= pivot){
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);
        return (i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //creating a stack
        int[] stack = new int[arr.length+1];

        // initialize top to -1
        int top=-1;

        // push initial values to stack low and high values
        stack[++top] = l;
        stack[++top] = h;

        // pop elements until stack is empty
        while(top >= 0){

            //pop high and low values.
             h = stack[top--];
             l = stack[top--];

             // pivot element using partition
             int p = partition(arr, l, h);

             if(p-1 > l) {
                 stack[++top] = l;
                 stack[++top]= p-1;
             }

             if(p+1 < h) {
                 stack[++top] = p+1;
                 stack[++top] = h;
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