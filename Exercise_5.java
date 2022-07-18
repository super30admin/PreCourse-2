// Time Complexity : O(nlog n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : no
// Any problem you faced while coding this : no


/*Your code here along with comments explaining your approach -- Divide and concur
•    Create an auxiliary stack
•   initialize top of stack
•    push initial values of l and h to stack
•   Keep popping from stack while is not empty
•    Set pivot element at its correct position
•   If there are elements on left side of pivot,then push left side to stack
If there are elements on right side of pivot,then push right side to stack
*/


class Exercise_5 { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	int temp =arr[i];
    	arr[i]=arr[j];
    	arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
    	int pivot= arr[h];
    	int r=l-1;
    	for(int i=l;i<=h-1;i++) {
    		if(arr[i]<pivot) {
    			r++;
    			swap(arr,r,i);
    		}
    	}
    	swap(arr,r+1,h);
    	return(r+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	 int[] stack = new int[h - l + 1];
    	   int top = -1;
    	   stack[++top] = l;
           stack[++top] = h;
           while (top >= 0) {
               h = stack[top--];
               l = stack[top--];
               int p = partition(arr, l, h);
               if (p - 1 > l) {
                   stack[++top] = l;
                   stack[++top] = p - 1;
               }
                   if (p + 1 < h) {
                       stack[++top] = p + 1;
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
    	Exercise_5 ob = new Exercise_5(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 