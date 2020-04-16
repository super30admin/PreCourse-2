//time complexity o(nlog(n))
import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        //Try swapping without extra variable 
        int temp =arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
       //tried the below approach for swapping but getting a different solution i.e. 1 2 2 0 0 3 4 5
       // arr[i]=arr[i]+arr[j]; 
       // arr[j]=arr[i]-arr[j];
       // arr[i]=arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot = arr[h];
        //smallest index element
        int i = l-1;
        for(int j=l;j<=h-1;j++){
             //Compare elements and swap.
            if(arr[j]<=pivot)
            {
                i++;
                swap(arr, j, i);
            }
        }
        swap(arr, i+1, h);
        return i+1;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<>();
        stack.push(l);
        stack.push(h);
        while(!stack.isEmpty()){
            h=stack.pop();
            l=stack.pop();
            int partIndex = partition(arr, l, h);
            if(partIndex-1 >l)
            {
                stack.push(l);
                stack.push(partIndex-1);
            }
            if(partIndex+1<h)
            {
                stack.push(partIndex+1);
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