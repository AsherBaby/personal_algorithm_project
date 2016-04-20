class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.ds = nestedList
        self.idx = 0
        self.stack = []
        self.find_next()

    def find_next(self):
        while ((self.idx < len(self.ds) and isinstance(self.ds[self.idx], list)) or
               (self.idx == len(self.ds) and self.stack)):
            if self.idx == len(self.ds):
                self.ds, self.idx = self.stack.pop()
                continue
            if self.idx < len(self.ds) - 1:
                self.stack.append((self.ds, self.idx+1))
            self.ds = self.ds[self.idx]
            self.idx = 0

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        ans = self.ds[self.idx]
        self.idx += 1
        if self.idx < len(self.ds) and isinstance(self.ds[self.idx], int):
            return ans
        self.find_next()
        return ans


    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        return self.idx < len(self.ds)
