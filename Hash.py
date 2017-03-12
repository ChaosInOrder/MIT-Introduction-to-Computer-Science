class node(object):
    def __init__(self, info=None):
        # node should be a list [key, count, pos linked list]
        self.info = info
        self.next = None

class wordInfo(object):
    def __init__(self):
class hash(object):
    """
    Use BKDR Hash algorithm, and implement the extra credit
    """
    def __init__(self,size=10000,text=None):
        self.size=size
        self.map=[0 for i in range(size)]
        for i,word in enumerate(text):
            self.insert(word,i)

    def BKDRHash(self,word):
        seed=131
        hash=0
        for i in word:
            hash+=seed*hash+ord(i)
        return hash%self.size

    def insert(self,key,value):
        hashNum=self.BKDRHash(key)
        head=self.map[hashNum]
        hasKey=False
        if not head:
            self.map[hashNum]=node([key,1,node(value)])
            return
        else:
            while not hasKey:
                if head.info[0]==key:
                    head.info[1]+=1
                    pos = head.info[2]
                    while pos.next: pos=pos.next
                    pos.next=node(value)
                    hasKey=True
                elif head.next==None:
                    head.next=node([key,1,node(value)])
                    hasKey=True
                else: head=head.next

    def delete(self,key):
        if self.find(key):
            hashNum = self.BKDRHash(key)
            head = self.map[hashNum]
            if head.info[0]==key:
                self.map[hashNum]=head.next
            while head.next:
                if head.next.info[0]==key:
                    head.next=head.next.next
                    print ("Delete %s" %key)
                    return
                head=head.next

    def find(self,key):
        hashNum = self.BKDRHash(key)
        head=self.map[hashNum]
        while head and head.info:
            if head.info[0]==key:
                print("Key: %s, Appear %d times, at:%r" % (head.info[0], head.info[1], self.getPos(head.info[2])))
                return True
            head=head.next
        print "The key doesn't exist"
        return False

    def increase(self,key):
        if self.find(key):
            hashNum = self.BKDRHash(key)
            head = self.map[hashNum]
            if head.info[0]==key:
                print "Already first"
                return
            while head.next:
                if head.next.info[0]==key:
                    increase=head.next
                    head.next=head.next.next
                    increase.next = self.map[hashNum]
                    self.map[hashNum] = increase
                    return
                head=head.next

    def getPos(self,head):
        res=[]
        while head:
            res.append(head.info+1)
            head=head.next
        return res

    def listAllKey(self):
        for head in self.map:
             while head:
                print("Key: %s, Appear %d times, at:%r" % (head.info[0], head.info[1], self.getPos(head.info[2])))
                head=head.next

a = "A human society is a group of people continued related to each other through continued relations, or a large social grouping sharing the same geographical or virtual territory, same interests, subject to the same political authority and dominant cultural expectations. Human societies are characterized by patterns of relationships social relations between individuals who share a distinctive culture and institutions. A given society may be described as the sum total of such relationships among its constituent members. In the social sciences, a larger society often evinces stratification and/or dominance patterns in subgroups. In so far as it is collaborative, a society can enable its members to benefit in ways that would not otherwise be possible on an individual basis; both individual and social common benefits can thus be distinguished, or in many cases found to overlap. A society can also consist of like-minded people governed by their own norms and values within a dominant, larger society. This is sometimes referred to as a subculture, a term used extensively within criminology: an organized group working together having a common interests, beliefs, or profession."
b="b b b a a d d"
def textProcess(text):
    info=text.split(" ")
    for i in range(len(info)):
        info[i]=filter(lambda c: c.isalpha(), info[i])
    return info

text = textProcess(a)

hashTable=hash(1,text)
hashTable.listAllKey()