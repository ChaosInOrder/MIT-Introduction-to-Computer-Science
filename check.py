class node():
    def __init__(self, info=None):
        # node should be a tuple (key, count, pos linked list)
        self.info = info
        self.next = None

a=node(["22",1,node()])
b="a,b"

print filter(lambda c: c.isalpha(), b)
print b