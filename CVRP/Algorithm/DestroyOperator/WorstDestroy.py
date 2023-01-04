def find_worst_position(solution):
    max_cost = 0
    distance_matrix = solution.instance.distance_matrix
    position = None

    for i in range(len(solution.routes)):
        # ko xet 2 cai depot tren 1 route
        for j in range(1, len(solution.routes[i].route) - 2):
            current_node = solution.routes[i].route[j].id
            before_node = solution.routes[i].route[j - 1].id
            after_node = solution.routes[i].route[j + 1].id
            cost = distance_matrix[before_node][current_node] + distance_matrix[current_node][after_node] - distance_matrix[before_node][after_node]
            if cost > max_cost:
                position = (i, j)

    return position


def worst_destroy(solution, to_remove, d=None):
    """
    :param solution: Nghiem can duoc pha
    :param to_remove: So luong khach hang se loai bo
    :return: Nghiem sau khi pha

    Ham nay se loai bo nhung khach hang nao co cost cao nhat
    """
    removed = []
    while len(removed) < to_remove:
        position = find_worst_position(solution)
        remove_node = solution.routes[position[0]].route[position[1]]
        removed.append(remove_node)
        solution.routes[position[0]].erase(remove_node.id)

    solution.extracted_node = removed
    return solution

