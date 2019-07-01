class SwapCheck
{
	 void swap(int arr[], int i, int j) 
	    { 
		//Try swapping without extra variable 
	    	
	    	System.out.println("Before: "+arr[i]+" "+arr[j]);
	    	arr[i] = arr[i] + arr[j];
	    	System.out.println(arr[i] + " " + arr[j]);
	    	arr[j] = arr[i] - arr[j];
	    	System.out.println(arr[i]+ " "+arr[j]);
	    	arr[i] = arr[i] - arr[j];
	    	System.out.println(arr[i]+ " "+arr[j]);
	    	System.out.println("After: "+arr[i]+" "+arr[j]);
	    	
	    }
	 
	 public static void main(String args[])
	 {
		 SwapCheck obj = new SwapCheck();
		 int arr[] = {2,2};
		 obj.swap(arr,0,arr.length-1);
	 }
}