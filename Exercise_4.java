
class MergeSort {
	
	void merge(int [] arr,int [] l_arr,int [] r_arr)
	{
		int a=0,l=0,r=0;
		while(l<l_arr.length && r<r_arr.length)
		{
			if(l_arr[l]<=r_arr[r])
			{
				arr[a]= l_arr[l];
				a++;
				l++;
			}
			
			else
			{
				arr[a]= r_arr[r];
				a++;
				r++;
			}
		 }
		
		while(l<l_arr.length)
		{
			arr[a] = l_arr[l];
			a++;
			l++;
		}
		while(r<r_arr.length)
		{
			arr[a] = r_arr[r];
			a++;
			r++;
		}	
		
	}
	
	void sort(int[]arr)
	{   
		if(arr.length>1)
		{
			int mid = (arr.length)/2;
			int [] left_arr = new int [mid];
			for(int i=0;i<mid;i++)
			{
				left_arr[i] = arr[i];
			}
			
			int [] right_arr = new int[(arr.length)-mid];
			for(int i=0;i<arr.length-mid;i++)
			{
				right_arr[i] = arr[mid+i];
			}
			
			sort(left_arr);
			sort(right_arr);
			merge(arr,left_arr,right_arr);
					
		}
	}
		void print_array(int []arr)
		{
			for(int i=0;i<arr.length;i++)
			{
				System.out.println(arr[i]);
				
			}
			System.out.println(" ");
		}
			
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = {12, 11, 13, 5, 6, 7};
		MergeSort ob = new MergeSort(); 
		ob.sort(arr);
		ob.print_array(arr);
        

	}

}
