// Time Complexity :O(nlogn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode :
// Any problem you faced while coding this :


// Your code here along with comments explaining your approach
import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(i!=j)
        {
            arr[i]=arr[i]+arr[j];
            arr[j]=arr[i]-arr[j];
            arr[i]=arr[i]-arr[j];
        }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot=arr[h];
        int i=l;
        for(int j=l;j<h;j++)
        {
            if(arr[j]<pivot){
                swap(arr,i,j);
                i++;
            }
        }
        swap(arr,i,h);
        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<int[]> temp=new Stack<>();
        int[] i={l,h};
        temp.push(i);
        while(!temp.isEmpty()){
            int[] ix=temp.pop();
            int lx=ix[0];
            int hx=ix[1];
            if(lx<hx){
                int p=partition(arr, lx, hx);
                int[] a1={lx,p-1};
                int[] a2={p+1,hx};
                temp.push(a1);
                temp.push(a2);
            }

        }

    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println();
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