// Time Complexity : O(N*logN) 
// Space Complexity : O(logN)
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
        arr[i]=arr[i]+arr[j];
        arr[j]=arr[i]-arr[j];
        arr[i]=arr[i]-arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
       //Compare elements and swap.
       int pivot = arr[h];
       int i=l-1;
       for(int j=l; j<=h-1; j++){
          //If array[j] is smaller than or eqaul to pivot
           if(arr[j] <= pivot){
               i++;
               //Swap elements of arr[i] and arr[j]
               swap(arr, i, j);
           }
       }
       //Swap elements of arr[i+1] and arr[high]
       swap(arr, i+1, h);
       return i+1;
        
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        //Create stack
        int[] stk = new int[h-l+1];
        //Initialize to as -1 to indicate stack is empty
        int top=-1;
        //push l and h in stack
        stk[++top] = l;
        stk[++top] = h;
        while(top>0){
            //Pop h and l from stack
            h=stk[top--];
            l=stk[top--];
            //Create int variable p which is pivot element
            int p = partition(arr, l, h);
            //If there are elements on left side of pivot push leftside to stack
            if(p - 1 > l){
                stk[++top]=l;
                stk[++top]=p-1;
            }
            //If there are elements on rightside of pivot push rightside to stack
            if(p + 1 < h){
                stk[++top] = p+1;
                stk[++top]=h;
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