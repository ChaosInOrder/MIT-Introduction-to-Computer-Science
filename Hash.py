
class hash(object):
    class node():
        def __init__(self,key):
            self.key=key
            self.next=None

    def __init__(self):
        map=[]

    def delete(self,key):
        if key not in map:
            return
        map.remove(key)

    def insert(self,key,value):
        if not
