# input information here
deliver_time = [0,1,1,2,2,3]
distance = [
    [0, 10, 75, 90, 5, 10], 
    [10, 0, 100, 25, 40,15],
    [75, 100, 0, 30, 25,40], 
    [90, 25, 30, 0, 30,45],
    [5, 40, 25, 30, 0, 35],
    [10, 15, 40, 45, 35, 0]
]
N=5
K=3
N=[x for x in range(1,N+1)]
K=[x for x in range(1,K+1)]
n=len(N)
to_writte=[-1 for x in range(len(N))]
answer={}
for i in range(n):
    for i1 in range(len(K)):
        answer[i]=i1
note=[]
def permutation(lst):

	if len(lst) == 0:
		return []

	if len(lst) == 1:
		return [lst]

	l = [] 

	for i in range(len(lst)):
	    m = lst[i]
	    remLst = lst[:i] + lst[i+1:]
	    for p in permutation(remLst):
		    l.append([m] + p)
	return l
#using backtracking to listed all posible outcomes and then save it into note
def posible(N,K,answer,m):
    global note
    if m==len(N):
        a=answer[::1]
        note.append(a)
        return 
    
    for i in K:
        answer[m]=i
        posible(N,K,answer,m+1)
posible(N,K,to_writte,0)
result=float('inf')
opt=float('inf')
#check each outcome
for i in note:
    last_move=[]
    for k in K:
        x=[]
        for m1 in range(len(i)):
            if i[m1] == k:
                
                x.append(m1+1)
        last_move.append(x[::1])
    pathcost=0 
    #for each outcome, check all available path of each 
    for delivery in last_move:
        optCost=float('inf')
        if delivery ==[]:
            optCost=0
        for path in permutation(delivery):
            cost=distance[0][path[0]]
            
            for way in range(len(path)-1):
                cost=cost+distance[path[way]][path[way+1]]
            optCost=min(cost,optCost) 
        pathcost+=optCost
    #save best possibility of each iteration
    if pathcost<result:
        result=pathcost
        opt=last_move
print('Minimal solution result: ',result+sum(deliver_time))
final=[]
#print minimal path of each delivery mans
o=0
for delivery in opt:
        m=[]
        optCost=float('inf')
        for path in permutation(delivery):
            cost=distance[0][path[0]]
            
            for way in range(len(path)-1):
                cost=cost+distance[path[way]][path[way+1]]  #check again
            if cost<=optCost:
                optCost=cost
                m=path
                o+=cost
        final.append(m)
[print('delivery man ',x+1,':',final[x]) for x in range(len(final))]

