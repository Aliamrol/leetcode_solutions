# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
# Time --> O(1) for each method
# Space --> O(1) for each method.
# This problem had 2 points. First, import specific class of a library not all of the library. Second,
# instead of set, we can use a dictionary and a list for doing insert, remove and GetRandom in O(1) time.

from random import choice
class RandomizedSet(object):

    def __init__(self):
        self.DictIndex = {}
        self.values = [] # Just for doing random.choice() operation in O(1)


    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.DictIndex:
            self.DictIndex[val] = len(self.values)
            self.values.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.DictIndex:
            index = self.DictIndex[val]
            last_val = self.values[-1]

            self.values[index] = last_val
            self.DictIndex[last_val] = index

            self.values.pop()
            del self.DictIndex[val]
            return True
        else:
            return False

    
    
    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()