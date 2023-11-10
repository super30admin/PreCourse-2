import java.util.Stack;

// Time Complexity :  O(logn)
// Space Complexity :   O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
class IterativeQuickSort { 

    class newstack{
        int start;
        int end;
        newstack(int start,int end)
        {
            this.start=start;
            this.end=end;
        }
    }
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
        int pivot=arr[h];
        int i=l,j=h;
        int p=h;
        while(i<j){
            if(arr[i]<pivot){
                i++;
            }
            if(arr[j]>pivot){
                j++;
            }
            if(i<j){
                swap(arr,i,j);
            }
           
        }
        swap(arr,j,p);
        return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        Stack<newstack> stack=new Stack<>();

        stack.push(new newstack(l,h));
        //Try using Stack Data Structure to remove recursion.
        while(!stack.isEmpty())
        {
            newstack startEnd=stack.pop();
            l=startEnd.start;
            h=startEnd.end;
            int p=partition(arr, l, h);
            if(p-1>l)
            stack.push(new newstack(l,p-1));
            if(p+1<h)
            stack.push(new newstack(p+1,h));

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