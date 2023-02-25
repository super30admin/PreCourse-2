//Time Complexity - O(n log n) 
//Space Complexity - O(log n)
import java.util.Stack;

class Exercise_5 { 
    void swap(int arr[], int i, int j) 
    { 
        // Swapping elements without extra variable
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    int partition(int arr[], int l, int h) 
    { 
        // Choosing the first element as pivot
        int pivot = arr[l];
        int i = l - 1;
        
        for (int j = l; j < h; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, h);
        return i + 1;
    } 
  
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(l);
        stack.push(h);
        
        while (!stack.isEmpty()) {
            h = stack.pop();
            l = stack.pop();
            
            int p = partition(arr, l, h);
            
            if (p - 1 > l) {
                stack.push(l);
                stack.push(p - 1);
            }
            
            if (p + 1 < h) {
                stack.push(p + 1);
                stack.push(h);
            }
        }
    } 
  
    void printArr(int arr[], int n) 
    { 
        for (int i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    public static void main(String args[]) 
    { 
       Exercise_5 ob = new Exercise_5(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
}
