from CVRP.Instances.Instance import Instance
from CVRP.Algorithm import NearestNeighbor
from CVRP.Algorithm.RepairOperator import greedy_repair
from CVRP.Algorithm.RepairOperator import random_repair
from CVRP.Config import Config
from copy import deepcopy
import matplotlib.pyplot as plt

# File chi de test mot so "tinh nang". Khong con su dung nua
for _ in range(1):
    a = Instance("A-n80-k10.txt")
    test = NearestNeighbor(a)
    sol = test.get_initial_solution()
    counter = 0

    for i in range(Config.ITERATION):
        sol2 = deepcopy(sol)
        if (i + 1) % 40 == 0:
            sol2 = MassiveDestroy.massive_destroy(sol2)
        elif (i + 1) % 20 == 0:
            sol2 = RandomDestroy.random_destroy(sol2, int(Config.DESTROY_RATIO * sol.instance.dimensions))
        elif (i + 1) % 5 == 0:
            sol2 = WorstDestroy.worst_destroy(sol2, int(Config.DESTROY_RATIO * sol.instance.dimensions))
        else:
            sol2 = ShawDestroy.shaw_destroy(sol2, int(Config.DESTROY_RATIO * sol.instance.dimensions), Config.D)


        if counter == 0:
            sol2 = random_repair(sol2)
        else:
            sol2 = greedy_repair(sol2)
            counter -= 1

        if sol2 is not None:
            if sol2.totalCost <= sol.totalCost:
                sol = sol2
                counter = 2
            print(sol2.totalCost)

    for route in sol.routes:
        x = []
        y = []
        for node in route.route:
            x.append(node.x)
            y.append(node.y)
        plt.plot(x, y)
    plt.title("VRP Solution (Cost = " + str("%.2f" % sol.totalCost) + ")")
    plt.show()
