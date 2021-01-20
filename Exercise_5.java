import java.util.*;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable
    //System.out.println(arr[i]+""+arr[j]);
    
    arr[i] = arr[i] + arr[j];
    arr[j] = arr[i] - arr[j];
    arr[i] = arr[i] - arr[j];
    //System.out.println(arr[i]+""+arr[j]);
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pi = arr[h];
        int j = l-1;
        for(int i = l;i<h-1;i++){
            if(arr[i] > pi){
                j++;
                swap(arr,i,h);

            }
        }
        swap(arr,j+1,h);
        return j+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if(arr.length < 2){
            System.out.println("Enter array with atleast 2 elements please!");

            return;
        }
        // Stack<Integer> stk = new Stack<Integer>();

        int[] stack = new int[h+1-l];

        int top = -1;

        stack[++top] = l;
        stack[++top] = h;

        while(top >= 0){
            h = stack[top--];
            l = stack[top--];

            int p = partition(arr,l,h);

            if(p-1 > l){
                stack[++top] = l;
                stack[++top] = p -1;
            }

            if(p+1 < h){
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
        // int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        int arr[] = {1};
        // ob.swap(arr, 0,1);

        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 


    } 
} 