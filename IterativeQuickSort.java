import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

public class IterativeQuickSort { 
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
    	int pivot = arr[h];
        int i = l-1;
        for (int j = l; j<=h; j++)
        { if (arr[j]<pivot)
            {   
                i++;
                swap(arr,i,j);
            } 
        }
        swap(arr,i+1,h);
        return(i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	 int endIndex = arr.length-1;
         int startIndex = 0;
         Stack<ArrayList<Integer>> indexPair = new Stack<ArrayList<Integer>>();
         ArrayList<Integer> subStack = new ArrayList<Integer>(Arrays.asList(startIndex,endIndex));
         indexPair.add(subStack);
         while (!indexPair.empty()){
             ArrayList<Integer> pair = indexPair.peek();
             indexPair.pop();
             startIndex = pair.get(0);
             endIndex = pair.get(1);
             int partitionIndex = partition(arr,startIndex,endIndex);
             if (partitionIndex-1>startIndex){
                 ArrayList<Integer> newSubStack = new ArrayList<Integer>(Arrays.asList(startIndex,partitionIndex-1));
                 indexPair.add(newSubStack);
             }
             if (partitionIndex+1<endIndex){
                 ArrayList<Integer> newSubStack = new ArrayList<Integer>(Arrays.asList(partitionIndex+1,endIndex));
                 indexPair.add(newSubStack);
             }
             //System.out.println(indexPair);

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