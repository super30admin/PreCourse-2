// Time Complexity : O(NlogN)
//  Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : No

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
           arr[i] = arr[i]+arr[j];
          arr[j] = arr[i] - arr[j];
         arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int m = arr[h];
        int index = (l-1);
        for(int j=l;j<=h-1;j++)
        {
            if(arr[j]<=m){
               index++;
               swap(arr,index,j);
            }
        }
       swap(arr,index+1,h);
       return(index+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
       int stack[] = new int[h-l+1];
      int top = -1;

      stack[++top] = l;
      stack[++top] = h;

      while(top>=0){
          h = stack[top--];
          l = stack[top--];

          int mid = partition(arr, l, h);
          if(mid-1>l){
              stack[++top] = l;
              stack[++top] = mid-1;
          }
          if(mid+1<h){
              stack[++top] = mid+1;
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