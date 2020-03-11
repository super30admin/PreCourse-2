// Time Complexity :O(nlogn)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : N/A


// Your code here along with comments explaining your approach

//Insertion of an element in Binary Search


#include <iostream>

using namespace std;


int partition(int* &arr, int low, int high){
    int pivot=arr[low];
   
    int start =low, end =high;
    while(start<end){
        while(arr[start] <= pivot && start<high){
            start++;
        }
        while(arr[end] > pivot && end>low){
            end--;
        }
        if(start<end){
            swap(arr[end],arr[start]);
        }
    }
    
    if(start>=end){
        swap(arr[end],arr[low]);
    }
    return end;
}

void quick_sort(int* &arr, int low, int high){
 
    
    if(low<high){
        int pivot_index = partition(arr, low, high);
        //Call upper half
         quick_sort(arr, pivot_index+1, high);
        //Call lower half
         quick_sort(arr, low, pivot_index-1);
    }

}


int main(void){
    int arr[] = {770,  279,   844,   714,   687,   765,   888,   723,   807,   561,   270,   951,   778,   936,   600};
    int *arr_ptr = arr;
    quick_sort(arr_ptr, 0, (sizeof(arr)/sizeof(int))-1);
    int i=0;
    while(i<sizeof(arr)/sizeof(int)){
        cout<<arr[i]<<"\t";
        i++;
    }
    return 0;
}

