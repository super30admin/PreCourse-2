
import java.util.Stack;
import java.util.stream.IntStream;
import java.util.stream.Collectors;
import java.util.ArrayList;
import java.util.Random;
import java.util.Arrays;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    //Try swapping without extra variable 
    int t = arr[i];
    arr[i] =  arr[j];
    arr[j] = t;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    {   Random rand = new Random();
        //Compare elements and swap.
        int index = rand.nextInt(arr.length-1);
        int pivot = arr[index];
        System.out.println("POS "+ index);
        while(l < h){
            while( arr[l] < pivot){
                l++;
            }
            while(arr[h]>= pivot){
                h--;
            }
            if(l<=h){
                swap(arr, l, h);
                l++;
                h--;
            }
        }
        swap(arr, l, index);
        return l;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> stack = new Stack<Integer>();
        int pos = partition(arr, l, h);
        stack.push(pos);
        System.out.println(pos);
        while(!stack.empty()){
            int a = stack.pop();
            if(a > 0){
            int pos_left = partition(arr, l, a-1);
            System.out.println(pos_left);
            stack.push(pos_left);
            }
            if(a < arr.length-1){
            int pos_right = partition(arr, a+1, h);
            System.out.println(pos_right);
            stack.push(pos_right);
            }
            System.out.println(stack);
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