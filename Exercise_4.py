class MergeSort:
	def merge(self, arr, l, m, r):
		pass

	def sort(self, arr):
		if len(arr) > 1:
			mid = len(arr)//2
			leftHalf = arr[:mid]
			rightHalf = arr[mid:]
			self.sort(leftHalf)
			self.sort(rightHalf)
			i = j = k = 0
			while i < len(leftHalf) and j < len(rightHalf):
				if leftHalf[i] < rightHalf[j]:
					arr[k] = leftHalf[i]
					i += 1
				else:
					arr[k] = rightHalf[j]
					j += 1
				k += 1
			
			while i < len(leftHalf):
				arr[k] = leftHalf[i]
				i += 1
				k += 1

			while j < len(rightHalf):
				arr[k] = rightHalf[j]
				j += 1
				k += 1

	def printArray(self, arr):
		for i in arr:
			print(i, end =" ")
		print("\n")

	def main(self):
		arr = [12, 11, 13, 5, 6, 7]
		self.sort(arr)
		print("Sorted Array")
		self.printArray(arr)

if __name__ == "__main__":
	qb = MergeSort()
	qb.main()