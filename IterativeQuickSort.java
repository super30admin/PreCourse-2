import java.util.Stack;

class Pair{
	
	private int x;
	private int y;
	
	Pair(int x, int y){
		this.x = x;
		this.y = y;
	}
	
	public int getX() {
		return x;
	}
	
	public int getY() {
		return y;
	}
}
public class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
    	int temp = arr[i];
    	arr[i] = arr[j];
    	arr[j] =temp;
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot = h;
    	int s = l;
    	
    	for(int i = l; i <= h; i++) {
    		if(arr[i] < arr[pivot]) {
    			swap(arr, s, i);
    			s++;
    		}
    	}
    	swap(arr, s, pivot);
    	return s;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[]) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	Stack<Pair> stack = new Stack<>();
    	int start = 0;
    	int end = arr.length - 1;
    	
    	stack.push(new Pair(start, end));
    	
    	while(!stack.isEmpty()) {
    		start = stack.peek().getX();
    		end = stack.peek().getY();
    		stack.pop();
    		
    		int pivot = partition(arr, start, end);
    		
    		if(pivot - 1 > start) {
    			stack.push(new Pair(start, pivot - 1));
    		}
    		if(pivot + 1 < end) {
    			stack.push(new Pair(pivot + 1, end));
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
        ob.QuickSort(arr); 
        ob.printArr(arr, arr.length); 
    } 
} 