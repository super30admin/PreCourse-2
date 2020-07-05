import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    /*
    arr[i] = arr[i] + arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] = arr[i] - arr[j];*/

    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h]; // last element as pivot
        int i = l;
        for(int j = l ; j < h; j++)
        {
            if(arr[j] < pivot)
            {
                swap(arr, i, j);
                i++;
            }
        }
        swap(arr, i, h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stk = new Stack<Integer>();
        stk.push(l);
        stk.push(h);

        while(!stk.isEmpty())
        {
            h= stk.pop();
            l= stk.pop();

            int pivotIndex = partition(arr, l, h);
            if(pivotIndex - 1 > l)
            {
                stk.push(l);
                stk.push(pivotIndex-1);
            }

            if(pivotIndex + 1 < h)
            {
                stk.push(pivotIndex+1);
                stk.push(h);
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
//Time Complexity = O(n log n), Worst = O(n^2)
//Space Complexity = O(n log n)