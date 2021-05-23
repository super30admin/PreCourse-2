import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int index = l-1;

        for(int j=l; j<=h-1; j++){
            if(arr[j]<pivot){
                swap(arr, index+1, j);
                index++;
            }
        }
        swap(arr, index+1, h);
        return index+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);

        while(!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();

            int pivot = partition(arr, l, h);
            if(pivot - 1 > l){
                stack.push(l);
                stack.push(pivot-1);
            }
            if(pivot + 1 < h){
                stack.push(pivot + 1);
                stack.push(h);
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