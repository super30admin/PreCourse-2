class IterativeQuickSort { 
    // Time Complexity :O(n2) in worst case if the array is sorted
    // Space Complexity :O(n) size of the stack
    // Did this code successfully run on Leetcode :Yes
    // Any problem you faced while coding this : Had hard time to understand the partition algoithm.
    void swap(int arr[], int i, int j) 
    { 
        if(i!=j){
            arr[i]=arr[i]+arr[j];
            arr[j]=arr[i]-arr[j];
            arr[i]=arr[i]-arr[j];
        }
	//Try swapping without extra variable
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot=arr[h];
        int i=l-1;
        for(int j=l;j<=h-1;j++){
            if(arr[j]<=pivot){
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
         int [] stack=new int [h-l+1];
         int t=-1;
         stack[++t]=l;
         stack[++t]=h;
        
         while(t>=0){
             h=stack[t--];
             l=stack[t--];
             int pivotindex=partition(arr,l,h);
             if(pivotindex-1>l){
                stack[++t]=l;
                stack[++t]=pivotindex-1;
             }
             if(pivotindex+1<h){
                stack[++t]=pivotindex+1;
                stack[++t]=h;
             }
             
         }
        //Try using Stack Data Structure to remove recursion.
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