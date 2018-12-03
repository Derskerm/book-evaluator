class BookData:
    def __init__(self, title, author, rank):
        self.title = title
        self.author = author
        self.rank = rank
        self.count = 1

    def __str__(self):
        return self.title.title() + " by " + self.author.title() + f": {self.rank:.2f} ({self.count:d})"
    
    def compare_to(self, other):
        if self.title > other.title:
            return 1
        elif self.title < other.title:
            return -1
        else:
            if self.author > other.author:
                return 1
            elif self.author < other.author:
                return -1
            else:
                return 0
    
    def merge_in(self, other):
        self.rank += other.rank
        self.count += 1

class RankData:
    def __init__(self, book_datum):
        self.title = book_datum.title
        self.author = book_datum.author
        self.rank = book_datum.rank
        self.count = book_datum.count

    def __str__(self):
        return self.title.title() + " by " + self.author.title() + f": {self.rank:.2f} ({self.count:d})"
    
    def compare_to(self, other):
        if self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return -1
        else:
            if self.count > other.count:
                return 1
            elif self.count < other.count:
                return -1
            else:
                if self.title > other.title:
                    return -1
                elif self.title < other.title:
                    return 1
                else:
                    if self.author > other.author:
                        return -1
                    elif self.author < other.author:
                        return 1
                    else:
                        return 0
    
    def merge_in(self, other):
        pass

class BookNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):
        if self.data:
            cmp = self.data.compare_to(data)
            if cmp < 0:
                if self.left is None:
                    self.left = BookNode(data)
                else:
                    self.left.insert(data)
            elif cmp > 0:
                if self.right is None:
                    self.right = BookNode(data)
                else:
                    self.right.insert(data)
            else:  # data == self.data
                self.data.merge_in(data)
        else:
            self.data = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def to_list(self):
        ret_list = []
        def helper(self, lst):
            if self.left:
                helper(self.left, lst)
            lst.append(self.data)
            if self.right:
                helper(self.right, lst)
        helper(self, ret_list)
        return ret_list
        