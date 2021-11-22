
//TC: O(n^2) as last element as pivot.
//SC:O(N)
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h]; 
        int index = (l - 1); 
      
        for(int i = l; i <= h - 1; i++)
        {
            if (arr[i] < pivot) 
            {
                index++; 
                swap(arr, index, i);
            }
        }
        swap(arr, h,index + 1);
        return (index + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        int[] stack_array = new int[h - l + 1];
 
        int top = -1;
        
        stack_array[++top] = l;
        stack_array[++top] = h;
 
        while (top >= 0) {
            h = stack_array[top--];
            l = stack_array[top--];
 
            int pivot = partition(arr, l, h);
 
            if (pivot - 1 > l) {
                stack_array[++top] = l;
                stack_array[++top] = pivot - 1;
            }
 
            if (pivot + 1 < h) {
                stack_array[++top] = pivot + 1;
                stack_array[++top] = h;
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