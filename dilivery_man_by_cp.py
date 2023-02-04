from ortools.sat.python import cp_model

def main():
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
  num_customers=5 
  num_vehicles=3
  # Define the decision variables.
  route = {}
  for k in range(num_vehicles):
    for i in range(num_customers+1):
      for j in range(num_customers+1):
        route[(k,i,j)] = model.NewBoolVar('route_%d_%d_%d' % (k,i, j))
  for i in range(1,num_customers+1): 
    model.Add(sum(route[(k,i,j)] for j in range(num_customers+1) for k in range(num_vehicles) if i!=j)==1)
  for j in range(1,num_customers+1):
    model.Add(sum(route[(k,i,j)] for i in range(num_customers+1) for k in range(num_vehicles) if i!=j)==1)
  for k in range(num_vehicles):  
    model.Add(sum(route[(k,0,j)] for j in range(1,num_customers+1))==1)
  for k in range(num_vehicles):  
    model.Add(sum(route[(k,j,0)] for j in range(1,num_customers+1))==1)
  for k in range(num_vehicles):
    for h in  range(1,num_customers+1):
      model.Add(
        sum(route[(k,i,h)] for i in range(num_customers+1) if i!=h)
        -
        sum(route[(k,h,j)] for j in range(num_customers+1) if j!=h)
        ==0
      )

    

  for h in range(1,num_customers+1):
    vehicle_in=sum(route[(k,h,j)] for j in range(1,num_customers+1) for k in range(num_vehicles) if h!=j)
    
    vehicle_out=sum(route[(k,j,h)] for j in range(1,num_customers+1) for k in range(num_vehicles) if h!=j)
    
    model.Add(vehicle_in+vehicle_out<=1)

  
  obj=sum(distance[i][j]*route[(k,i,j)] for i in range(num_customers+1) for j in range(num_customers+1) for k in range(num_vehicles) if j!=0)
  model.Minimize(obj)
  
  solver = cp_model.CpSolver()
  status = solver.Solve(model)
  if status == cp_model.OPTIMAL:
    print('Minimal total distance: %d' % (solver.ObjectiveValue()+sum(deliver_time)))
    for k in range(num_vehicles):
        customers_visited = []
        for i in range(num_customers+1):
          for j in range(num_customers+1):
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
