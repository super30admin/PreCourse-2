// Time Complexity : O(N^2)
// Space Complexity : O(N)
// Did this code successfully run on Leetcode : ran it on local machine
// Any problem you faced while coding this : No
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    if(i!=j){  //exor on same values will give 0 which hampers our output
        arr[i] = arr[i] ^ arr[j];
        arr[j] = arr[i] ^ arr[j];
        arr[i] = arr[i] ^ arr[j];
    }
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int lp = l;
        for(int i=l;i<h;i++){
            if(arr[i]<=arr[h]){
                swap(arr,i,lp);
                lp++;
            }    
        }
        swap(arr, lp, h);
        return lp;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int size = h-l+1;
        int[] st = new int[size];
        int top = -1;
        st[++top] = l;
        st[++top] = h;
        while(top>=0){
            h = st[top--];
            l = st[top--];

            int partIndex = partition(arr, l, h);

            if(partIndex-1 > l){
                st[++top] = l;
                st[++top] = partIndex - 1;
            }

            if(partIndex+1 < h){
                st[++top] = partIndex + 1;
                st[++top] = h;
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