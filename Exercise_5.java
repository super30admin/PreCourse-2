// Time Complexity : Worst-O(n^2), Average: O(nlogn)
// Space Complexity : O(n)

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
        int pivot=h;
        int s=l;
        for(int i=l;i<pivot;i++){
            if(arr[i]<arr[pivot]){
                if(s!=i){
                    swap(arr,s,i);
                }
                s++;
            }
        }
        swap(arr, s, pivot);
        return s;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        int stack[] = new int[h-l+1];
        int top=-1; //initializing top of stack
        //pushing initial values of l and h to stack
        stack[++top]=l;
        stack[++top]=h;
        //pop until stack is not empty
        while(top>=0){
            h=stack[top--]; //pop h
            l=stack[top--]; //pop l
            int p=partition(arr, l, h);
            //push left side elements to stack, if there are any
            if(p-1>l){
                stack[++top]=l;
                stack[++top]=p-1;
            }
            //push right side elements to stack, if there are any
            if(p+1<h){
                stack[++top]=p+1;
                stack[++top]=h;
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