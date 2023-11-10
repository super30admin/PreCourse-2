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
    	int j = l;
    	int pivot = arr[h];
    	for(int i = l; i<h; i++) {
    		if(arr[i]< pivot) {
    			swap(arr, i, j);
    			j++;
    		}
    	}
    	swap(arr, j, h);
    	return j;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<PartitionValue> stack=new Stack<>();
    	stack.push(new PartitionValue(l, h));
    	
    	while(!stack.isEmpty()) {
    		PartitionValue temp=stack.pop();
    		if(temp.low < temp.high) {
    			int mid = partition(arr,temp.low,temp.high);
        		
        		stack.add(new PartitionValue(temp.low, mid-1));
        		
        		stack.add(new PartitionValue(mid+1,temp.high));
    		}
    		
    	}
    	
    	
    	
    } 
    class PartitionValue{
    	int low, high;
    	
    	PartitionValue(int l, int h){
    		low = l;
    		high = h;
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