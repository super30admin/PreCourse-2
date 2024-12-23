//Time complexity : O(nlogn)
//space complexity : O(1)

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
 	int pivot = arr[l];
        int i = l+1;
        int j = l+1;
        
        while (j <= h) {
            if (arr[j] < pivot) {
                swap(arr, i, j);
                i++;
            }
            j++;
        }
        swap(arr, l, i-1);
        return i-1;    
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        int[] stack = new int[l - l + 1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;

        while (top >= 0) {
            h = stack[top--];
            l = stack[top--];

            int pivot = partition(arr, l, h);

            if (pivot - 1 > l) {
                stack[++top] = l;
                stack[++top] = pivot - 1;
            }

            if (pivot + 1 < h) {
                stack[++top] = pivot + 1;
                stack[++top] = h;
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
