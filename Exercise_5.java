//Time complexity is O(nlogn)
//space complexity is O(n)

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
        arr[i] = arr[i] + arr[j];
        arr[j] = arr[i] - arr[j];
        arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int pivot = arr[h];
        int i = (l - 1);
        for (int j = l; j <= h-1; j++)
       {
        if (arr[j] < pivot) {
       i++;
       swap(arr,i,j);
     }

    } 
 swap(arr, i+1, high);
 return (i+1);
}
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       Stack st = new Stack();
       st.push(0);
       st.push(arr.length);
       while(!st.isEmpty()){
      int end = st.pop();
      int start = st.pop();
      if (end - start < 2){ 
       continue;    
    }
  int p = start + ((end - start)/2);
  p = partition(arr, p , start, end);
  st.push(p+1);
  st.push(end);
  st.push(start);
  st.push(p);
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
