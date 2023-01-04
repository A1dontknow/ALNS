from Instance import Instance
from CVRP.Algorithm import NearestNeighbor
from CVRP.Algorithm.DestroyOperator.ShawDestroy import shaw_destroy
from CVRP.Algorithm.RepairOperator import greedy_repair
from CVRP.Algorithm.RepairOperator import random_repair
from CVRP.Config import Config
from copy import deepcopy

# File chi de test mot so "tinh nang". Khong con su dung nua
a = Instance("A-n33-k5.txt")
test = NearestNeighbor(a)
print("Optimal value = ", a.optimal)
sol = test.get_initial_solution()
print(sol)
counter = 0
for i in range(Config.ITERATION):
    sol2 = deepcopy(sol)
    sol2 = shaw_destroy(sol2, int(Config.DESTROY_RATIO * sol.instance.dimensions), Config.D)
    if counter == 0:
        sol2 = random_repair(sol2)
    else:
        sol2 = greedy_repair(sol2)
        counter -= 1

    if sol2.totalCost <= sol.totalCost:
        sol = sol2
        counter = 0


print(sol)

