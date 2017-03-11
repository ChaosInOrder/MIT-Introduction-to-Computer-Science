class Solution(object):
    def heapSort(self,A):
        self.buildMaxHeap(A)
        for i in range(len(A),1,-1):
            A[i],A[1]=A[1],A[i]
            self.heapSize-=1
            self.maxHeapify(A,1)

    def buildMaxHeap(self,A):
        self.heapSize=len(A)+1
        for i in range(((len(A)+1)/2),1,-1):
            print i
            self.maxHeapify(A,i)


    def maxHeapify(self,A,i):
        l=2*i
        r=2*i+1
        if l<= self.heapSize and A[l]>A[i]:
            largest=l
        if r<=self.heapSize and A[r]>A[largest]:
            largest=r
        if largest!=i:
            A[i],A[largest]=A[largest],A[i]
            self.maxHeapify(A,largest)

sol=Solution()
A=[0,1,4,6,2,14,5,436,4]
sol.heapSort(A)
print A

