class QuickSort:
	"""
		This function takes last element as pivot, 
		places the pivot element at its correct 
		position in sorted array, and places all 
		smaller (smaller than pivot) to left of 
		pivot and all greater elements to right 
		of pivot
	"""
	def swap(self, arr, i, j):
		pass

	def partition(self, arr, low, high):
		pivot = arr[high]
		i = low - 1
		for j in range(low, high):
			if (arr[j] <= pivot):
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		return i + 1

	def sort(self, arr, low, high):
		if low < high:
			midPoint = self.partition(arr, low, high)
			self.sort(arr, low, midPoint - 1)
			self.sort(arr, midPoint + 1, high)

	def printArray(self, arr):
		for i in arr:
			print(i, end =" ")
		print("\n")

	def main(self):
		arr = [10, 7, 8, 9, 1, 5]
		n = len(arr)
		self.sort(arr, 0, n - 1)
		print("Sorted Array")
		self.printArray(arr)

if __name__ == "__main__":
	qb = QuickSort()
	qb.main()