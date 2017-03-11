people=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

people=sorted(people,key=lambda x:x[1])
print people
res = []
for p in people:
    print (p[1],p)
    res.insert(p[1], p)

for i in range(1,10):
    print i

print (1+2)/2