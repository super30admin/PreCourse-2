#time complexity : O(nlogn)
#space complexity O(1)
class solution:
    def quicksort(self,a,left,right):
        if(left<right):
            pivotposition = self.partition(a,left,right)
            self.quicksort(a,left,pivotposition-1)
            self.quicksort(a,pivotposition+1,right)

    def partition(self,a,l,r):
         pivot=a[r]
         i=l-1
         for j in range(l,r):
             if(a[j]<=pivot):
                i=i+1
                self.swap(a, i, j)

         self.swap(a,i+1,r)
         return i+1

    def swap(self,a,f,s):
        tmp=a[f]
        a[f]=a[s]
        a[s]=tmp





s = solution()
a=[4,0,8,6,3,155,100,96]
s.quicksort(a, 0, len(a)-1)
print(str(a))
  
 
