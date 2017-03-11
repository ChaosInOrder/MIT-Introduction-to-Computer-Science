class hash(object):
    class node():
        def __init__(self,key=None):
            self.key=key
            self.next=None

    def __init__(self,size=100000,test=None):
        self.size=size
        if not test:
            map=[]

    def BKDRHash(self,word):
        seed=131
        hash=0
        for i in word:
            hash+=seed*hash+ord(i)
        return hash%self.size
