time = [
    [0, 10, 75, 90, 5, 10], 
    [10, 0, 100, 25, 40,15],
    [75, 100, 0, 30, 25,40], 
    [90, 25, 30, 0, 30,45],
    [5, 40, 25, 30, 0, 35],
    [10, 15, 40, 45, 35, 0]
]
N=[1,2,3,4,5]
to_writte=[-1 for x in range(len(N))]
K=[1,2,3]
n=len(N)
answer={}
for i in range(n):
    for i1 in range(len(K)):
        answer[i]=i1
note=[]
def permutation(lst):

	# If lst is empty then there are no permutations
	if len(lst) == 0:
		return []

	# If there is only one element in lst then, only
	# one permutation is possible
	if len(lst) == 1:
		return [lst]

	# Find the permutations for lst if there are
	# more than 1 characters

	l = [] # empty list that will store current permutation

	# Iterate the input(lst) and calculate the permutation
	for i in range(len(lst)):
	    m = lst[i]

	    # Extract lst[i] or m from the list. remLst is
	    # remaining list
	    remLst = lst[:i] + lst[i+1:]

	    # Generating all permutations where m is first
	    # element
	    for p in permutation(remLst):
		    l.append([m] + p)
	return l
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
result=10000000000
opt=100000000000000
for i in note:
    last_move=[]
    for k in K:
        x=[]
        for m1 in range(len(i)):
            if i[m1] == k:
                
                x.append(m1+1)
        last_move.append(x[::1])
    pathcost=0 

    for delivery in last_move:
        optCost=10000000000
        if delivery ==[]:
            optCost=0
        for path in permutation(delivery):
            cost=time[0][path[0]]
            
            for way in range(len(path)-1):
                cost=cost+time[path[way]][path[way+1]]  #check again
            optCost=min(cost,optCost) 
        pathcost+=optCost

    if pathcost<result:
        result=pathcost
        opt=last_move
[print('delivery man ',x+1,' ',opt[x]) for x in range(len(opt))]
print('optimal solution result: ',result)


