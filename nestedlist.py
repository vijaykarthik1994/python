if __name__ == '__main__':
 students=[]
 scorelist=[]
 result=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
    
for st in students:
    scorelist.append(st[1])
sortedlist=set(scorelist);
sortedlist = sorted(sortedlist)
if len(sortedlist) == 1:
    lowest=sortedlist[0]
else:
    lowest=sortedlist[1]
for st in students:
    if st[1] == lowest:
        result.append(st[0])
result.sort()
for dt in result:
    print(dt)
    
    
        


