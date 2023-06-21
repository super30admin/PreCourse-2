/*
Time Complexity: nlog(n)->n iterations in partition() and log n times for storing
                          values on stack
 Space Complexity:log(n)-> we store values on stack and its depth is height of tree
*/

import java.util.Stack;

class IterativeQuickSort {
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable j
        // swap only if elements at i and j th index are different,not otherwise
        if(arr[i]!=arr[j]) {
            arr[i] = arr[i] + arr[j];
            arr[j] = arr[i] - arr[j];
            arr[i] = arr[i] - arr[j];
        }

    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        //Write code here for Partition and Swap
        int i=l-1;
        int pivot=arr[h];
        for(int j=l;j<h;j++)
        {
            //swap only if elements are less than pivot
            //i will be used to track index of smaller elements
            if(arr[j]<pivot)
            {
                i++;
                swap(arr,i,j);
            }
        }
        //element till it are smaller than pivot
        //so i+1 will be correct position for pivot
        swap(arr,i+1,h);
        //return index of pivot
        return i+1;
    }
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<Pair> stk=new Stack<>();
        //push the first and last index on stack at the start
        stk.push(new Pair(l,h));
        while(!stk.empty())//breaking condition
        {
            int start=stk.peek().getX();
            int end=stk.peek().getY();
            stk.pop();
            //find pivot position from partition function
            int pivot=partition(arr,start,end);
            //if there are elements which are smaller than pivot, push their start
            //and end index on stack (same like we make recursive call for left subarray)
            if(pivot-1>start)
            {
                stk.push(new Pair(start,pivot-1));
            }
            //if there are elements which are larger than pivot, push their start
            //and end index on stack (same like we make recursive call for right subarray)
            if(pivot+1<end)
            {
                stk.push(new Pair(pivot+1,end));
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
class Pair
{
    int x;
    int y;
    public Pair(int x,int y)
    {
        this.x=x;
        this.y=y;
    }
    public int getX()
    {
        return this.x;
    }
    public int getY()
    {
        return this.y;
    }

}