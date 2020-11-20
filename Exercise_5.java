// Time Complexity : O(NlogN)
// Space Complexity : O(1)

public class IterativeQuickSort { 
    
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
        int tmp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = tmp;

        return (i + 1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    {  
        int stack[] = new int[h - l + 1]; 
   
        int top = -1; 

        top += 1; 
        stack[top] = l;
        top += 1; 
        stack[top] = h; 
  
        while (top >= 0) { 
            
            h = stack[top];
            top -= 1; 
            l = stack[top];
            top -= 1; 
  
            int p = partition(arr, l, h); 
  
            if (p - 1 > l) { 
                top += 1;
                stack[top] = l; 
                top += 1;
                stack[top] = p - 1; 
            } 
  
            if (p + 1 < h) {
                top += 1; 
                stack[top] = p + 1;
                top += 1; 
                stack[top] = h; 
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