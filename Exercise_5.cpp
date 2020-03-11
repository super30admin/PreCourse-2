// Time Complexity :O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this : N/A


// Your code here along with comments explaining your approach



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
    
    //Temporary stack
    int stack[high];
    int top=-1;
    int  partition_low=0, partition_high=0;
    int pivot_index=0;

    //Push initial upper and lower bounds
    stack[++top] = low;
    stack[++top] = high;

    while(top>=0){
        //Pop the top upper and lower bounds
        partition_high= stack[top--];
        partition_low = stack[top--];
        pivot_index = partition(arr, partition_low, partition_high);

        //Stack the upper and lower bounds after the partition
        //upper half
        if(pivot_index+1 < partition_high){
            stack[++top] = pivot_index+1;
            stack[++top] = partition_high;
        }
        // lower half
        if(partition_low < pivot_index-1){
            stack[++top] = partition_low;
            stack[++top] = pivot_index-1;
        }

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


