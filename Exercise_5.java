import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	int temp=arr[i];
    	arr[i]=arr[j];
    	arr[j]=temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot=arr[h];
    	int i=l-1;
    	for(int j=l;j<=h-1;j++)
    	{
    		if(arr[j]<=pivot)
    		{
    			i++;
    			swap(arr,i,j);
    		}
    	}
    	swap(arr,i+1,h);
    	return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    //Time Complexity: o(nlogn)
    //Space Complexity: o(logn)
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<Integer> s=new Stack<Integer>();
    	int low=l;
    	int high=h;
    	s.push(low);
    	s.push(high);
    	while(s.size()>0)
    	{
    		high=s.pop();
    		low=s.pop();
    		if(low>high)
    			continue;
    		int pivot=partition(arr, low, high);
    		s.push(low);
            s.push(pivot - 1);
            s.push(pivot + 1);
            s.push(high);
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