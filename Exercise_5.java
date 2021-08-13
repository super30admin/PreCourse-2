    
    // Time Complexity : O(Nlog(N))
    // Space Complexity : O(1)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No

class IterativeQuickSort { 
    
    void swap(int arr[], int i, int j) 
    { 
	// swapping without extra variable
    if(arr[i]==arr[j]){
        return;
    }
    arr[i]=arr[i]+arr[j];
    arr[j]=arr[i]-arr[j]; 
    arr[i]=arr[i]-arr[j];
    } 

      /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
   	/* This function takes first element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
       int count=0;
       //finding total number of elements lower than pivot element
       int pivotElement = arr[low];
       for(int i=low;i<=high;i++){
           if(arr[i]<pivotElement){
               count++;
           }
       }
       // swapping the pivot element to correct position
       swap(arr,low,low+count);
  
    
       //putting elements lower than pivot its left and greater than on its right
       int lower = low;
       int higher = high;
       while(lower<higher){
            if(arr[lower] <pivotElement){
                lower++;
            }else if(arr[higher]>=pivotElement){
                higher--;
            }else{
                swap(arr, lower, higher);
                     
            }
       }
       //returns the index of pivot element
       return low+count;


    } 
  
  
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
       
        int stack[] = new int[h - l + 1];
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
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { -1, 3, 0, 2, 20, 8, 2, 10 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 