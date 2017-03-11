class Solution(object):
    def insertionSort(self,A):
        n=len(A)
        for j in range(1,n):
            key=A[j]
            i=j-1
            while i>=0 and A[i]>key:
                A[i+1]=A[i]
                i-=1
            A[i+1]=key



sol=Solution()
A=[8,7,64,3,34]
sol.insertionSort(A)
print A
