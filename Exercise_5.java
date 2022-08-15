/*time complexity O(n^2)
 * Space complexity O(n) when the stack is full*/
import java.util.Stack;
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable 
    	if(i==j) {
    		return;
    	}
		arr[i]=arr[i]^arr[j];
    	arr[j]=arr[i]^arr[j];
     	arr[i]=arr[i]^arr[j];
     	
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int pivot=h;
    	int x=l;
     	int y=h-1;
    	while(true) {
     	while(true) {
    		if(arr[x]<=arr[pivot]&&x<=h-1) {
    			x++;
    		}
    		if(arr[y]>=arr[pivot]&&y>=l) {
    			y--;
    		}
    		if(x<y) {
    			break;
    		}
    		break;
    	}
    	if(x>y) {
    	swap(arr,pivot,x);
    	return x;
    	}
    	else {
    		swap(arr,x,y);
    	}
    	}
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 	
    	//Try using Stack Data Structure to remove recursion.
    	Stack<Integer> a =new Stack<Integer>();
    	a.push(l);
    	a.push(h);
    	while(!a.empty()) {
    		h=a.pop();
    		l=a.pop();
    		int d=partition(arr, l, h);
    		if(d-1>l) {
    			a.push(l);
    			a.push(d-1);
    		}
    		if(d+1<h) {
    			a.push(d+1);
    			a.push(h);
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