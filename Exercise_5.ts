class IterativeQuickSort { 
    swap(arr: number[], i:number, j:number) :void
    { 
	    //Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    partition(arr: number[], l: number, h:number): number
    { 
        //Compare elements and swap.
        var pivot: number= arr[h];
        var i:number=l-1;
        var temp: number;
        for(let j=l;j<=h-1;j++){
            if(arr[j]<=pivot){
                i++;
                temp= arr[i];
                arr[i]= arr[j];
                arr[j]= temp;
            }
        }
            temp= arr[i+1];
            arr[i+1]= pivot;
            arr[h]= temp;
            i++;
        //console.log(i);

        return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    QuickSort(arr: number[], l:number, h:number):void 
    { 
        //Try using Stack Data Structure to remove recursion.
        var stack:number[] = [];
        var top:number=-1;
        stack[++top]=l;
        stack[++top]=h;

        while(top>=0){
            //pop h and l
            h= stack[top--];
            l=stack[top--];

            var p: number= this.partition(arr,l,h);
            
            // If there are elements on
			// left side of pivot, then
			// push left side to stack
			if (p - 1 > l)
			{
				stack[++top] = l;
				stack[++top] = p - 1;
			}

			// If there are elements on
			// right side of pivot, then
			// push right side to stack
			if (p + 1 < h)
			{
				stack[++top] = p + 1;
				stack[++top] = h;
			}
        }
    } 
  
    // A utility function to print contents of arr 
    printArr(arr:number[], n:number): void 
    { 
        for (let i = 0; i < n; ++i) 
           console.log(arr[i] + " "); 
    } 
}
    // Driver code to test above 
 
        var obj: IterativeQuickSort = new IterativeQuickSort(); 
        var arr: number[] = [ 4, 3, 5, 2, 1, 3, 2, 3 ]; 
        obj.QuickSort(arr, 0, arr.length - 1); 
        obj.printArr(arr, arr.length); 