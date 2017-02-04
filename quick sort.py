class Solution(object):
    def quickSort(self,A,p,r):
        if p<r:
            q=self.partition(A,p,r)
            self.quickSort(A,p,q-1)
            self.quickSort(A,q+1,r)
        return A
    def partition(self,A,p,r):
        pivot=A[r]
        i=p-1
        j=p
        while j<=r-1:
            if A[j]<=pivot:
                i+=1
                A[j],A[i]=A[i],A[j]
            j+=1

        A[r],A[i+1]=A[i+1],A[r]
        return i+1

a=[2,5,7,1,3,7,4,7,9,4,3,2,5,7]
b=len(a)-1
print b
check=Solution()
print check.quickSort(a,0,b)