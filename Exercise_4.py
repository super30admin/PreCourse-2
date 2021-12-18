# Time complexity O(nLogn)
# Space complexity O(n)
# Github Reff :- https://github.com/mandgenikhil/comparison_based_sorting_algo.git

class MergeSort:
    __arr = []

    #Constructor : Will take input array (Must be called before calling sort)
    def __init__(self,array):
        self.__arr = array
    
    #Exchanging Data : Will InterChange The Current Array Values with current changing indices
    def exchange_data(self,arr,x,y,arr_c):
        while x < len(arr_c):
                arr[y] = arr_c[x]
                x += 1
                y += 1
        pass
    
    def __sort(self,input_data):
        if len(input_data) > 1:
            value_mid = int(len(input_data)/2)
            arr_right = input_data[value_mid:]

            arr_left = input_data[:value_mid]
            self.__sort(arr_left)
            self.__sort(arr_right)
            temp_x=0
            temp_y =0
            temp_z = 0
            while temp_x < len(arr_left) and temp_y < len(arr_right):
                if arr_left[temp_x] < arr_right[temp_y]:
                    input_data[temp_z] = arr_left[temp_x]
                    temp_x += 1
                else:
                    input_data[temp_z] = arr_right[temp_y]
                    temp_y += 1
                temp_z += 1

            self.exchange_data(input_data,temp_x,temp_z,arr_left)
            self.exchange_data(input_data,temp_y,temp_z,arr_right)

    def sort1(self):
        self.__sort(self.__arr)

    def print(self):
        print(self.__arr)
  
  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print("Given array is", end="\n")  
    m_obj = MergeSort(arr)
    m_obj.print()
    m_obj.sort1() 
    print("Sorted array is: ", end="\n") 
    m_obj.print() 
