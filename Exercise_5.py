class IterativeQuickSort:
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

	def QuickSort(self, arr, l, h):
		st = []
		st.append(l)
		st.append(h)
		while(len(st) > 0):
			h = st[-1]
			del st[-1]
			l = st[-1]
			del st[-1]
			p = self.partition(arr, l, h)
			if p - 1 > l:
				st.append(l)
				st.append(p - 1)

			if p + 1 < h:
				st.append(p + 1)
				st.append(h)

	def printArray(self, arr):
		for i in arr:
			print(i, end =" ")
		print("\n")

	def main(self):
		arr = [4, 3, 5, 2, 1, 3, 2, 3]
		#arr = [10, 7, 8, 9, 1, 5]
		n = len(arr)
		self.QuickSort(arr, 0, n - 1)
		print("Sorted Array")
		self.printArray(arr)

if __name__ == "__main__":
	qb = IterativeQuickSort()
	qb.main()