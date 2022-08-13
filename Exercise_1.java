class BinarySearch {
	public static int low, high, mid;

	public static void binarySearch(int arr[],int key) {
			low=0;
			high=arr.length-1;
			while(low<=high) {
				mid=(low+high);
				if(arr[mid]==key)//checking if mid is equal to key
					{
	
					System.out.print("key "+key+" found at "+ mid+"th\sposition");
					return;
				}else if(arr[mid]<key)//search in left subarray  
				{    
					low=mid+1;
				}
				else {
					//search in right subarray
					high=mid-1;
				}
			}
			//once low is greater then high that means key not found
			if ( low >high ){  
				System.out.println("Element is not found!");  
			}  
		}
//main
	public static void main(String arg[]) {
		int a[] = { 10, 20, 30, 40, 50 };
		BinarySearch.binarySearch(a, 50);

	}
}
