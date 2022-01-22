/**
Quick Sort - It's a devide & Conqure algorithm.
// Time Complexity :
    Sorting - in the worst case O(n^2) where n is the length of an array. It occurs if the partiion process picks every time the largest element as pivot. Best case O(nlogn) where n is the length of an array. It occurs when the partition process every time picks the median as the pivot from the array.  
// Space Complexity :
    Total space complexity = Auxilary space + space used towards input.
    O(n) in worst case and O(logn) for best case. where n is the length of an array.
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
**/
import java.util.*;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
        int temp = arr[j];
        arr[j] = arr[i];
        arr[i] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int pivot_element = arr[h];
        int i = l - 1;
        int j;
        for(j=l; j<h; j++)
        {
            if (arr[j] < pivot_element)
            {
                i++;
                swap(arr, i, j);
            }
        }
        
        i++;
        swap(arr, i, j);
        return i;
    } 
    
    // -9 -5 -4 1 1 2 6 7 8 11 12 13 
    
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<int[]> stackToHoldValues = new Stack<>();
        int partion_index = partition(arr, l, h);
        stackToHoldValues.push(new int[]{l, partion_index - 1});
        stackToHoldValues.push(new int[]{partion_index + 1, h});
        
        while (!stackToHoldValues.isEmpty())
        {
            int pop[] = stackToHoldValues.pop();
            l = pop[0];
            h = pop[1];
            
            
            if (l >= h)
            {
                continue;
            }
            
            partion_index = partition(arr, l, h);
            stackToHoldValues.push(new int[]{l, partion_index - 1});
            stackToHoldValues.push(new int[]{partion_index + 1, h});
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