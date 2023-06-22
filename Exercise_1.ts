export class BinarySearch { 
    // Returns index of x if it is present in arr[l.. r], else return -1 
     binarySearch( arr: number[], l: number, r:number, x:number): number{ 
        //Write your code here
        while(l<=r){
            const mid: number= Math.floor((l+r)/2);
            console.log(mid);
            if(arr[mid]==x) return mid;
            
            (x<arr[mid])? r=mid-1: l=mid+1;
        }

        return -1;
    } 
}
    // Driver method to test above 

        var  ob: BinarySearch = new BinarySearch(); 
        var arr: number[] = [ 2, 3, 4, 10, 40 ]; 
        var n:number = arr.length; 
        var x:number = 10; 
        var result:number = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            console.log("Element not present"); 
        else
            console.log("Element found at index " + result); 
