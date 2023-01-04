def find_best_position(node, solution):
    min_insert_cost = 999999999
    distance_matrix = solution.instance.distance_matrix
    position = None

    for i in range(len(solution.routes)):
        if solution.routes[i].can_insert(node):
            for j in range(0, len(solution.routes[i].route) - 1):
                before_node = solution.routes[i].route[j].id
                after_node = solution.routes[i].route[j + 1].id
                insert_cost = distance_matrix[before_node][node.id] + distance_matrix[node.id][after_node] - \
                              distance_matrix[before_node][after_node]
                if insert_cost < min_insert_cost:
                    position = (i, j)

    return position


def greedy_repair(solution):
    """
    :param solution: (Solution) the solution to be repaired
    :return: None

    Ham nay sua nghiem sau khi da pha
    """
    # Nghiem co mot ti le thap khong sua duoc nen se phai xu ly neu phat sinh
    try:
        for node in solution.extracted_node:
            position = find_best_position(node, solution)
            solution.routes[position[0]].insert(node, position[1])

        solution.extracted_node = []
        solution.update_total_cost()
        return solution
    except Exception:
        pass


