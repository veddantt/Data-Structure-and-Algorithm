class SmallestInfiniteSet(object):

    def __init__(self):
        self.added_back = set()
        self.next_smallest = 1

    def popSmallest(self):
        if self.added_back:
            smallest = min(self.added_back)
            self.added_back.remove(smallest)
            return smallest

        self.next_smallest += 1
        return self.next_smallest - 1

    def addBack(self, num):
        if num < self.next_smallest:
            self.added_back.add(num)