// Time Complexity : Same as recursive quick sort
// Space Complexity : Same as recursive quick sort
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : N/A
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        if(arr[i] == arr[j])
            return;
        arr[i] = arr[i]+arr[j]; //Adding both values to get the total 
        arr[j] = arr[i]-arr[j]; //Subtracting the element itself from total to store the 
                                  //other value in this variable ( got the required value for 
                                  //arr[j] )
        arr[i] = arr[i]-arr[j]; //Subtracting the previously obtained correct value from                                       //total to get the remaining value
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i = l-1;
        int pivot = arr[h];
        for(int j=l; j<=h-1; j++)
        {
            if(arr[j]<pivot)
            {
                i++;
                swap(arr,i,j);
            }
        }
        swap(arr,i+1,h);
        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Using Stack Data Structure to remove recursion.
        int[] stack = new int[h-l+1];
        int top = -1;
        stack[++top] = l;
        stack[++top] = h;
        
        while(top>=0)
        {
            h = stack[top--];
            l = stack[top--];
            
            int p = partition(arr,l,h);
            
            if(p-1 > l)
            {
                stack[++top] = l;
                stack[++top] = p-1;
            }
            
            if(p+1 < h)
            {
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 