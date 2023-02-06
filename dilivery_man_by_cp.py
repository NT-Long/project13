from ortools.sat.python import cp_model


def main():
  #input data here
  model = cp_model.CpModel()
  distance = [
    [0, 10, 75, 90, 5, 10], 
    [10, 0, 100, 25, 40,15],
    [75, 100, 0, 30, 25,40], 
    [90, 25, 30, 0, 30,45],
    [5, 40, 25, 30, 0, 35],
    [10, 15, 40, 45, 35, 0]
    ]
  deliver_time = [0,1,1,2,2,3]
  N=5 
  K=3
  # Define the decision variables.
  route = {}
  for k in range(K):
    for i in range(N+1):
      for j in range(N+1):
        route[(k,i,j)] = model.NewBoolVar('route_%d_%d_%d' % (k,i, j))
  #Exactly 1 vehicle goes into point [ j ] for every point [ j ] ≠ 0
  for i in range(1,N+1): 
    model.Add(sum(route[(k,i,j)] for j in range(N+1) for k in range(K) if i!=j)==1)
  #Exactly 1 vehicle goes out of point [ i ] for every point [ i ] ≠ 0
  for j in range(1,N+1):
    model.Add(sum(route[(k,i,j)] for i in range(N+1) for k in range(K) if i!=j)==1)
  #. All vehicles have to start at point 0
  for k in range(K):  
    model.Add(sum(route[(k,0,j)] for j in range(1,N+1))==1)
  #If a vehicle go into point h ≠ 0, then it has to go out of point h

  for k in range(K):
    for h in  range(1,N+1):
      model.Add(
        sum(route[(k,i,h)] for i in range(N+1) if i!=h)
        -
        sum(route[(k,h,j)] for j in range(N+1) if j!=h)
        ==0
      )

    
  #all customers visited exactly one
  for h in range(1,N+1):
    vehicle_in=sum(route[(k,h,j)] for j in range(1,N+1) for k in range(K) if h!=j)
    
    vehicle_out=sum(route[(k,j,h)] for j in range(1,N+1) for k in range(K) if h!=j)
    
    model.Add(vehicle_in+vehicle_out<=1)

  #object fuction
  obj=sum(distance[i][j]*route[(k,i,j)] for i in range(N+1) for j in range(N+1) for k in range(K) if j!=0)
  model.Minimize(obj)
  #solve
  solver = cp_model.CpSolver()
  status = solver.Solve(model)
  #print method
  if status == cp_model.OPTIMAL:
    print('Minimal total distance: %d' % (solver.ObjectiveValue()+sum(deliver_time)))
    for k in range(K):
        customers_visited = []
        for i in range(N+1):
          for j in range(N+1):
            if solver.Value(route[k,i,j]) == 1 and j!=0 :
              if i not in customers_visited:    
                customers_visited.append(i)
              if j not in customers_visited:
                customers_visited.append(j)
        print('delivery man %d : %s' % (k+1,customers_visited))
        
  else:
        print('No solution found.')

if __name__ == '__main__':
  main()
