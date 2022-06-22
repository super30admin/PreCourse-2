class QuickSort 
 public static int[] quickSort(int[] array) {
		    quickSort(array,0,array.length-1);
		    return array;
		  }
			
			public static void quickSort(int[] array,int startIdx, int endIdx){
		if (startIdx>=endIdx){
		return;
			
		}	
				int pivotIdx= startIdx;
			 int leftIdx = startIdx+1;
				int rightIdx= endIdx;
				
				while (rightIdx>=leftIdx){
					
					if ( array[leftIdx]> array[pivotIdx] && array[rightIdx] < array[pivotIdx]){
						swap(leftIdx,rightIdx,array);
					}if (array[leftIdx] <=array[pivotIdx]){
						leftIdx+=1;
					}if ( array[rightIdx] >=array[pivotIdx]){
						rightIdx-=1;
					}
					
				}
					swap(pivotIdx,rightIdx,array);
					boolean leftSubArrayISSmaller= rightIdx-1-startIdx<endIdx-(rightIdx+1);
				System.out.println("rightIdx "+rightIdx +" "+ "startIdx "+startIdx + " endIdx "+endIdx+ " rightIdx-1-startIdx "+ (rightIdx-1-startIdx) + " endIdx-(rightIdx+1) "+(endIdx-(rightIdx+1)));
			if(leftSubArrayISSmaller){
				
				quickSort(array,startIdx,rightIdx-1);
					quickSort(array,rightIdx+1,endIdx);
		}  	else{
				quickSort(array,rightIdx+1,endIdx);
					quickSort(array,startIdx,rightIdx-1);
			}
		}

		public static void swap(int i , int j , int [] array){
			int temp=array[j];
			array[j] = array[i];
			array[i]= temp;
			
		}
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 
