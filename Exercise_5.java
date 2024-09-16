import java.util.Stack;

class IterativeQuickSort { 

    class StartEnd{
        int start;
        int end;
        StartEnd(int start,int end)
        {
            this.start=start;
            this.end=end;
        }
    } 
    void swap(int arr[], int i, int j) 
    { 
	   //Try swapping without extra variable 
       /*arr[i]=arr[i]+arr[j];
       arr[j]=arr[i]-arr[j];
       arr[i]=arr[i]-arr[j];*/

       int temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
        int i=l-1;
        for(int j=l;j<=h-1;j++)
        {
            if(arr[j]<=arr[h])
            {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, h);

        return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        Stack<StartEnd> stack=new Stack<>();

        stack.push(new StartEnd(l,h));
        //Try using Stack Data Structure to remove recursion.
        while(!stack.isEmpty())
        {
            StartEnd startEnd=stack.pop();
            l=startEnd.start;
            h=startEnd.end;
            int p=partition(arr, l, h);
            if(p-1>l)
            stack.push(new StartEnd(l,p-1));
            if(p+1<h)
            stack.push(new StartEnd(p+1,h));
           
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