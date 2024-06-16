// Time Complexity : O(nlogn)
// Space Complexity : 0(n) 
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : problem with swap function, it didn't work until I used 2 new variables and applied same logic

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    int x=arr[i];
    int y=arr[j];
    x=x+y;
    y=x-y;
    x=x-y;

    arr[i] = x;
    arr[j] =y;
    
    // Below code doesn't work even though the logic is same as above
    // arr[i] = arr[i]+arr[j];
    // arr[j] = arr[i]-arr[j];
    // arr[i]= arr[i]-arr[j];

  
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
      int pivot = arr[h];  //Assign last element in arr to be pivot
      int k = l-1;         // this is a pointer to the smaller element
      for(int i=l;i<h;i++){ //iterate through low to high-1
        if(arr[i]<pivot){  
          k++;              //if elemet is smaller, then swap
          swap(arr,k,i);
        }
      }
      swap(arr,k+1,h);   //place pivot after all smaller elements
      return k+1;    //return pivot index

    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //create stack
        int[] stack = new int[h - l + 1]; 
        int top = -1; 

        //push low and high elements
        stack[++top] = l;  
        stack[++top] = h; 
  
      while (top >= 0) { 
           //Pop low and high elements
            h = stack[top--]; 
            l = stack[top--]; 


            //find pivot index
            int p = partition(arr, l, h); 

            //if there are elements to the left of pivot, then push high and low of the subarray, this will keep the loop continuing until all elements are done
            if (p - 1 > l) { 
                stack[++top] = l; 
                stack[++top] = p - 1; 
            } 

            //if there are elements to the righ of pivot, then push high and low of the subarray
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
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 