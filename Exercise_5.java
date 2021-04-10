import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	    //Try swapping without extra variable
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int index = l-1;
        int key = arr[h];
        for(int j=l;j<=h-1;j++){
            if(arr[j]<key)
            {
                index+=1;
                swap(arr,index,j);
            }
        }
        swap(arr,index+1,h);
        return index+1;
    }
    public class Indices{
        int low;
        int high;
        public Indices(int low,int high)
        {
            this.low = low;
            this.high = high;
        }
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Indices> stk = new Stack<Indices>();
        Indices first = new Indices(l,h);
        stk.push(first);
        while(!stk.isEmpty())
        {
            Indices temp = stk.pop();
            if(temp.low<temp.high)
            {
                int p = partition(arr, temp.low, temp.high);
                stk.push(new Indices(temp.low, p-1));
                stk.push(new Indices(p+1, temp.high));
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
        //int arr[] = {10, 7, 8, 9, 1, 5}; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 