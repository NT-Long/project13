# input information here
N =5
K =3
deliver_time = [2,3,1,2,2,3,3,1,2]
distance = [[0, 10, 75, 90, 5, 10], 
    [10, 0, 100, 25, 40,15],
    [75, 100, 0, 30, 25,40], 
    [90, 25, 30, 0, 30,45],
    [5, 40, 25, 30, 0, 35],
    [10, 15, 40, 45, 35, 0]]
N=[x for x in range(1,N+1)]
K=[x for x in range(1,K+1)]
n=len(N)
to_writte=[-1 for x in range(len(N))]
answer={}
for i in range(n):
    for i1 in range(len(K)):
        answer[i]=i1

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
#Try function to check each outcome
def Try(i):
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
    return pathcost,last_move
result=float('inf')
opt=float('inf')
#using backtracking to try all possible outcomes
def possible(N,K,answer,m):
    global result,opt
    if m==len(N):
        
        a=answer[::1]
        pathcost,last_move= Try(a)
        if pathcost<result:
            result=pathcost
            opt=last_move

        return 
    
    for i in K:
        answer[m]=i
        possible(N,K,answer,m+1)

possible(N,K,to_writte,0)

#check each outcome

    
print('Minimal solution result: ',result+sum(deliver_time))
final=[]

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

