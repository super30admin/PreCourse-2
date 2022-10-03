// Time Complexity :O(n.logn)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this :no
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	  int t = arr[i];
      arr[i] = arr[j];
      arr[j] = t;//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int x = arr[h];
        int i = (l - 1);
 
        for (int j = l; j <= h - 1; j++) {
          if (arr[j] <= x) {
          i++;
           // swap arr[i] and arr[j]
           swap(arr, i, j);
              }
  }
  // swap arr[i+1] and arr[h]
  swap(arr, i + 1, h);
  return (i + 1);
    } 
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
  }//Try using Stack Data Structure to remove recursion.
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
