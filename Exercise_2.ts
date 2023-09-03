class QuickSort 
{ 
    /* This function takes last element as pivot, 
       places the pivot element at its correct 
       position in sorted array, and places all 
       smaller (smaller than pivot) to left of 
       pivot and all greater elements to right 
       of pivot */
     swap(arr: number[],i:number, j: number):void{
        let temp= arr[j];
        arr[j]=arr[i];
        arr[i]=temp;
        //Your code here   
    }
    
    partition(arr: number[], low: number, high: number):number{ 
   	//Write code here for Partition and Swap 
    let pivot= arr[high];
    let i = low;
    for(let j=low; j<high; j++){
        if(arr[j]<pivot){
            this.swap(arr,i,j);
            i++;
        }
    }
    this.swap(arr,i,high);
    return i;

    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    sort( arr: number[], low:number, high:number): number[]{  
            // Recursively sort elements before 
            // partition and after partition 
        if(low<high){
          var p: number= this.partition(arr, low, high);
          this.sort(arr,low,p-1);
          this.sort(arr,p+1, high);
        }
        //console.log(arr);
        return arr;
    } 

    printArray( arr: number[]): void
    { 
        var n: number = arr.length; 
        for (let i=0; i<n; ++i) 
            console.log(arr[i]+" ");  
    } 
  
    /* A utility function to print array of size n */
}
    // Driver program 
    var arr:number[] = [10, 7, 8, 9, 1, 5]; 
    var n: number = arr.length; 
  
    var ob: QuickSort = new QuickSort(); 
    ob.sort(arr,0,n-1);
    console.log("sorted array");
    ob.printArray(arr); 