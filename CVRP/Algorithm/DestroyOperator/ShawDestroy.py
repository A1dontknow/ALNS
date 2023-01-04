from random import choice, randint, random
from copy import deepcopy


def get_in_plan(routes, to_remove):
    i = randint(0, len(routes) - 1)
    counter = 1
    while len(routes[i].route) < to_remove + 2:
        try:
            i = randint(0, len(routes) - 1)
            counter += 1
        except counter == 100:
            print("ShawDestroy: Invalid number to removes")
    return i


def rank_using_relatedness(v, visit_sets, distance_matrix):
    visit_list = []
    for visit in visit_sets:
        # Khong xet depot
        if visit.id != 0:
            relate = distance_matrix[v.id][visit.id]
            visit_list.append((visit, relate))
    visit_list.sort(key=lambda x: x[1], reverse=False)
    return visit_list


def shaw_destroy(solution, to_remove, d):
    """
    :param solution: (Solution) the solution to be destroyed
    :param to_remove: (int) the numbers of customers will be removed
    :param d: (float) Deterministic parameter
    :return: partial solution

    Ham nay duoc implement tu bai bao Shaw P. Using constraint programming and local search
    methods to vehicle routing problem. Lecture Notes in Computer Science 1998;1520:417–30
    """

    selected_route = get_in_plan(solution.routes, to_remove)
    visit_sets = deepcopy(solution.routes[selected_route].route)
    v = visit_sets[randint(1, len(visit_sets) - 2)]
    visit_sets.remove(v)
    removed = [v]

    while len(removed) < to_remove:
        v = choice(removed)
        # Rank visits in plan with respect to relatedness to v. Rank will be decreasing order
        lst = rank_using_relatedness(v, visit_sets, solution.instance.distance_matrix)
        rand = random()
        v = lst[int((len(lst) - 1) * rand ** d)][0]
        removed.append(v)
        visit_sets.remove(v)

    for node in removed:
        solution.routes[selected_route].erase(node.id)
        solution.extracted_node.append(node)

    return solution
