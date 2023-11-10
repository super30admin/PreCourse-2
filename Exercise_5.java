////Time Complexity : Best case is when the pivot element is the middle element in the sorted array, then O(nlogn). Otherwise it would be O(n^2) in the worst case
//Space Complexity : The iterative solution is using a stack to store the fucntion calls, at worst , when the array is already sorted, then it could be O(n)
//Did this code successfully run on Leetcode :
//Any problem you faced while coding this : yes, while implementing the swapping logic without third variable, 
//I encountered some bug which was printing invalid values in the sorted array. Later on, I found out that new swapping logic
//does not work when i and j are pointing to the same index in the array. I then implemented a guard condition which solved my
//problem


//Your code here along with comments explaining your approach


class IterativeQuickSort { 
  void swap(int arr[], int i, int j) 
  { 
	//Try swapping without extra variable 

  	if(i ==j) // since we are swapping value of the same index and using swap technique without third variable, the logic would not work if both pointers point to the same element
  		return; // return as swapping would not have any affect
  	//else
  	arr[i] = arr[i] + arr[j];
  	arr[j] = arr[i] - arr[j];
  	arr[i] = arr[i] - arr[j];  	
  	
  	/*
  	 *  if a  =1 , b=4
  	 *  
  	 *  then 
  	 *  a = a+b;
  	 *  b = a-b;
  	 *  a= a - b;
  	 *  
  	 *  new values : a=4, b=1
  	 *  	
  	 */
  } 

  /* This function is same in both iterative and 
     recursive*/
  int partition(int arr[], int l, int h) 
  { 
      //Compare elements and swap.
  	int pivot = arr[h]; // taking last element as pivot
  	int i = l -1; // i would point to the position where the element smaller than pivot should be
  	
  	for(int j=l;j<=h;j++) { // we need to visit each element until the pivot
  		if(arr[j] <= pivot) { 
  			i++; // incrementing i , so it points to the next place where smaller element should b
  			swap(arr,i,j); // swapping i with j
  		}    		
  	}
  	
  	// i is now pointing to the pivot position
  	return i;
  } 

  // Sorts arr[l..h] using iterative QuickSort 
  void QuickSort(int arr[], int l, int h) 
  { 
  	// The stack would represent the state of the recursive function call stack
	  // After each iteration , we would push the state of the next function call
	  // This way the stack would mimic the recursive call stack
  	Stack<Integer[]> stack = new Stack<Integer[]>();
  	Integer[] element = new Integer[2]; // array to store the partition limits 
  	
  	element[0] = l; //  0 index for low pointer
  	element[1] = h; // 1 index for high pointer
  	stack.push(element);
      //Try using Stack Data Structure to remove recursion.
  	
  	while(!stack.isEmpty()) { 
  		Integer[] current = stack.pop();
  		int low = current[0];
  		int high = current[1];
  	
  	if(low<high) {
  		int pivotPosition = partition(arr,low, high);
  		// Since we have to explore the left array and right array array, 
  		// we will push them in stack  in form of low and high pairs
  		// Whatever gets pushed to the stack at last , that path would be further traversed
  		// For example, we are putting the right partition in the stack , then it would get traversed first
  		
  		Integer[] leftPartition = new Integer[2];
  		leftPartition[0] = low;
  		leftPartition[1] = pivotPosition - 1; // pivot already in its position, so not including it
  		stack.push(leftPartition); // left partition would contain elements from low till pivotPosition - 1
  		
  		Integer[] rightPartition = new Integer[2];
  		rightPartition[0] = pivotPosition+1; // pivot already in its position, so not including it
  		rightPartition[1] = high;
  		stack.push(rightPartition);// right partition would contain elements from pivotPosition + 1 to high

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
      //int arr[] = { 10, 7, 8, 9, 1, 5 };
      ob.QuickSort(arr, 0, arr.length - 1); 
      ob.printArr(arr, arr.length); 
  } 
} 