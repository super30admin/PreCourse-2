class MyHashSet(object):

    def __init__(self):
        self.MAX = 10000
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self,key):
        #if the key is a string do the below lines 9 thro 11, line 12  return h % self.MAX
        # get the ASCII equivalent of each character and sum it up. then do mod operation on           # sum with total size of array
        #h = 0
        #for char in key:
        #    h += ord(char)
        return key % self.MAX
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.get_hash(key)
        if self.arr[h] == None:
            self.arr[h] = [key]
        else:
            self.arr[h].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self.get_hash(key)
        if self.arr[h] != None:
            # we go inside a while loop to remove all instances of the key, for ex if there are             # duplicates remove those as well. Calling remove after line 32 deletes only first             # instance of the key
            while key in self.arr[h]:
                self.arr[h].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        h = self.get_hash(key)
        if self.arr[h] != None:
            return key in self.arr[h]
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)