import java.util.ArrayDeque;
import java.util.Deque;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	    //Try swapping without extra variable 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    //with this method my code doesn't work
    //not sure why?
   /*  public void swap2(int arr[], int i, int j) 
    { 
	    //Try swapping without extra variable 
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j]; 

    } */
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[l];
        int j = l+1;
        for(int i=l+1; i<=h; i++){
            if(arr[i] < pivot){
                 swap(arr, i, j);
                 j++;
            }
        }
        swap(arr, l, j-1);
        return j-1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(l);
        stack.push(h);
        //Try using Stack Data Structure to remove recursion.
        while (!stack.isEmpty()){
            h = stack.pop();
            l = stack.pop();

            int p = partition(arr, l, h);

            if(p > l){
                stack.push(l);
                stack.push(p-1);
            }
            if(p < h){
                stack.push(p+1);
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
        //ob.swap2(arr, 2, 3);
        //ob.printArr(arr, arr.length);
    } 
} 