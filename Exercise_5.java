//Time complexity : o(nlogn)
//Space complexity : o(n) for stack
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
        int pIndex = l;
        int pivot = arr[h];
        for(int i=l;i<=h-1;i++){
            if(arr[i] <= pivot){
                swap(arr,i, pIndex);
                pIndex++;
            }
        }
        swap(arr, pIndex,h);
        return pIndex;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while (!stack.isEmpty()) {
            int high = stack.pop();
            int low = stack.pop();
            int pIndex = partition(arr, low, high);
            if(pIndex - 1 > low){
                stack.push(low);
                stack.push(pIndex - 1);
            }
            if(pIndex + 1 < high){
                stack.push(pIndex + 1);
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