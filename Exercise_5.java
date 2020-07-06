import java.util.Stack;

class IterativeQuickSort { 
    static void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	
    	if(arr[i] == arr[j])
    		return;
    	arr[i] = arr[i] + arr[j];
    	arr[j] = arr[i] - arr[j];
    	arr[i] = arr[i] - arr[j];
    } 
    
    //Approach: Here there are 3 functions, 
  	//swap - to swap elements in the array
  	//partition - choose a pivot element , here am choosing last element as pivot 
  	// and rearrange the array such that elements less than pivot comes before it and element 
  	// higher than it goes after it in the array.
  	//sort - sorting is done using a stack, here am pushing the l and h values and managing 
    // the recursion with a stack 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
    	printArr(arr, arr.length);
        //Compare elements and swap.
    	int i=(l-1);
    	int pivot = arr[h];
    	for(int j=l ; j <= h-1 ;j++)
    	{
    		if(arr[j] < pivot)
    		{
    			i++;
    			swap(arr,i,j);
    		}
    	}    	
    	swap( arr, i+1, h);
    	return (i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
    	printArr(arr, arr.length);
        //Try using Stack Data Structure to remove recursion.
    	Stack<Integer> stack = new Stack<>();
    	//initiaize stack with range values l and h
    	stack.push(l);
    	stack.push(h);
    	while(!stack.isEmpty())
    	{
    		h = stack.pop();
    		l = stack.pop();
    		int partition = partition(arr, l, h);
    		
    		if(partition - 1 > l)
    		{
    			stack.push(l);
    			stack.push(partition-1);
    		}
    		if(partition + 1 < h)
    		{
    			stack.push(partition+1);
    			stack.push(h);
    		}
    	}
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        System.out.println("");
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
     //   int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 };
        int arr[] = { 4, 1, 2, 3, 5 };
        ob.printArr(arr, arr.length);
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 

//Time Complexity : O(n2), since by worst case we might end up choosing the pivot wrongly such that
//the partition might end up resulting in n-1 elements and 1 element halves. In this case we have to sorting 
//for althose n-1 elements all over again.
//Space Complexity : O(1) no extra space is used
//Did this code successfully run on Leetcode : NA
//Any problem you faced while coding this : Yes, I could not do the swapping without extra variable part.