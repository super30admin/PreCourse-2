// Time Complexity :O(n^2)
// Space Complexity : O(n) n-length of the array.
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : Using stack
import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
	if(arr[i]!=arr[j]) // No need to swap if both elements are same
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
		for(int i=l;i<=h;i++)
		{
			if(arr[i]<arr[h])//If pivot is greater than the number then we swap and increment the low pointer
			{
			swap(arr,l,i);
			l++;
			}
		} 
		swap(arr,l,h);// Swap the pivot element to it correct position
	return l; // return pivot index
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
		Stack<Integer> stack=new Stack<Integer>();
		stack.push(l);
		stack.push(h);
		while(!stack.isEmpty())
		{
		
	    int high=stack.pop();
		int low=stack.pop();		
		int pivot=partition(arr,low,high); // returns the position of the pivot
		if(pivot-1>low) // For elements to the left of the pivot
		{
		stack.push(low);
		stack.push(pivot-1);
		}
		if(pivot+1<high) // For elements to the right of the pivot
		{
		stack.push(pivot+1);
		stack.push(high);
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3,2 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 