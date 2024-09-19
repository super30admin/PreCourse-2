import java.util.*;
public class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	   //Try swapping without extra 
        /*arr[i]+=arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]-=arr[j];*/
        int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[l];
        int i=l+1, j=h;
        while(i<j){
            while(i<h && arr[i]<=pivot) i++;
            while(j>=l && arr[j]>pivot) j--;
            if(i<j) {
                swap(arr, i, j);
                i++;j--;
            }
        }
        swap(arr,j,l);
        return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Integer> recurse = new Stack<>();
        int i,j;
        recurse.push(l);
        recurse.push(h);
        while(!recurse.isEmpty()){
            j=recurse.pop();
            i=recurse.pop();
            if(i<j){
                int pivot = partition(arr, i, j);
                   
                recurse.push(i);
                recurse.push(pivot-1);
                                
                recurse.push(pivot+1);
                recurse.push(j);
                
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