// Time Complexity :  O(nlogn) for best case and O(n^2) for worst case
// Space Complexity :  O(n)
// Did this code successfully run on Leetcode : No
// Any problem you faced while coding this : No

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
         int i = l - 1;

      
        for(int j=l;j<h;j++){

            if(arr[j]<arr[h]){
                i = i+1;
                swap(arr, i, j);                 
            }
        }
       
       swap(arr, i+1, h);        
       return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int[] st = new int[h-l+1];

        int top = -1;

        top = top+1;
        st[top] = l;
        top = top+1;
        st[top] = h;

        while(top >=0){
            h = st[top];
            top = top-1;
            l = st[top];
            top = top-1;

            //pivot element

            int pi = partition(arr, l, h);

            if(pi-1>l){
                top = top+1;
                st[top] = l;
                top = top+1;
                st[top] = pi-1;
            }
            if(pi+1<h){
                top = top+1;
                st[top] = pi+1;
                top = top+1;
                st[top] = h;
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